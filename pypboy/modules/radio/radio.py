import pypboy
import settings
import pygame
import os
import imp
import glob
import time
import game
from collections import deque
import mutagen
import random
import configparser
import sys

from pypboy.modules.data import entities
import pypboy.data

class Module(pypboy.SubModule):

    label = "RADIO"

    def __init__(self, *args, **kwargs):
        super(Module, self).__init__(*args, **kwargs)

        self.audiofolders = 'sounds/radio/'
        self.stations = []
        self.station_menu = []
        self.station_list = []
        self.station_list = self.get_station_data()
        self.station_waveforms = []
        self.total_length = 0
        self.station_meta_data_file = None
        self.station_files = []
        self.station_lengths = []

        self.grid = Grid()
        self.grid.rect[0] = 400
        self.grid.rect[1] = 180
        self.add(self.grid)

        self.animation = Animation()
        self.animation.rect[0] = 400
        self.animation.rect[1] = 190
        self.add(self.animation)

        for station in self.station_list:
            # station_data = [station_name, folder, station_files, station_ordered, station_lengths, total_length]
            station_folder = station[1]+"/"
            station_name = station[0]
            self.station_menu.append([station_name])
            self.stations.append(entities.RadioClass(station_name,station_folder,station))

        for station in self.stations:
            self.add(station)
        self.active_station = None
        settings.radio = self

        stationCallbacks = []
        for i, station in enumerate(self.stations):
            stationCallbacks.append(lambda i=i: self.select_station(i))

            # print ("station labels = ",stationLabels)
            # print ("station callbacks = ",stationCallbacks)

        self.menu = pypboy.ui.Menu(self.station_menu, stationCallbacks, settings.STATION)
        self.menu.rect[0] = settings.menu_x
        self.menu.rect[1] = settings.menu_y
        self.add(self.menu)
        # self.menu.select(settings.STATION)

    def select_station(self, station):
        if hasattr(self, 'active_station') and self.active_station:
            self.active_station.new_selection = True
            # self.active_station.stop()
        self.active_station = self.stations[station]
        settings.STATION = station
        self.active_station.play_song()

    def handle_event(self, event):
        if event.type == settings.EVENTS['SONG_END']:
            if hasattr(self, 'active_station') and self.active_station:
                if self.active_station.new_selection:
                    self.active_station.new_selection = False
                else:
                    self.active_station.files.rotate(-1)
                    self.active_station.song_lengths.rotate(-1)
                    self.active_station.play_song()
                    self.active_station.new_selection = False
                    print("Song ended, Playing next song")
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_PAGEUP:
                if hasattr(self, 'active_station') and self.active_station:
                    self.active_station.volume_up()
            elif event.key == pygame.K_PAGEDOWN:
                if hasattr(self, 'active_station') and self.active_station:
                    self.active_station.volume_down()
            elif event.key == pygame.K_END:
                if hasattr(self, 'active_station') and self.active_station:
                    self.active_station.next_song()
            elif event.key == pygame.K_HOME:
                if hasattr(self, 'active_station') and self.active_station:
                    self.active_station.prev_song()
            elif event.key == pygame.K_DELETE:
                if hasattr(self, 'active_station') and self.active_station:
                    self.active_station.randomize_station()

    def get_station_data(self):
        
        # Get list of folders
        folders = []
        stations = []

        self.station_ordered = True
        for f in sorted(os.listdir(self.audiofolders)):
            if not f.endswith("/"):
                folders.append(self.audiofolders + f)

        for folder in folders:
            config = configparser.SafeConfigParser()

            folder_name = os.path.basename(folder)  # Get the folder name without the full path
            if len(glob.glob(folder+"/*.ogg")) == 0:
                print ("No .ogg files in:", folder)
                continue

            song_data = self.load_files(folder)
            self.station_files = song_data[0]
            self.station_lengths = song_data[1]

            self.station_meta_data_file = ("./" + folder + "/" + "station.ini")

            try:
                assert os.path.exists(self.station_meta_data_file)
                config.read(self.station_meta_data_file, encoding=None)
            except Exception as e:
                print("Error reading the following:",str(e))

            try:
                self.station_name = config.get('metadata', 'station_name')
                self.ordered = config.get('metadata', 'ordered')
            except Exception as e:
                self.station_name = folder_name
                self.station_ordered = True
                print(str(e), ' could not read configuration file')
            if not settings.do_not_use_cache:
                try:
                    self.station_waveforms = config.get('cache', 'waveforms')
                    print("Loaded cached waveforms in file", self.station_meta_data_file)
                except Exception as e:
                    self.station_waveforms = []
                    print(str(e), ' No cache section in', self.station_meta_data_file)
            else:
                print("Using live waveform generation")
                self.station_waveforms = []

            self.total_length = sum(self.station_lengths)

            if not self.station_waveforms and not settings.do_not_use_cache or settings.force_caching:  # Write cached data
                self.station_waveforms = self.process_waveforms(folder)
                print("Writing cache data to ", self.station_meta_data_file)
                try:
                    config.add_section("metadata")
                    config.set("metadata", "station_name", str(self.station_name))
                    config.set("metadata", "ordered", str(self.station_ordered))
                except Exception as e:
                    print(str(e))
                try:
                    config.add_section("cache")
                except Exception as e:
                    print(str(e))
                config.set("cache", "waveforms", str(self.station_waveforms))
                with open(self.station_meta_data_file, 'w') as configfile:
                    config.write(configfile)

            if not self.station_ordered:
                seed = random.random()
                random.Random(seed).shuffle(self.station_files)
                random.Random(seed).shuffle(self.station_lengths)
                random.Random(seed).shuffle(self.station_waveforms)

            station_data = self.station_name, folder, self.station_files, self.station_ordered, self.station_lengths,self.total_length, self.station_waveforms
            stations.append(station_data)

        return stations

    def process_waveforms(self, folder):
        print("started processing waveforms in folder",folder,"this may take a while")
        now = time.time()
        waveforms = []
        for file in sorted(os.listdir(folder)):
            if file.endswith(".ogg"):
                print ("Processing waveforms for file = ",file)
                frame_skip = int(48000 / 75) #sample rate / (25 fps * 3 pixels shift per frame)
                amplitude = pygame.sndarray.array(pygame.mixer.Sound("./" + folder + "/" + file))  # Load the sound file)
                amplitude = amplitude[:, 0] + amplitude[:, 1]

                amplitude = amplitude[::frame_skip]
                # frequency = list(abs(fft.fft(amplitude)))

                # scale the amplitude to 1/4th of the frame height and translate it to height/2(central line)
                max_amplitude = max(amplitude)
                for i in range(len(amplitude)):
                    amplitude[i] = float(amplitude[i]) / max_amplitude * 100 + 125

                waveform = [125] * 250 + list(amplitude)
                for x in range(100):  # Add end frames
                    waveform.append(125)
                waveforms.append(waveform)
        print("Finished processing waveforms in folder",folder,"Time:",time.time()-now)
        return waveforms

    def load_files(self, folder):
        files = []
        song_lengths = []

        for file in sorted(os.listdir(folder)):
            if file.endswith(".ogg"):
                files.append("./" + folder + "/" + file)
                song_lengths.append(mutagen.File("./" + folder + "/" + file).info.length)

        return [files,song_lengths]

