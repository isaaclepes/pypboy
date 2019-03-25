import pypboy
import pygame
import game
import config


class Module(pypboy.SubModule):

	label = " Weapons "

	def __init__(self, *args, **kwargs):
		super(Module, self).__init__(*args, **kwargs)
		self.menu = pypboy.ui.Menu(100, config.INVENTORY, self.change_items, 0)
		self.menu.rect[0] = 4
		self.menu.rect[1] = 60
		self.add(self.menu)
		
	def change_items(self):
		print "Changing"