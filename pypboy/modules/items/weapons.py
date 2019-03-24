import pypboy
import pygame
import game
import config


class Module(pypboy.SubModule):

	label = " Weapons "

	def __init__(self, *args, **kwargs):
		super(Module, self).__init__(*args, **kwargs)
		
	def handle_resume(self):
		self.parent.pypboy.header.headline = "ITEMS"
		self.parent.pypboy.header.title = " Wg 186/280  |  HP 160/175"
		super(Module, self).handle_resume()