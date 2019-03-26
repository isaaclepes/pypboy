import pypboy
import pygame
import game
import config

class Weapon():
	def __init__(self, name, imageloc, damage, weight, value, condition, notes): 
		self.name = name
		self.imageloc = imageloc
		self.image = pygame.image.load(self.imageloc)
		self.damage = damage
		self.weight= weight
		self.value = value
		self.condition = condition
		self.notes = notes

class Module(pypboy.SubModule):

	label = " Weapons "
	selected = 3
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
		self.menu = pypboy.ui.Menu(200, item_names, handlers, selected, 15)
		self.menu.rect[0] = 4
		self.menu.rect[1] = 60
		self.add(self.menu)
		#show weapon image
		weapon_to_display = self.INVENTORY[self.selected]
		weapon_to_display.rect = weapon_to_display.image.get_rect()
		weapon_to_display.image = weapon_to_display.image.convert()
		weapon_to_display.rect[0] = 200
		weapon_to_display.rect[1] = 40
		
	def change_items(self):
		print "Changing"
		
