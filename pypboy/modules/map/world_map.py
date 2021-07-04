import pygame
import pypboy
import settings

from pypboy.modules.data import entities


class Module(pypboy.SubModule):
    label = "WORLD MAP"
    title = "Jefferson City"
    map_top_edge = 128

    def __init__(self, *args, **kwargs):
        super(Module, self).__init__(*args, **kwargs)
        if settings.LOAD_CACHED_MAP:
            mapgrid = entities.Map(480, pygame.Rect(0, 0, settings.WIDTH - 8, settings.HEIGHT - self.map_top_edge), "Loading cached map")
            mapgrid.load_map(settings.MAP_FOCUS, settings.WORLD_MAP_FOCUS, True)
        else:
            mapgrid = entities.Map(480, pygame.Rect(0, 0, settings.WIDTH - 8, settings.HEIGHT - self.map_top_edge), "Fetching cached map")
            mapgrid.fetch_map(settings.MAP_FOCUS, settings.WORLD_MAP_FOCUS, True)
        self.add(mapgrid)
        mapgrid.rect[0] = 4
        mapgrid.rect[1] = 40

    def handle_resume(self):
        #self.parent.pypboy.topmenu.headline = "DATA"
        #self.parent.pypboy.topmenu.title = [self.title]
        super(Module, self).handle_resume()