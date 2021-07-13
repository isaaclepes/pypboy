import pypboy
import pygame
import game
import settings
import pypboy.ui
import pypboy.core
import time
import pypboy.modules.stats.status


class Module(pypboy.SubModule):

    label = "hidden"

    def __init__(self, *args, **kwargs):
        super(Module, self).__init__(*args, **kwargs)
        settings.glitch = True
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN,key=pygame.K_F1))
        
    def handle_resume(self):
        settings.glitch = True
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN,key=pygame.K_F1))
        super(Module, self).handle_resume()