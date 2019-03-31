import pypboy
import pygame
import game
import config

class Module(pypboy.SubModule):

	label = " Weapons "

	def __init__(self, *args, **kwargs):
		super(Module, self).__init__((config.WIDTH, config.HEIGHT), *args, **kwargs)
		handlers = []
		item_names = []
		INVENTORY = [
			Weapon('Chinese Assault Rifle','images/inventory/flamer.png',0,0,0,0,''),
			Weapon('Combat Shotgun','images/inventory/flamer.png',0,0,0,0,''),
			Weapon('Deathclaw Gauntlet','images/inventory/flamer.png',0,0,0,0,''),
			Weapon('Flamer','images/inventory/flamer.png',20,10,250,100,''),
			Weapon('Hunting Rifle','images/inventory/flamer.png',0,0,0,0,''),
			Weapon('Minigun','images/inventory/flamer.png',0,0,0,0,''),
			Weapon('Missile Launcher','images/inventory/flamer.png',0,0,0,0,''),
			Weapon('Pulse Grenade (2)','images/inventory/flamer.png',0,0,0,0,'')
		]
		selected = 3
		for i in INVENTORY:
			handlers.append(self.change_items)
			item_names.append(i.name)
		self.menu = pypboy.ui.Menu(200, item_names, handlers, selected, 15)
		self.menu.rect[0] = 4
		self.menu.rect[1] = 60
		self.add(self.menu)
		#show weapon image
		weapon_to_display = INVENTORY[selected]
		#weapon_to_display.rect = weapon_to_display.image.get_rect()
		weapon_to_display.image = weapon_to_display.image.convert()
		weapon_to_display.rect[0] = 200
		weapon_to_display.rect[1] = 40	
		weapon_to_display.rect[2] = 280	
		weapon_to_display.rect[3] = 280	
		
		print "RECTANGLE %s %s %s %s" % (weapon_to_display.rect[0],weapon_to_display.rect[1],weapon_to_display.rect[2],weapon_to_display.rect[3])
		
		#Show Weapon stats - Value
		#text = config.FONTS[14].render("%s" %(weapon_to_display.value), True, (95, 255, 177), (0, 0, 0))
		#pygame.draw.line(weapon_to_display.image, (95, 255, 177), (config.WIDTH - 13, weapon_to_display.rect[1] + weapon_to_display.image.get_rect()[3] + 5 ), (config.WIDTH - 13, weapon_to_display.rect[1] + weapon_to_display.image.get_rect()[3] + 25), 2)	#End of title Verticle bar
		#weapon_to_display.image.blit(text, (config.WIDTH - (text.get_width() + 5), weapon_to_display.rect[1] + weapon_to_display.image.get_rect()[3] + 9))
		#pygame.draw.line(weapon_to_display.image, (95, 255, 177), (config.WIDTH - 50, 15), (config.WIDTH - 13, weapon_to_display.rect[1] + weapon_to_display.image.get_rect()[3] + 5 ), 2) # Horizontal Bar
		
		#pygame.draw.line(weapon_to_display.image, (95, 255, 177), (config.WIDTH - 13, 200 ), (config.WIDTH - 13, 215), 2)	#End of title Verticle bar
		#weapon_to_display.image.blit(text, (config.WIDTH - (text.get_width() + 5), weapon_to_display.rect[1] + weapon_to_display.image.get_rect()[3] + 9))
		#pygame.draw.line(weapon_to_display.image, (95, 255, 177), (config.WIDTH - 50, 15), (config.WIDTH - 13, weapon_to_display.rect[1] + weapon_to_display.image.get_rect()[3] + 5 ), 2) # Horizontal Bar
		
		#Test starts here
		#Value
		pygame.draw.line(weapon_to_display.image, (95, 255, 177), (weapon_to_display.rect[2] - 13 - 0, 160), (weapon_to_display.rect[2] - 13 - 0, 180), 2)#Verticle Bar
		text = config.FONTS[14].render("25", True, (95, 255, 177), (0, 0, 0))
		#weapon_to_display.image.blit(text, (10, 204-weapon_to_display.rect[1]))
		weapon_to_display.image.blit(text, (config.WIDTH - weapon_to_display.rect[0] - 13 - 0 - (text.get_width() + 5), 204-weapon_to_display.rect[1]))
		text = config.FONTS[14].render("VAL", True, (95, 255, 177), (0, 0, 0))
		weapon_to_display.image.blit(text, (config.WIDTH - weapon_to_display.rect[0] - 13 - 0 - 85 + 2, 204-weapon_to_display.rect[1]))
		pygame.draw.line(weapon_to_display.image, (95, 255, 177), (config.WIDTH - weapon_to_display.rect[0] - 13 - 85, 200-weapon_to_display.rect[1]), (config.WIDTH - weapon_to_display.rect[0] - 13, 200-weapon_to_display.rect[1]), 2) # Horizontal Bar
		
		
		
		pygame.draw.line(weapon_to_display.image, (95, 255, 177), (config.WIDTH - weapon_to_display.rect[0] - 13 - 95, 200-weapon_to_display.rect[1]), (config.WIDTH - weapon_to_display.rect[0] - 13 - 95, 220-weapon_to_display.rect[1]), 2)#Verticle Bar
		text = config.FONTS[14].render("10", True, (95, 255, 177), (0, 0, 0))
		weapon_to_display.image.blit(text, (config.WIDTH - weapon_to_display.rect[0] - 13 - 95 - (text.get_width() + 5), 204-weapon_to_display.rect[1]))
		text = config.FONTS[14].render("WG", True, (95, 255, 177), (0, 0, 0))
		weapon_to_display.image.blit(text, (config.WIDTH - 13  - 95 - 85 + 2, 204-weapon_to_display.rect[1]))
		pygame.draw.line(weapon_to_display.image, (95, 255, 177), (config.WIDTH - weapon_to_display.rect[0] - 13 - 95 - 85, 200-weapon_to_display.rect[1]), (config.WIDTH - weapon_to_display.rect[0] - 13 - 95, 200-weapon_to_display.rect[1]), 2) # Horizontal Bar
		
		pygame.draw.line(weapon_to_display.image, (95, 255, 177), (config.WIDTH - weapon_to_display.rect[0] - 13 - 190, 200-weapon_to_display.rect[1]), (config.WIDTH - weapon_to_display.rect[0] - 13 - 190, 220-weapon_to_display.rect[1]), 2)#Verticle Bar
		text = config.FONTS[14].render("20", True, (95, 255, 177), (0, 0, 0))
		weapon_to_display.image.blit(text, (config.WIDTH - weapon_to_display.rect[0] - 13 - 190 - (text.get_width() + 5), 204-weapon_to_display.rect[1]))
		text = config.FONTS[14].render("DAM", True, (95, 255, 177), (0, 0, 0))
		weapon_to_display.image.blit(text, (config.WIDTH - weapon_to_display.rect[0] - 13  - 190 - 85 + 2, 204-weapon_to_display.rect[1]))
		pygame.draw.line(weapon_to_display.image, (95, 255, 177), (config.WIDTH - weapon_to_display.rect[0] - 13 - 190 - 85, 200-weapon_to_display.rect[1]), (config.WIDTH - weapon_to_display.rect[0] - 13 - 190, 200-weapon_to_display.rect[1]), 2) # Horizontal Bar
				
		#Row 2
