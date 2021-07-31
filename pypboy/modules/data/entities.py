import os

import mutagen

import game
import settings
import pygame
import threading
import pypboy.data
import time
import random
from mutagen.mp3 import MP3
import imp
from collections import deque

class Map(game.Entity):

    _mapper = None
    _transposed = None
    _size = 0
    _fetching = None
    _map_surface = None
    _loading_size = 0
    _render_rect = None

    def __init__(self, width, render_rect=None, loading_type="Loading map...", *args, **kwargs):
        self._mapper = pypboy.data.Maps()
        self._size = width
        self._map_surface = pygame.Surface((width, width))
        self._render_rect = render_rect
        super(Map, self).__init__((width, width), *args, **kwargs)
        text = settings.RobotoB[14].render(loading_type, True, (settings.bright), (0, 0, 0))
        self.image.blit(text, (10, 10))

    def fetch_map(self, position, radius, isWorld):
        self._fetching = threading.Thread(target=self._internal_fetch_map, args=(position, radius, isWorld))
        self._fetching.start()

    def _internal_fetch_map(self, position, radius, isWorld):
        self._mapper.fetch_by_coordinate(position, radius, isWorld)
        self.redraw_map()
        
    def load_map(self, position, radius, isWorld):
        self._fetching = threading.Thread(target=self._internal_load_map, args=(position, radius, isWorld))
        self._fetching.start()

    def _internal_load_map(self, position, radius, isWorld):
        self._mapper.load_map_coordinates(position, radius, isWorld)
        self.redraw_map()

    # def update(self, *args, **kwargs):
    #     super(Map, self).update(*args, **kwargs)

    def move_map(self, x, y):
        self._render_rect.move_ip(x, y)

    def redraw_map(self, coef=1):
        self._map_surface.fill((0, 0, 0))
        for way in self._mapper.transpose_ways((self._size / coef, self._size / coef), (self._size / 2, self._size / 2)):
            pygame.draw.lines(
                    self._map_surface,
                    (settings.mid), # Map line Color
                    False,
                    way,
                    2
            )
        for tag in self._mapper.transpose_tags((self._size / coef, self._size / coef), (self._size / 2, self._size / 2)):
            if tag[3] in settings.AMENITIES:
                image = settings.AMENITIES[tag[3]]
                pygame.transform.scale(image, (10, 10))
                self._map_surface.blit(image, (tag[1], tag[2]))
                text = settings.RobotoB[12].render(tag[0], True, (settings.bright), (0, 0, 0))
                self._map_surface.blit(text, (tag[1] + 17, tag[2] + 4))
            else:
                image = settings.MAP_ICONS['misc']

        self.image.blit(self._map_surface, (0, 0), area=self._render_rect)

class MapSquare(game.Entity):
    _mapper = None
    _size = 0
    _fetching = None
    _map_surface = None
    map_position = (0, 0)

    def __init__(self, size, map_position, parent, *args, **kwargs):
        self._mapper = pypboy.data.Maps()
        self._size = size
        self.parent = parent
        self._map_surface = pygame.Surface((size * 2, size * 2))
        self.map_position = map_position
        self.tags = {}
        super(MapSquare, self).__init__((size, size), *args, **kwargs)

    def fetch_map(self):
        self._fetching = threading.Thread(target=self._internal_fetch_map)
        self._fetching.start()

    def _internal_fetch_map(self):
        self._mapper.fetch_grid(self.map_position)
        self.redraw_map()
        self.parent.redraw_map()

    def redraw_map(self, coef=1):
        self._map_surface.fill((0, 0, 0))
        for way in self._mapper.transpose_ways((self._size, self._size), (self._size / 2, self._size / 2)):
            pygame.draw.lines(
                    self._map_surface,
                    (settings.mid),
                    False,
                    way,
                    1
            )
        for tag in self._mapper.transpose_tags((self._size, self._size), (self._size / 2, self._size / 2)):
            self.tags[tag[0]] = (tag[1] + self.position[0], tag[2] + self.position[1], tag[3])
        self.image.fill((0, 0, 0))
        self.image.blit(self._map_surface, (-self._size / 2, -self._size / 2))

