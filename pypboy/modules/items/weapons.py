import pypboy
import pygame
import game
import config


class Module(pypboy.SubModule):

	label = " Weapons "

	def __init__(self, *args, **kwargs):
		super(Module, self).__init__(*args, **kwargs)
		handlers = []
		for i in config.INVENTORY:
			handlers.append(self.change_items)
		self.menu = pypboy.ui.Menu(200, config.INVENTORY, handlers, 0, 15)
		self.menu.rect[0] = 4
		self.menu.rect[1] = 60
		
		self.add(self.menu)
		
	def change_items(self):
		print "Changing"
		
class Weapon:
	
	def __init__(self, name, imageloc, damage, weight, value, condition, notes): 
		self.name = name
		self.imageloc = imageloc
		self.damage = damage
		self.weight= weight
		self.value = value
		self.condition = condition
		self.notes = notes
		