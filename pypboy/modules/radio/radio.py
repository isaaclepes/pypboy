import pypboy
import settings
import pygame
import os
import imp
import glob

from pypboy.modules.data import entities

class Module(pypboy.SubModule):

    label = "RADIO"

    def __init__(self, *args, **kwargs):
        super(Module, self).__init__(*args, **kwargs)
        
        self.stations = []
        self.audiofolders = 'sounds/radio/'
        self.list_of_stations = []
        self.station_info = []
        self.list_folders()
        stationLabels = []
        stationCallbacks = []
        station_menu = []

        for self.station in self.list_of_stations:
            #Make station classes
            stationLabels.append(self.station[2])
            station_menu.append([self.station[2]])
            self.stations.append(entities.RadioClass(self.station[1],self.station[0]+"/"),)
             
        for station in self.stations:
            self.add(station)
        self.active_station = None
        settings.radio = self

        stationCallbacks = []
        for i, station in enumerate(self.stations):
            stationLabels.append(station.label)
            stationCallbacks.append(lambda i=i: self.select_station(i))


        #print ("station labels = ",stationLabels)
        #print ("station callbacks = ",stationCallbacks)
        self.menu = pypboy.ui.Menu(station_menu, stationCallbacks, 0)
        self.menu.rect[0] = settings.menu_x
        self.menu.rect[1] = settings.menu_y
        self.add(self.menu)

        self.menu.select(settings.STATION)

    def select_station(self, station):
        
        if hasattr(self, 'active_station') and self.active_station:
            self.active_station.stop()
        self.active_station = self.stations[station]
        if station != 0: #Allow position 0 to be off
            settings.STATION = station
            self.active_station.play_random() #Play a random station upon selection

    def handle_event(self, event):
        if event.type == settings.EVENTS['SONG_END']:
            if hasattr(self, 'active_station') and self.active_station:
                self.active_station.play_random()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_PAGEUP:
                self.active_station.volume_up()
            elif event.key == pygame.K_PAGEDOWN:
                self.active_station.volume_down()


    def list_folders(self):  
        
        #Get list of folders
        folders = []
        for f in os.listdir(self.audiofolders):
            if not f.endswith("/"):
                folders.append(self.audiofolders + f)

        #Get station_name from station.py
        for folder in folders:
            folder_name = os.path.basename(folder) #Get the folder name without the full path
            if len(glob.glob(folder+"/*.mp3")) + len(glob.glob(folder+"/*.ogg")) + len(glob.glob(folder+"/*.wav")) == 0:
                print ("No audio files in:", folder)
                continue 
            try:
                station = imp.load_source("station.py", os.path.join(folder,"station.py"))
                station_name = station.station_name
            except:
                station_name = folder_name
            
            self.list_of_stations.append([folder,folder_name,station_name])