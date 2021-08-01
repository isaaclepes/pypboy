import pypboy
import settings
import pygame
import os
import imp
import glob
import time
import game
from numpy import fft

from pypboy.modules.data import entities
import pypboy.data

class Module(pypboy.SubModule):

    label = "RADIO"

    def __init__(self, *args, **kwargs):
        super(Module, self).__init__(*args, **kwargs)
        
        self.stations = []
        self.audiofolders = 'sounds/radio/'
        self.list_of_stations = []
        self.list_folders()
        stationLabels = []
        station_menu = []
        stationOrdered = []
        self.new_selection = False

        self.grid = Grid()
        self.grid.rect[0] = 400
        self.grid.rect[1] = 180
        self.add(self.grid)

        self.animation = Animation()
        self.animation.rect[0] = 400
        self.animation.rect[1] = 190
        self.add(self.animation)



        for self.station in self.list_of_stations:
            #Make station classes
            stationLabels.append(self.station[2])
            stationOrdered.append(self.station[3])
            station_menu.append([self.station[2]])
            self.stations.append(entities.RadioClass(self.station[1],self.station[0]+"/"),)

        for station in self.stations:
            self.add(station)
        self.active_station = None
        settings.radio = self

        stationCallbacks = []
        for i, station in enumerate(self.stations):
            stationCallbacks.append(lambda i=i: self.select_station(i))

        #print ("station labels = ",stationLabels)
        #print ("station callbacks = ",stationCallbacks)
        self.menu = pypboy.ui.Menu(station_menu, stationCallbacks, settings.STATION)
        self.menu.rect[0] = settings.menu_x
        self.menu.rect[1] = settings.menu_y
        self.add(self.menu)
        #self.menu.select(settings.STATION)

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

    def list_folders(self):
        
        #Get list of folders
        folders = []
        for f in sorted(os.listdir(self.audiofolders)):
            if not f.endswith("/"):
                folders.append(self.audiofolders + f)

        #Get station_name from station.py
        for folder in folders:
            folder_name = os.path.basename(folder) #Get the folder name without the full path
            if len(glob.glob(folder+"/*.mp3")) == 0:
                print ("No MP3 files in:", folder)
                continue 
            try:
                station = imp.load_source("station.py", os.path.join(folder,"station.py"))
                station_name = station.station_name
                station_ordered = station.ordered

            except:
                station_name = folder_name
            
            self.list_of_stations.append([folder,folder_name,station_name,station_ordered])

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

    def render(self, *args, **kwargs):

            self.current_time = time.time()
            self.delta_time = self.current_time - self.prev_time

            if self.delta_time >= self.animation_time:
                self.prev_time = self.current_time
                if settings.SONG == None:
                    self.image.fill((0, 0, 0))
                    pygame.draw.line(self.image, [0, 255, 0], [0, self.height / 2], [self.width, self.height / 2], 2)
                elif settings.AMPLITUDE and settings.SONG:
                    self.index += 3
                    if settings.SONG != self.prev_song:
                        self.prev_song = settings.SONG
                        print("new start position = ",settings.START_POS)
                        if not settings.START_POS == 0:
                            self.index = int(settings.START_POS*75) #Adjust for new start position
                        else:
                            self.index = 5
                        print("New index=", self.index)

                    if self.index >= len(settings.AMPLITUDE[self.width:]):
                        self.index = 5

                    self.image.fill((0, 0, 0))

                    # Credit to https://github.com/prtx/Music-Visualizer-in-Python/blob/master/music_visualizer.py
                    prev_x, prev_y = 0, settings.AMPLITUDE[self.index]
                    for x, y in enumerate(settings.AMPLITUDE[self.index + 1:self.index + 1 + self.width][::1]):
                        pygame.draw.line(self.image, [0, 255, 0], [prev_x, prev_y], [x, y], 2)
                        prev_x, prev_y = x, y



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

