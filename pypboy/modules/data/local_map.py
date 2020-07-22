import pygame
import pypboy
import config

from pypboy.modules.data import entities

class Module(pypboy.SubModule):
    label = "Local Map"
    load_cached_map = False
    zoom = 0.003

    def __init__(self, *args, **kwargs):
        super(Module, self).__init__(*args, **kwargs)
        #mapgrid = entities.MapGrid((-5.9302032, 54.5966701), (config.WIDTH - 8, config.HEIGHT - 80))
        self.mapgrid = entities.Map(config.WIDTH, pygame.Rect(4, (config.WIDTH - config.HEIGHT) / 2, config.WIDTH - 8, config.HEIGHT - 80))
        if(config.LOAD_CACHED_MAP):
            print("Loading cached map")
            self.mapgrid = entities.Map(config.WIDTH, pygame.Rect(4, (config.WIDTH - config.HEIGHT) / 2, config.WIDTH - 8, config.HEIGHT - 80), "Loading cached map")
            map_data_location = 'map.cache'
            self.mapgrid.load_map(config.MAP_FOCUS, self.zoom)
        else:
            print("Loading map from the internet")
            self.mapgrid = entities.Map(config.WIDTH, pygame.Rect(4, (config.WIDTH - config.HEIGHT) / 2, config.WIDTH - 8, config.HEIGHT - 80), "Loading map from the internet")
            self.mapgrid.fetch_map(config.MAP_FOCUS, self.zoom)
        self.add(self.mapgrid)
        self.mapgrid.rect[0] = 4
        self.mapgrid.rect[1] = 40
    
    def handle_action(self, action, value=0):
        if action == "zoom_in":
            self.zoom = self.zoom - 0.003
            print(self.zoom)
        if action == "zoom_out":
            self.zoom = self.zoom + 0.003
            print(self.zoom)
        self.mapgrid.fetch_map(config.MAP_FOCUS, self.zoom)
        self.add(self.mapgrid)
        self.mapgrid.rect[0] = 4
        self.mapgrid.rect[1] = 40