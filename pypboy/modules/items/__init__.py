from pypboy import BaseModule
from pypboy.modules.items import weapons
from pypboy.modules.items import apparel
from pypboy.modules.items import aid
from pypboy.modules.items import misc
from pypboy.modules.items import ammo
import config
import datetime


class Module(BaseModule):

	label = "ITEMS"
	GPIO_LED_ID = 29 #GPIO27 #21

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
		self.pypboy.header.title = " Wg 186/280  |  HP 160/175"
		self.active.handle_action("resume")

	def render(self, interval):
		new_date = datetime.datetime.now().strftime("%d.%m.%y.%H:%M:%S")
		if new_date != self.pypboy.header._date:
			self.pypboy.header.image.fill((0, 0, 0))
			pygame.draw.line(self.pypboy.header.image, (95, 255, 177), (5, 15), (5, 35), 2)
			pygame.draw.line(self.pypboy.header.image, (95, 255, 177), (5, 15), (config.WIDTH - 154, 15), 2)
			pygame.draw.line(self.pypboy.header.image, (95, 255, 177), (config.WIDTH - 154, 15), (config.WIDTH - 154, 35), 2)
			pygame.draw.line(self.pypboy.header.image, (95, 255, 177), (config.WIDTH - 148, 15), (config.WIDTH - 13, 15), 2)
			pygame.draw.line(self.pypboy.header.image, (95, 255, 177), (config.WIDTH - 13, 15), (config.WIDTH - 13, 35), 2)

			text = config.FONTS[14].render("  %s  " % self.pypboy.header.headline, True, (105, 251, 187), (0, 0, 0))
			self.pypboy.header.image.blit(text, (26, 8))
			text = config.FONTS[14].render("TEST", True, (95, 255, 177), (0, 0, 0))
			self.pypboy.header.image.blit(text, ((config.WIDTH - 154) - text.get_width() - 10, 19))
			text = config.FONTS[14].render(self.pypboy.header._date, True, (95, 255, 177), (0, 0, 0))
			self.pypboy.header.image.blit(text, ((config.WIDTH - 141), 19))
			self.pypboy.header._date = new_date