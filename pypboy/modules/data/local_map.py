import pygame
import pypboy
import config

from pypboy.modules.data import entities


class Module(pypboy.SubModule):
	label = "Local Map"
	load_cached_map = False

	def __init__(self, *args, **kwargs):
		super(Module, self).__init__(*args, **kwargs)
		#mapgrid = entities.MapGrid((-5.9302032, 54.5966701), (config.WIDTH - 8, config.HEIGHT - 80))
		mapgrid = entities.Map(config.WIDTH, pygame.Rect(4, (config.WIDTH - config.HEIGHT) / 2, config.WIDTH - 8, config.HEIGHT - 80))
		if(config.LOAD_CACHED_MAP):
			print "Loading cached map"
			try:
				f = open("map.cache")
				map_data = f.readlines();
				f.close()
				mapgrid.display_map(map_data)
			except:
				print "ERROR reading cached map file"
				quit()
		else:
			print "Loading map from the internet"
			mapgrid.fetch_map(config.MAP_FOCUS, 0.003)
		self.add(mapgrid)
		mapgrid.rect[0] = 4
		mapgrid.rect[1] = 40

	def handle_resume(self):
		self.parent.pypboy.header.headline = "DATA"
		self.parent.pypboy.header.title = "City Centre"
		super(Module, self).handle_resume()