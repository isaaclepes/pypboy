import pypboy
import pygame
import game
import settings


class Module(pypboy.SubModule):

    label = "WEAPONS"

    def __init__(self, *args, **kwargs):
        super(Module, self).__init__(*args, **kwargs)

        self.menu = pypboy.ui.Menu(settings.WEAPONS)
        self.menu.rect[0] = settings.menu_x
        self.menu.rect[1] = settings.menu_y
        
        self.add(self.menu)
