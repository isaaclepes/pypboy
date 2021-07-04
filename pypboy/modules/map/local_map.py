import pygame
import pypboy
import settings

from pypboy.modules.data import entities

class Module(pypboy.SubModule):
    label = "LOCAL MAP"
    title = "Cosplacon"
    zoom = 0.003
    map_top_edge = 128

    def __init__(self, *args, **kwargs):
        super(Module, self).__init__(*args, **kwargs)
        self.mapgrid = entities.Map(settings.WIDTH, pygame.Rect(0, (settings.WIDTH - settings.HEIGHT) / 2, settings.WIDTH - 8, settings.HEIGHT - self.map_top_edge))
        if(settings.LOAD_CACHED_MAP):
            print("Loading cached map")
            self.mapgrid = entities.Map(settings.WIDTH, pygame.Rect(0, (settings.WIDTH - settings.HEIGHT) / 2, settings.WIDTH - 8, settings.HEIGHT - self.map_top_edge), "Loading cached map")
            self.mapgrid.load_map(settings.MAP_FOCUS, self.zoom, False)
        else:
            print("Loading map from the internet")
            self.mapgrid = entities.Map(settings.WIDTH, pygame.Rect(0, (settings.WIDTH - settings.HEIGHT) / 2, settings.WIDTH - 8, settings.HEIGHT - self.map_top_edge), "Loading map from the internet")
            self.mapgrid.fetch_map(settings.MAP_FOCUS, self.zoom, False)
        self.add(self.mapgrid)
        self.mapgrid.rect[0] = 0
        self.mapgrid.rect[1] = self.map_top_edge
    
    def handle_action(self, action, value=0):
        if action == "zoom_in":
            self.zoomMap(-0.003)
        if action == "zoom_out":
            self.zoomMap(0.003)

    def handle_resume(self):
        #self.parent.pypboy.topmenu.headline = "DATA"
        #self.parent.pypboy.topmenu.title = [self.title]
        super(Module, self).handle_resume()

    # def handle_tap(self):
        # x,y = pygame.mouse.get_pos()
        # if x < (settings.WIDTH / 2):
            # self.zoomMap(-0.003)
        # if x > (settings.WIDTH / 2):
            # self.zoomMap(0.003)

    def zoomMap(self, zoomFactor):
        self.zoom = self.zoom + zoomFactor
        if settings.LOAD_CACHED_MAP:
            print("Loading cached map")
            self.mapgrid.load_map(settings.MAP_FOCUS, self.zoom, False)
        else:
            print("Loading map from the internet")
            self.mapgrid.fetch_map(settings.MAP_FOCUS, self.zoom, False)
        
        self.add(self.mapgrid)
        self.mapgrid.rect[0] = 0
        self.mapgrid.rect[1] = self.map_top_edge
        #self.parent.pypboy.topmenu.headline = "DATA"
        #self.parent.pypboy.topmenu.title = [self.title]
    