class MapGrid(game.Entity):

    _grid = None
    _delta = 0.002
    _starting_position = (0, 0)

    def __init__(self, starting_position, dimensions, *args, **kwargs):
        self._grid = []
        self._starting_position = starting_position
        self.dimensions = dimensions
        self._tag_surface = pygame.Surface(dimensions)
        super(MapGrid, self).__init__(dimensions, *args, **kwargs)
        self.tags = {}
        self.fetch_outwards()

    def test_fetch(self):
        for x in range(10):
            for y in range(5):
                square = MapSquare(
                    100,
                    (
                        self._starting_position[0] + (self._delta * x),
                        self._starting_position[1] - (self._delta * y)
                    )
                )
                square.fetch_map()
                square.position = (100 * x, 100 * y)
                self._grid.append(square)

    def fetch_outwards(self):
        for x in range(-4, 4):
            for y in range(-2, 2):
                square = MapSquare(
                    86,
                    (
                        self._starting_position[0] + (self._delta * x),
                        self._starting_position[1] - (self._delta * y)
                    ),
                    self
                )
                square.fetch_map()
                square.position = ((86 * x) + (self.dimensions[0] / 2) - 43, (86 * y) + (self.dimensions[1] / 2) - 43)
                self._grid.append(square)


    def draw_tags(self):
        self.tags = {}
        for square in self._grid:
            self.tags.update(square.tags)
        self._tag_surface.fill((0, 0, 0))
        for name in self.tags:
            if self.tags[name][2] in settings.AMENITIES:
                image = settings.AMENITIES[self.tags[name][2]]
            #else:
            #	print "Unknown amenity: %s" % self.tags[name][2]
            #	image = settings.MAP_ICONS['misc']
                pygame.transform.scale(image, (10, 10))
                self.image.blit(image, (self.tags[name][0], self.tags[name][1]))
            # try:
                text = settings.RobotoB[12].render(name, True, (settings.bright), (0, 0, 0))
            # text_width = text.get_size()[0]
            # 	pygame.draw.rect(
            # 		self,
            # 		(0, 0, 0),
            # 		(self.tags[name][0], self.tags[name][1], text_width + 4, 15),
            # 		0
            # 	)
                self.image.blit(text, (self.tags[name][0] + 17, self.tags[name][1] + 4))
            # 	pygame.draw.rect(
            # 		self,
            # 		(95, 255, 177),
            # 		(self.tags[name][0], self.tags[name][1], text_width + 4, 15),
            # 		1
            # 	)
            # except Exception, e:
            # 	print(e)
            # 	pass

    def redraw_map(self, *args, **kwargs):
        self.image.fill((0, 0, 0))
        for square in self._grid:
            self.image.blit(square._map_surface, square.position)
        self.draw_tags()

