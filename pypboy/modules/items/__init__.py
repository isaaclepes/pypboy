from pypboy import BaseModule
from pypboy.modules.items import weapons
from pypboy.modules.items import apparel
from pypboy.modules.items import aid
from pypboy.modules.items import misc
from pypboy.modules.items import ammo
import pygame
import config
import datetime


class Module(BaseModule):

	label = "ITEMS"
	GPIO_LED_ID = 29 #GPIO27 #21
	HeaderGap = 13

	def __init__(self, *args, **kwargs):
		self.submodules = [
			weapons.Module(self),
			apparel.Module(self),
			aid.Module(self),
			misc.Module(self),
			ammo.Module(self)
		]
		super(Module, self).__init__(*args, **kwargs)
	
	def handle_resume(self):
		self.pypboy.header.headline = "ITEMS"
		self.pypboy.header.title = ["DR  20","HP 160/175"]
		self.active.handle_action("resume")