class Animation(game.Entity):

    def __init__(self):
        super(Animation, self).__init__()

        self.width, self.height = 250, 250
        self.center = [self.width / 2, self.height / 2]
        self.image = pygame.Surface((self.width, self.height))
        self.animation_time = 0.04  # 25 fps
        self.prev_time = 0
        self.index = 0
        self.prev_song = 0
        settings.SONG = None

    def render(self, *args, **kwargs):

            self.current_time = time.time()
            self.delta_time = self.current_time - self.prev_time

            if self.delta_time >= self.animation_time:
                self.prev_time = self.current_time
                if not settings.SONG:
                    self.image.fill((0, 0, 0))
                    pygame.draw.line(self.image, [0, 255, 0], [0, self.height / 2], [self.width, self.height / 2], 2)
                elif settings.SONG:
                    self.image.fill((0, 0, 0))
                    self.index += 3
                    if settings.SONG != self.prev_song:
                        self.prev_song = settings.SONG
                        self.start_pos = settings.START_POS

                        try:
                            self.waveform = settings.WAVEFORM
                            print("Loading cached waveform for", settings.SONG)
                        except:
                            print("Generating waveform from",settings.SONG)
                            frame_skip = int(48000 / 75)
                            amplitude = pygame.sndarray.array(pygame.mixer.Sound(settings.SONG))  # Load the sound file)
                            amplitude = amplitude[:, 0] + amplitude[:, 1]

                            amplitude = amplitude[::frame_skip]

                            # scale the amplitude to 1/4th of the frame height and translate it to height/2(central line)
                            max_amplitude = max(amplitude)
                            for i in range(len(amplitude)):
                                amplitude[i] = float(amplitude[i]) / max_amplitude * int(
                                    self.height / 2.5) + self.height / 2

                            self.waveform = [int(self.height / 2)] * self.width + list(amplitude)
                            for x in range(100):  #Add end frames
                                self.waveform.append(125)

                        # print("new start position = ",settings.START_POS)
                        if not self.start_pos == 0:
                            self.index = int(self.start_pos*75) #Adjust for new start position
                        else:
                            self.index = 5
                        # print("New index=", self.index)
                    if self.index >= len(self.waveform) - 1:
                        self.index = 0

                    prev_x, prev_y = 0, self.waveform[self.index]
                    for x, y in enumerate(self.waveform[self.index + 1:self.index + 1 + self.width][::1]):
                        pygame.draw.line(self.image, [0, 255, 0], [prev_x, prev_y], [x, y], 2)
                        prev_x, prev_y = x, y

                    # Credit to https://github.com/prtx/Music-Visualizer-in-Python/blob/master/music_visualizer.py

class Grid(game.Entity):

    def __init__(self):
        super(Grid, self).__init__()

        self.image = pygame.Surface((270, 270))
        self.image.fill((0, 0, 0))
        long_line = 14
        long_lines = 10
        short_line = 9
        short_lines = long_lines * 3
        line_start = 0
        bottom = self.image.get_rect().bottom
        right = self.image.get_rect().right

        pygame.draw.lines(self.image, settings.light, False, [(0, 268), (268, 268), (268,0)],3)

        line_x = int(self.image.get_rect().height / long_lines)
        while long_lines >= 1:
            line_start += line_x
            pygame.draw.line(self.image, settings.light, (line_start, bottom), (line_start, bottom - long_line), 2)
            pygame.draw.line(self.image, settings.light, (right, line_start), (right - long_line, line_start), 2)
            long_lines -= 1

        line_start = 0
        line_x = int(self.image.get_rect().height / short_lines)
        while short_lines > 2:
            line_start += line_x
            pygame.draw.line(self.image, settings.light, (line_start, bottom), (line_start, bottom - short_line), 2)
            pygame.draw.line(self.image, settings.light, (right, line_start), (right - short_line, line_start), 2)
            short_lines -= 1
