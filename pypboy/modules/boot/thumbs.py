import pypboy
import pygame
import game
import settings
import pypboy.ui
import os
import time

class Module(pypboy.SubModule):

    label = "hidden"
    images = []

    def __init__(self, *args, **kwargs):
        super(Module, self).__init__(*args, **kwargs)
        thumbs = Thumbs()
        thumbs.rect[0] = 260
        thumbs.rect[1] = 210
        self.add(thumbs)

        #self.menu = pypboy.ui.Menu([["CND", "RAD", "EFF"], [self.show_cnd, self.show_rad, self.show_eff]], 0)
        # self.menu.rect[0] = settings.menu_x
        # self.menu.rect[1] = settings.menu_y
        # self.add(self.menu)

    # def show_cnd(self):
        # print("CND")

    # def show_rad(self):
        # print("RAD")

    # def show_eff(self):
        # print("EFF")

class Thumbs(game.Entity):

    def __init__(self):
        super(Thumbs, self).__init__()

        self.image = pygame.Surface((180, 300))
        self.image.fill((0, 0, 0))

        self.clock = pygame.time.Clock()
        self.animation_time = 0.125
        self.current_time = 0
        self.index = 0                
        self.images = []
        self.prev_time = 0
        # self.prev_fps_time = 0
        self.frameorder = [0,0,0,0,0,0,0,0,0,0,0,1,2,0,0,0,0,0,0,0,0,3,4,5,6,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7]

        self.brightness = list(range(0, 150, 15)) + list(range(150, 0, -15))
        self.brightness_index = 0
        path = "./images/boot"
        for filename in sorted(os.listdir(path)):
            if filename.endswith(".png"):
                self.images.append(pygame.image.load(path + "/" + filename).convert_alpha())
                      
    def render(self):
        
        self.current_time = time.time()
        self.delta_time = self.current_time - self.prev_time

        #FPS debugging
        # self.fps_delta_time = self.current_time - self.prev_fps_time
        # if self.fps_delta_time:
        #     self.fps = round(1/self.fps_delta_time,1)
        # self.prev_fps_time = time.time()
        
        if self.delta_time >= self.animation_time:
            self.prev_time = time.time()

            if self.index >= len(self.frameorder): #Loop the animation
                self.index = 0
                settings.glitch = True
                pygame.event.post(pygame.event.Event(pygame.KEYDOWN,key=pygame.K_F1))

            self.image.fill((0,0,0))
            self.image.blit((self.images[self.frameorder[self.index]]),(0,0))
            
            self.index += 1
            
            self.brightness_index += 1
            if self.brightness_index >= len(self.brightness):
                self.brightness_index = 0
            self.color = (0, self.brightness[self.brightness_index], 0)
            
            #settings.FreeRobotoB[24].render_to(self.image, (0, 0), str(self.fps), settings.bright) #FPS
            #settings.FreeRobotoB[24].render_to(self.image, (0, 50), str(round(1/self.delta_time,1)), settings.bright) #FPS
            #settings.FreeRobotoB[24].render_to(self.image, (0, 190), str(self.index), settings.bright) #FPS

            settings.FreeRobotoB[29].render_to(self.image, (10, 270), "INITITATING...", self.color)