class RadioStation(game.Entity):

    STATES = {
        'stopped': 0,
        'playing': 1,
        'paused': 2
    }
   
    def __init__(self, *args, **kwargs):
        super(RadioStation, self).__init__((10, 10), *args, **kwargs)
        self.state = self.STATES['stopped']

        self.total_length = 0
        self.song_lengths = []
        self.station_length = 0
        self.song_lengths = []
        self.filename = 0
        self.files = self.load_files()
        self.start_pos = 0
        self.new_selection = True
        self.last_filename = None

        pygame.mixer.music.set_endevent(settings.EVENTS['SONG_END'])

    def play_song(self):
        self.start_pos = 0
        if settings.SOUND_ENABLED:
            if self.files[0].endswith("Silence.mp3"):
                print("Radio off")
                self.stop()
            else:
                if hasattr(self, 'last_filename') and self.last_filename: #Support resuming
                    self.start_pos = self.last_playpos + (time.time() - self.last_playtime)
                    print ("Resuming song:", self.last_filename)

                if self.files:
                    if self.new_selection: # If changed stations manually
                        song_length = self.song_lengths[0]  # length of the current song
                        self.start_pos = time.time() - self.start_time
                        # print("time based start_pos =", self.start_pos)

                        if self.start_pos > song_length:
                            i = 0
                            lengths = list(self.song_lengths)
                            if self.start_pos > self.station_length:
                                print("start_pos longer than station length",self.start_pos,self.station_length)
                                self.start_time = time.time()
                                self.start_pos = 0
                            else:
                                while sum(lengths[0:i]) <= self.start_pos: #Find where in the station list we should be base on current time
                                    i += 1
                                    self.files.rotate(-1)
                                    self.song_lengths.rotate(-1)

                                i -= 1 #compensate for overshoot
                                self.files.rotate(1)
                                self.song_lengths.rotate(1)

                                self.sum_of_song_lengths = sum(lengths[0:i])
                                self.start_pos = self.start_pos - self.sum_of_song_lengths
                                self.start_time = time.time() - self.start_pos
                                print("Jumping to song index: :", i, "New Song Length =", lengths[i], "start_pos =",self.start_pos,"self.sum_of_song_lengths",self.sum_of_song_lengths)

                        self.new_selection = False
                        # print("-----------")
                        # print("New Selection")
                        # print("start_pos =", self.start_pos)
                        # print("Song length =",song_length)
                        # print("-----------")

                        # print ("Song to jump into is:: ",self.song_index,  "song time = ",song_time,"Song length =",self.song_lengths[self.song_index], "time_since_reset = ",time_since_reset, "start_pos = ",start_pos)

                    else:
                        print("Same station, new song")
                        self.start_pos = 0

                    self.filename = self.files[0]

                    pygame.mixer.music.load(self.filename)
                    pygame.mixer.music.play(0, self.start_pos)
                    self.state = self.STATES['playing']
                    print("Playing =", self.filename, "length =",str(round(self.song_lengths[0],2)), "start_pos =",str(round(self.start_pos,2)))

    
    def volume_up(self):   
        if settings.SOUND_ENABLED:
            print ("Volume up")
            settings.VOLUME = settings.VOLUME + 0.1 
            pygame.mixer.music.set_volume(settings.VOLUME)

    def volume_down(self):   
        if settings.SOUND_ENABLED:
            print ("Volume down")
            settings.VOLUME = settings.VOLUME - 0.1 
            pygame.mixer.music.set_volume(settings.VOLUME)
    
    def play(self):
        if settings.SOUND_ENABLED:
            if self.state == self.STATES['paused']:
                pygame.mixer.music.unpause()
                self.state = self.STATES['playing']
            else:
                self.play_song()
            print("Music resumed")
        
    def pause(self):
        if settings.SOUND_ENABLED:
            self.state = self.STATES['paused']
            pygame.mixer.music.pause()
            print("Music paused")
        
    def stop(self):
        if settings.SOUND_ENABLED:
            self.state = self.STATES['stopped']
            if self.filename:
                self.last_filename = self.filename
                self.last_playpos = pygame.mixer.music.get_pos()
                self.last_playtime = time.time()
            pygame.mixer.music.stop()
            print("Music stopped")

    def next_song(self):
        if settings.SOUND_ENABLED:
            print ("Next song")
            self.files.rotate(-1)
            self.song_lengths.rotate(-1)
            self.start_time = time.time()
            self.play_song()

    def prev_song(self):
        if settings.SOUND_ENABLED:
            print("Prev song")
            self.files.rotate(1)
            self.song_lengths.rotate(1)
            self.start_time = time.time()
            self.play_song()

    def load_files(self):
        files = deque([])
        self.total_length = 0
        self.song_lengths =  deque([])

        for f in sorted(os.listdir(self.directory)):
            if f.endswith(".mp3"):
                files.append(self.directory + f)
                self.song_lengths.append(MP3(self.directory + f).info.length)
        self.station_length = sum(self.song_lengths)

        try:
            station = imp.load_source("station.py", os.path.join(self.directory, "station.py"))
            self.station_ordered = station.ordered
            #print(self.station_ordered)

        except:
            self.station_ordered = False

        self.start_time = time.time()

        if not self.station_ordered:
            seed = random.random()
            random.Random(seed).shuffle(files)
            random.Random(seed).shuffle(self.song_lengths)


        return files
        
    def __le__(self, other):
        if type(other) is not RadioStation:
            return 0
        else:
            return self.label <= other.label
    
    def __ge__(self, other):
        if type(other) is not RadioStation:
            return 0
        else:
            return self.label >= other.label

class RadioClass(RadioStation):
    def __init__(self, station_name, folder_name, *args, **kwargs):
        self.label = station_name
        self.directory = folder_name
        super(RadioClass, self).__init__(self, *args, **kwargs)