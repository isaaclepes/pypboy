import pypboy
import pygame
import game
import config


class Module(pypboy.SubModule):

    label = " Apparel "

    def __init__(self, *args, **kwargs):
        super(Module, self).__init__((config.WIDTH, config.HEIGHT), *args, **kwargs)
        handlers = []
        item_names = []
        INVENTORY = [
            Apparel('NCR Ranger combat armor','images/inventory/desertarmor.png',20,30,7500,0,''),
            Apparel('Ranger helmet','images/inventory/rangerhelment.png',4,3,999,100,''),
            Apparel('Pulse Grenade (2)','images/inventory/flamer.png',0,0,0,0,'')
        ]
        selected = 0
        for i in INVENTORY:
            handlers.append(self.change_items)
            item_names.append(i.name)
        self.menu = pypboy.ui.Menu(200, item_names, handlers, selected, 15)
        self.menu.rect[0] = 4
        self.menu.rect[1] = 60
        self.add(self.menu)
        #show weapon image
        apparel_to_display = INVENTORY[selected]
        apparel_to_display.rect = apparel_to_display.image.get_rect()
        apparel_to_display.image = apparel_to_display.image.convert()
        apparel_to_display.rect[0] = 189
        apparel_to_display.rect[1] = 40
        
        print("RECTANGLE %s %s %s %s" % (apparel_to_display.rect[0],apparel_to_display.rect[1],apparel_to_display.rect[2],apparel_to_display.rect[3]))
        
        #Show Weapon stats - Value
        #text = config.FONTS[14].render("%s" %(apparel_to_display.value), True, (95, 255, 177), (0, 0, 0))
        #pygame.draw.line(apparel_to_display.image, (95, 255, 177), (config.WIDTH - 13, apparel_to_display.rect[1] + apparel_to_display.image.get_rect()[3] + 5 ), (config.WIDTH - 13, apparel_to_display.rect[1] + apparel_to_display.image.get_rect()[3] + 25), 2)	#End of title Verticle bar
        #apparel_to_display.image.blit(text, (config.WIDTH - (text.get_width() + 5), apparel_to_display.rect[1] + apparel_to_display.image.get_rect()[3] + 9))
        #pygame.draw.line(apparel_to_display.image, (95, 255, 177), (config.WIDTH - 50, 15), (config.WIDTH - 13, apparel_to_display.rect[1] + apparel_to_display.image.get_rect()[3] + 5 ), 2) # Horizontal Bar
        
        #pygame.draw.line(apparel_to_display.image, (95, 255, 177), (config.WIDTH - 13, 200 ), (config.WIDTH - 13, 215), 2)	#End of title Verticle bar
        #apparel_to_display.image.blit(text, (config.WIDTH - (text.get_width() + 5), apparel_to_display.rect[1] + apparel_to_display.image.get_rect()[3] + 9))
        #pygame.draw.line(apparel_to_display.image, (95, 255, 177), (config.WIDTH - 50, 15), (config.WIDTH - 13, apparel_to_display.rect[1] + apparel_to_display.image.get_rect()[3] + 5 ), 2) # Horizontal Bar
        
        #Test starts here
        #Value
        pygame.draw.line(apparel_to_display.image, (95, 255, 177), (apparel_to_display.rect[2] - 2, 200-apparel_to_display.rect[1]), (apparel_to_display.rect[2] -2, 220-apparel_to_display.rect[1]), 2)#Verticle Bar
        pygame.draw.line(apparel_to_display.image, (95, 255, 177), (apparel_to_display.rect[2] - 85, 200-apparel_to_display.rect[1]), (apparel_to_display.rect[2], 200-apparel_to_display.rect[1]), 2) # Horizontal Bar
        text = config.FONTS[14].render("25", True, (95, 255, 177), (0, 0, 0))
        apparel_to_display.image.blit(text, (apparel_to_display.rect[2] - 0 - (text.get_width() + 5), 204-apparel_to_display.rect[1]))
        text = config.FONTS[14].render("VAL", True, (95, 255, 177), (0, 0, 0))
        apparel_to_display.image.blit(text, (apparel_to_display.rect[2] - 0 - 85 + 2, 204-apparel_to_display.rect[1]))
        
        
        
        #Weight
        pygame.draw.line(apparel_to_display.image, (95, 255, 177), (apparel_to_display.rect[2] - 95, 200-apparel_to_display.rect[1]), (apparel_to_display.rect[2] - 95, 220-apparel_to_display.rect[1]), 2)#Verticle Bar
        pygame.draw.line(apparel_to_display.image, (95, 255, 177), (apparel_to_display.rect[2] - 95 - 85, 200-apparel_to_display.rect[1]), (apparel_to_display.rect[2] - 95, 200-apparel_to_display.rect[1]), 2) # Horizontal Bar
        text = config.FONTS[14].render("4", True, (95, 255, 177), (0, 0, 0))
        apparel_to_display.image.blit(text, (apparel_to_display.rect[2] - 95 - (text.get_width() + 5), 204-apparel_to_display.rect[1]))
        text = config.FONTS[14].render("WG", True, (95, 255, 177), (0, 0, 0))
        apparel_to_display.image.blit(text, (apparel_to_display.rect[2]  - 95 - 85 + 2, 204-apparel_to_display.rect[1]))
        
        
        
        
        #Armor
        pygame.draw.line(apparel_to_display.image, (95, 255, 177), (apparel_to_display.rect[2] - 190, apparel_to_display.rect[3] - 80 - apparel_to_display.rect[1]), (apparel_to_display.rect[2] - 190, apparel_to_display.rect[3] - 60 - apparel_to_display.rect[1]), 2)#Verticle Bar
        pygame.draw.line(apparel_to_display.image, (95, 255, 177), (apparel_to_display.rect[2] - 190 - 85, 200-apparel_to_display.rect[1]), (apparel_to_display.rect[2] - 190, 200-apparel_to_display.rect[1]), 2) # Horizontal Bar
        text = config.FONTS[14].render("%s" %(apparel_to_display.armor), True, (95, 255, 177), (0, 0, 0))
        apparel_to_display.image.blit(text, (apparel_to_display.rect[2] - 190 - (text.get_width() + 5), 204-apparel_to_display.rect[1]))
        text = config.FONTS[14].render("DT", True, (95, 255, 177), (0, 0, 0))
        apparel_to_display.image.blit(text, (apparel_to_display.rect[2]  - 190 - 85 + 2, 204-apparel_to_display.rect[1]))
        
                
        #Row 2
        pygame.draw.line(apparel_to_display.image, (95, 255, 177), (apparel_to_display.rect[2] - 2, 230-apparel_to_display.rect[1]), (apparel_to_display.rect[2] - 2, 250-apparel_to_display.rect[1]), 2)
        text = config.FONTS[14].render("-- --", True, (95, 255, 177), (0, 0, 0))
        apparel_to_display.image.blit(text, (apparel_to_display.rect[2] - 95 - 85 + 2, 234-apparel_to_display.rect[1]))
        pygame.draw.line(apparel_to_display.image, (95, 255, 177), (apparel_to_display.rect[2] - 95 - 85, 230-apparel_to_display.rect[1]), (apparel_to_display.rect[2], 230-apparel_to_display.rect[1]), 2) # Horizontal Bar
        
        #Condition
        pygame.draw.line(apparel_to_display.image, (95, 255, 177), (apparel_to_display.rect[2] - 190, 230-apparel_to_display.rect[1]), (apparel_to_display.rect[2] - 190, 250-apparel_to_display.rect[1]), 2)#Verticle Bar
        pygame.draw.line(apparel_to_display.image, (95, 255, 177), (apparel_to_display.rect[2] - 190 - 85, 230-apparel_to_display.rect[1]), (apparel_to_display.rect[2] - 190, 230-apparel_to_display.rect[1]), 2) # Horizontal Bar
        cndlength = 50
        pygame.draw.rect(apparel_to_display.image, (95, 255, 177), (apparel_to_display.rect[2] - 190 - 55,237-apparel_to_display.rect[1],40,12)) #Condition bar
        pygame.draw.rect(apparel_to_display.image, (0, 70, 0), (apparel_to_display.rect[2] - 190 - 55 + 40,237-apparel_to_display.rect[1],10,12))#Filler bar
        text = config.FONTS[14].render("CND", True, (95, 255, 177), (0, 0, 0))
        apparel_to_display.image.blit(text, (apparel_to_display.rect[2]  - 190 - 85 + 2, 234-apparel_to_display.rect[1]))
        
        #Test ends here
        
        self.add(apparel_to_display)	

        
    def change_items(self):
        print("Changing")
        
class Apparel (game.Entity):
    def __init__(self, name, imageloc, armor , weight, value, condition, notes): 
        super(Apparel, self).__init__((config.WIDTH, config.HEIGHT))
        self.name = name
        self.imageloc = imageloc
        self.image = pygame.image.load(self.imageloc)
        self.armor = armor
        self.weight= weight
        self.value = value
        self.condition = condition
        self.notes = notes
