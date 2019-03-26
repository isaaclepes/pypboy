import pypboy
import pygame
import game
import config
from pypboy.modules.items import weapon


class Module(pypboy.SubModule):

	label = " Weapons "

	def __init__(self, *args, **kwargs):
		super(Module, self).__init__(*args, **kwargs)
		handlers = []
		item_names = []
		for i in config.INVENTORY:
			handlers.append(self.change_items)
			item_names.append(i.name)
		self.menu = pypboy.ui.Menu(200, config.INVENTORY, handlers, 3, 15)
		self.menu.rect[0] = 4
		self.menu.rect[1] = 60
		
		self.add(self.menu)
		
	def change_items(self):
		print "Changing"
		
		