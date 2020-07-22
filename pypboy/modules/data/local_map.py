import pygame
import pypboy
import config

from pypboy.modules.data import entities

class Module(pypboy.SubModule):
    label = "Local Map"
    load_cached_map = False
    zoom = 0.003
    mapgrid = ''

    def __init__(self, *args, **kwargs):
        super(Module, self).__init__(*args, **kwargs)
        zoom = 0.003
        #mapgrid = entities.MapGrid((-5.9302032, 54.5966701), (config.WIDTH - 8, config.HEIGHT - 80))
        mapgrid = entities.Map(config.WIDTH, pygame.Rect(4, (config.WIDTH - config.HEIGHT) / 2, config.WIDTH - 8, config.HEIGHT - 80))
        if(config.LOAD_CACHED_MAP):
            print("Loading cached map")
            #mapgrid = entities.Map(config.WIDTH, pygame.Rect(4, (config.WIDTH - config.HEIGHT) / 2, config.WIDTH - 8, config.HEIGHT - 80), "Loading cached map")
            map_data_location = 'map.cache'
            mapgrid.load_map(config.MAP_FOCUS, 0.003)
        else:
            print("Loading map from the internet")
            #mapgrid = entities.Map(config.WIDTH, pygame.Rect(4, (config.WIDTH - config.HEIGHT) / 2, config.WIDTH - 8, config.HEIGHT - 80), "Loading map from the internet")
            mapgrid.fetch_map(config.MAP_FOCUS, 0.003)
        self.add(mapgrid)
        mapgrid.rect[0] = 4
        mapgrid.rect[1] = 40
    
    # def handle_action(self, action):
    #     zoom = 0.003
    #     mapgrid = entities.Map(config.WIDTH, pygame.Rect(4, (config.WIDTH - config.HEIGHT) / 2, config.WIDTH - 8, config.HEIGHT - 80))
    #     if action == "zoom_in":
    #         zoom = zoom - 0.003
    #     if action == "zoom_out":
    #         zoom = zoom + 0.003
    #     mapgrid.load_map(config.MAP_FOCUS, zoom)