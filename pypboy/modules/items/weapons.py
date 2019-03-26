import pypboy
import pygame
import game
import config
from pypboy.modules.items import weapon


class Module(pypboy.SubModule):

	label = " Weapons "
	
	INVENTORY = [
pypboy.modules.items.weapon("Chinese Assault Rifle",'images/inventory/flamer.png',0,0,0,0,''),
pypboy.modules.items.weapon("Combat Shotgun",'images/inventory/flamer.png',0,0,0,0,''),
pypboy.modules.items.weapon("Deathclaw Gauntlet",'images/inventory/flamer.png',0,0,0,0,''),
pypboy.modules.items.weapon("Flamer",'images/inventory/flamer.png',0,0,0,0,''),
pypboy.modules.items.weapon("Hunting Rifle",'images/inventory/flamer.png',0,0,0,0,''),
pypboy.modules.items.weapon("Minigun",'images/inventory/flamer.png',0,0,0,0,''),
pypboy.modules.items.weapon("Missile Launcher",'images/inventory/flamer.png',0,0,0,0,''),
pypboy.modules.items.weapon("Pulse Grenade (2)",'images/inventory/flamer.png',0,0,0,0,'')
]

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
		
		