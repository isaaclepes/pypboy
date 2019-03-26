import pypboy
import pygame
import game
import config

class Weapon():
	def __init__(self, name, imageloc, damage, weight, value, condition, notes): 
		self.name = name
		self.imageloc = imageloc
		self.damage = damage
		self.weight= weight
		self.value = value
		self.condition = condition
		self.notes = notes

class Module(pypboy.SubModule):

	label = " Weapons "
	
	INVENTORY = [
		Weapon('Chinese Assault Rifle','images/inventory/flamer.png',0,0,0,0,''),
		Weapon('Combat Shotgun','images/inventory/flamer.png',0,0,0,0,''),
		Weapon('Deathclaw Gauntlet','images/inventory/flamer.png',0,0,0,0,''),
		Weapon('Flamer','images/inventory/flamer.png',0,0,0,0,''),
		Weapon('Hunting Rifle','images/inventory/flamer.png',0,0,0,0,''),
		Weapon('Minigun','images/inventory/flamer.png',0,0,0,0,''),
		Weapon('Missile Launcher','images/inventory/flamer.png',0,0,0,0,''),
		Weapon('Pulse Grenade (2)','images/inventory/flamer.png',0,0,0,0,'')
	]

	def __init__(self, *args, **kwargs):
		super(Module, self).__init__(*args, **kwargs)
		handlers = []
		item_names = []
		for i in self.INVENTORY:
		print "%s" % (i.name)
			handlers.append(self.change_items)
			item_names.append(i.name)
		self.menu = pypboy.ui.Menu(200, self.INVENTORY, handlers, 3, 15)
		self.menu.rect[0] = 4
		self.menu.rect[1] = 60
		
		self.add(self.menu)
		
	def change_items(self):
		print "Changing"
		
