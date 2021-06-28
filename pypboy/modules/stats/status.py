import pypboy
import pygame
import game
import config
import pypboy.ui


class Module(pypboy.SubModule):

    label = "Status"

    def __init__(self, *args, **kwargs):
        super(Module, self).__init__(*args, **kwargs)
        health = Health()
        health.rect[0] = 0
        health.rect[1] = config.header_height + 1
        self.add(health)
        self.menu = pypboy.ui.Menu(100, ["CND", "RAD", "EFF"], [self.show_cnd, self.show_rad, self.show_eff], 0)
        self.menu.rect[0] = 0
        self.menu.rect[1] = 0
        self.add(self.menu)


    def show_cnd(self):
        print("CND")

    def show_rad(self):
        print("RAD")

    def show_eff(self):
        print("EFF")


class Health(game.Entity):

    def __init__(self):
        super(Health, self).__init__()
        self.image = pygame.Surface((config.WIDTH, config.HEIGHT - config.header_height - config.footer_height))
        #self.image = pygame.image.load('images/stats/ref_stats.png').convert() #load for alignment reference

        
        # Top Text
        config.FreeRobotoB[33].render_to(self.image, (104, 0), "STAT", config.bright)
        config.FreeRobotoB[33].render_to(self.image, (221, 0), "INV", config.bright)
        config.FreeRobotoB[33].render_to(self.image, (311, 0), "DATA", config.bright)
        config.FreeRobotoB[33].render_to(self.image, (422, 0), "MAP", config.bright)
        config.FreeRobotoB[33].render_to(self.image, (527, 0), "RADIO", config.bright)
        
        # Sub Text
        config.FreeRobotoR[30].render_to(self.image, (93, 51), "STATUS", config.bright)
        config.FreeRobotoR[30].render_to(self.image, (203, 51), "SPECIAL", config.mid)
        config.FreeRobotoR[30].render_to(self.image, (319, 51), "PERKS", config.mid)
        
        # Lines around text
        pygame.draw.line(self.image, config.bright, (1, 32), (1, 39), 3)
        pygame.draw.line(self.image, config.bright, (0, 30), (92, 30), 3)
        pygame.draw.line(self.image, config.bright, (91, 7), (91, 28), 3)
        pygame.draw.line(self.image, config.bright, (90, 5), (101, 5), 3)
        pygame.draw.line(self.image, config.bright, (177, 5), (188, 5), 3)
        pygame.draw.line(self.image, config.bright, (187, 7), (187, 28), 3)
        pygame.draw.line(self.image, config.bright, (186, 30), (719, 30), 3)
        pygame.draw.line(self.image, config.bright, (718, 32), (718, 39), 3)
        
        # Health Bars
        pygame.draw.line(self.image, config.bright, (344, 112), (379, 112), 9)
        pygame.draw.line(self.image, config.bright, (465, 214), (500, 214), 9)
        pygame.draw.line(self.image, config.bright, (465, 346), (500, 346), 9)
        pygame.draw.line(self.image, config.bright, (344, 398), (379, 398), 9)
        pygame.draw.line(self.image, config.bright, (216, 346), (251, 346), 9)
        pygame.draw.line(self.image, config.bright, (216, 214), (251, 214), 9)
        
        # Middle Boxes
        pygame.draw.rect(self.image, config.mid, (203, 438, 64, 62)) #Gun box
        pygame.draw.rect(self.image, config.mid, (273, 438, 38, 62)) #Ammo box
        pygame.draw.rect(self.image, config.mid, (328, 438, 64, 62)) #Helmet box
        pygame.draw.rect(self.image, config.mid, (398, 438, 38, 62)) #Armor box
        pygame.draw.rect(self.image, config.mid, (440, 438, 38, 62)) #Energy box
        pygame.draw.rect(self.image, config.mid, (483, 438, 38, 62)) #Radiation box
        
        # Icons
        self.image.blit(pygame.image.load('images/stats/gun.png').convert_alpha(),(210,454))
        self.image.blit(pygame.image.load('images/stats/reticle.png').convert_alpha(),(284,443))
        self.image.blit(pygame.image.load('images/stats/helmet.png').convert_alpha(),(338,453))
        self.image.blit(pygame.image.load('images/stats/shield.png').convert_alpha(),(410,442))
        self.image.blit(pygame.image.load('images/stats/bolt.png').convert_alpha(),(453,442))
        self.image.blit(pygame.image.load('images/stats/radiation.png').convert_alpha(),(491,443))
        
        #Stat text
        config.FreeRobotoB[24].render_to(self.image, (281, 475), "18", config.bright) # Ammo count
        config.FreeRobotoB[24].render_to(self.image, (406, 475), "10", config.bright) # Armor count
        config.FreeRobotoB[24].render_to(self.image, (447, 475), "20", config.bright) # Energy count
        config.FreeRobotoB[24].render_to(self.image, (490, 475), "10", config.bright) # Rad count
        
        # Bottom Boxes
        pygame.draw.rect(self.image, config.dim, (0, 581, 166, 38)) #Hit point background
        pygame.draw.rect(self.image, config.dim, (170, 581, 370, 38)) #Level bar background
        pygame.draw.lines(self.image, config.mid,True,[(282,595),(529,595),(529,609),(282,609)], 3) #Level bar surround
        pygame.draw.rect(self.image, config.bright, (285, 597, 179, 11)) #Level bar fill
        pygame.draw.rect(self.image, config.dim, (544, 581, 176, 38)) #Actiion background
        
        # Bottom text
        config.FreeRobotoB[30].render_to(self.image, (7, 589), "HP 115/115", config.bright)
        config.FreeRobotoB[24].render_to(self.image, (188, 593), "LEVEL 66", config.bright)
        config.FreeRobotoB[30].render_to(self.image, (602, 589), "AP 90/90", config.bright)

        #User name
        config.FreeRobotoB[24].render_to(self.image, (301, 528), config.name, config.bright)
        
        # Vault Boy
        self.image.blit(pygame.image.load('images/stats/head_1.png').convert_alpha(),(328,139))
        self.image.blit(pygame.image.load('images/stats/body_1.png').convert_alpha(),(298,210))