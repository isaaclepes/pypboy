import pypboy
import pygame
import game
import settings
import pypboy.ui
import os


class Module(pypboy.SubModule):

    label = ""
    images = []

    def __init__(self, *args, **kwargs):
        super(Module, self).__init__(*args, **kwargs)
        thumbs = Thumbs()
        thumbs.rect[0] = 0
        thumbs.rect[1] = 51
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
        self.image = pygame.Surface((settings.WIDTH, settings.HEIGHT))
        self.image.fill((0, 0, 0))

        self.clock = pygame.time.Clock()
        self.animation_time = 0.1
        self.current_time = 0
        self.index = 0                
        self.images = []
        self.frameorder = [0,0,0,0,0,0,0,0,0,0,0,0,1,2,0,0,0,0,0,0,0,0,3,4,5,6,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7]

        self.brightness = list(range(0, 150, 15)) + list(range(150, 0, -15))
        self.brightness_index = 0
        path = "./images/boot"
        for f in os.listdir(path):
            if f.endswith(".png"):
                image = pygame.image.load(path + "/" + f).convert_alpha()
                self.images.append(image)
       
    def update(self):
        if self.current_time >= self.animation_time:
            self.current_time = 0
            if self.index >= len(self.frameorder):
                self.index = 0
            self.image.fill((0,0,0))
            self.next = self.frameorder[self.index]
            self.file = self.images[self.next]
            self.image.blit((self.file),(250,150))
            self.index += 1
            self.brightness_index += 1
            if self.brightness_index >= len(self.brightness):
                self.brightness_index = 0
            self.color = (0, self.brightness[self.brightness_index], 0)

            text = settings.FreeRobotoB[20].render_to(self.image, (300, 450), "INITITATING...", self.color)

        #User name
        

    def render(self, clock):
        self.current_time += self.clock.tick(30)