#		pygame.draw.line(weapon_to_display.image, (95, 255, 177), (config.WIDTH - weapon_to_display.rect[0] - 13 - 0, 230-weapon_to_display.rect[1]), (config.WIDTH - weapon_to_display.rect[0] - 13 - 0, 250-weapon_to_display.rect[1]), 2)
#		text = config.FONTS[14].render("-- --", True, (95, 255, 177), (0, 0, 0))
#		weapon_to_display.image.blit(text, (config.WIDTH - weapon_to_display.rect[0] - 13 - 95 - 85 + 2, 234-weapon_to_display.rect[1]))
#		pygame.draw.line(weapon_to_display.image, (95, 255, 177), (config.WIDTH - weapon_to_display.rect[0] - 13 - 95 - 85, 230-weapon_to_display.rect[1]), (config.WIDTH - weapon_to_display.rect[0] - 13, 230-weapon_to_display.rect[1]), 2) # Horizontal Bar
#		
#		pygame.draw.line(weapon_to_display.image, (95, 255, 177), (config.WIDTH - weapon_to_display.rect[0] - 13 - 190, 230-weapon_to_display.rect[1]), (config.WIDTH - weapon_to_display.rect[0] - 13 - 190, 250-weapon_to_display.rect[1]), 2)#Verticle Bar
#		#text = config.FONTS[14].render("100", True, (95, 255, 177), (0, 0, 0))
#		#weapon_to_display.image.blit(text, (config.WIDTH - 13 - 190 - (text.get_width() + 5), 234))
#		cndlength = 50
#		pygame.draw.rect(weapon_to_display.image, (95, 255, 177), (config.WIDTH - weapon_to_display.rect[0] - 13 - 190 - 55,237-weapon_to_display.rect[1],40,12)) #Condition bar
#		pygame.draw.rect(weapon_to_display.image, (0, 70, 0), (config.WIDTH - weapon_to_display.rect[0] - 13 - 190 - 55 + 40,237-weapon_to_display.rect[1],10,12))#Filler bar
#		text = config.FONTS[14].render("CND", True, (95, 255, 177), (0, 0, 0))
#		weapon_to_display.image.blit(text, (config.WIDTH - weapon_to_display.rect[0] - 13  - 190 - 85 + 2, 234-weapon_to_display.rect[1]))
#		pygame.draw.line(weapon_to_display.image, (95, 255, 177), (config.WIDTH - weapon_to_display.rect[0] - 13 - 190 - 85, 230-weapon_to_display.rect[1]), (config.WIDTH - weapon_to_display.rect[0] - 13 - 190, 230-weapon_to_display.rect[1]), 2) # Horizontal Bar
		#Test ends here
		
		self.add(weapon_to_display)	

		
	def change_items(self):
		print "Changing"
		
class Weapon(game.Entity):
	def __init__(self, name, imageloc, damage, weight, value, condition, notes): 
		super(Weapon, self).__init__((config.WIDTH, config.HEIGHT))
		self.name = name
		self.imageloc = imageloc
		self.image = pygame.image.load(self.imageloc)
		self.damage = damage
		self.weight= weight
		self.value = value
		self.condition = condition
		self.notes = notes
		self.rect[0] = 200
		self.rect[1] = 40	
		self.rect[2] = 280	
		self.rect[3] = 280	