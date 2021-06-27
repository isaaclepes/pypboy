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
        self.image = pygame.image.load('images/ref_stats.png').convert()
        #self.rect = self.image.get_rect()
        
        # Top Text
        config.FreeRobotoB[33].render_to(self.image, (104, 73), "STAT", (0, 255, 0))
        config.FreeRobotoB[33].render_to(self.image, (221, 73), "INV", (0, 255, 0))
        config.FreeRobotoB[33].render_to(self.image, (311, 73), "DATA", (0, 255, 0))
        config.FreeRobotoB[33].render_to(self.image, (422, 73), "MAP", (0, 255, 0))
        config.FreeRobotoB[33].render_to(self.image, (527, 73), "RADIO", (0, 255, 0))
        
        # Sub Text
        config.FreeRobotoR[30].render_to(self.image, (93, 118), "STATUS", (0, 255, 0))
        config.FreeRobotoR[30].render_to(self.image, (203, 118), "SPECIAL", (0, 128, 0))
        config.FreeRobotoR[30].render_to(self.image, (319, 118), "PERKS", (0, 128, 0))
        
        # Lines around the text
        pygame.draw.line(self.image, (0, 255, 0), (1, 105), (1, 112), 3)
        pygame.draw.line(self.image, (0, 255, 0), (0, 103), (95, 103), 3)
        pygame.draw.line(self.image, (0, 255, 0), (94, 80), (94, 101), 3)
        pygame.draw.line(self.image, (0, 255, 0), (93, 78), (101, 78), 3)
        pygame.draw.line(self.image, (0, 255, 0), (177, 78), (185, 78), 3)
        pygame.draw.line(self.image, (0, 255, 0), (184, 80), (184, 101), 3)
        pygame.draw.line(self.image, (0, 255, 0), (183, 103), (719, 103), 3)
        pygame.draw.line(self.image, (0, 255, 0), (717, 105), (719, 112), 3)
        
        # Limb Health Bars
        pygame.draw.line(self.image, (0, 255, 0), (344, 183), (379, 183), 9)
        pygame.draw.line(self.image, (0, 255, 0), (465, 284), (500, 285), 9)
        pygame.draw.line(self.image, (0, 255, 0), (465, 416), (500, 416), 9)
        pygame.draw.line(self.image, (0, 255, 0), (344, 462), (379, 462), 9)
        pygame.draw.line(self.image, (0, 255, 0), (216, 416), (251, 416), 9)
        pygame.draw.line(self.image, (0, 255, 0), (216, 284), (251, 284), 9)

        
        #text = config.RobotoB[18].render("ZapWizard", True, (105, 251, 20), (0, 0, 0))
        #text_width = text.get_size()[0]
        #self.image.blit(text, (config.WIDTH / 2 - 8 - text_width / 2, 20))
