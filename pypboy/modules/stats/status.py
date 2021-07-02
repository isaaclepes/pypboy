import pypboy
import pygame
import game
import config
import pypboy.ui
import os


class Module(pypboy.SubModule):

    label = "STATUS"
    images = []

    def __init__(self, *args, **kwargs):
        super(Module, self).__init__(*args, **kwargs)
        health = Health()
        health.rect[0] = 0
        health.rect[1] = config.header_height + 1
        self.add(health)

        #self.menu = pypboy.ui.Menu(100, ["CND", "RAD", "EFF"], [self.show_cnd, self.show_rad, self.show_eff], 0)
        # self.menu.rect[0] = config.menu_x
        # self.menu.rect[1] = config.menu_y
        # self.add(self.menu)

    # def show_cnd(self):
        # print("CND")

    # def show_rad(self):
        # print("RAD")

    # def show_eff(self):
        # print("EFF")



class Health(game.Entity):

    def __init__(self):
        super(Health, self).__init__()
        self.image = pygame.Surface((config.WIDTH, config.HEIGHT - config.header_height - config.footer_height))
        self.image.fill((0, 0, 0))
        #self.animation = pygame.surface.Surface((128, 240))
        #self.animation.fill((0, 0, 0))
        #self.image.blit((self.animation),(297,138))

        self.clock = pygame.time.Clock()
        self.animation_time = 0.1
        self.current_time = 0
        self.steps = list(range(4)) + list(range(4, 0, -1))
        self.index = 0                
        self.images = []
        path = "./images/stats/legs1"
        for f in os.listdir(path):
            if f.endswith(".png"):
                image = pygame.image.load(path + "/" + f).convert_alpha()
                self.images.append(image)
        self.head = pygame.image.load("images/stats/head1/1.png").convert_alpha()
        
    def update(self):
        if self.current_time >= self.animation_time:
            self.current_time = 0
            if self.index >= len(self.images):
                self.index = 0
            self.file = self.images[self.index]
            self.image.fill((0,0,0))
            self.image.blit((self.file),(297 + self.steps[self.index] // 2,209 + self.steps[self.index]))
            self.image.blit((self.head),(325 + self.steps[self.index] // 2,141 + self.steps[self.index]))
            self.index += 1
           
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

    def render(self, clock):
        self.current_time += self.clock.tick(30)
