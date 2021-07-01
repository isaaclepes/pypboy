import pygame
import game
import config
import pypboy.ui
from enum import Enum

if config.GPIO_AVAILABLE:
    import RPi.GPIO as GPIO

class GameState(Enum):
    BOOT = -4
    RADIO = -3
    MAP = -2
    DATA = -1
    INV = 0
    STATS = 1

class BaseModule(game.EntityGroup):

    submodules = []
    currentSubmodule = 0

    def __init__(self, boy, *args, **kwargs):
        super(BaseModule, self).__init__()

        #if config.GPIO_AVAILABLE:
            #GPIO.setup(self.GPIO_LED_ID, GPIO.OUT)
            #GPIO.output(self.GPIO_LED_ID, False)

        self.pypboy = boy
        self.position = (0, config.header_height)

        self.submenu = pypboy.ui.SubMenu()
        self.submenu.menu = []
        for mod in self.submodules:
           self.submenu.menu.append(mod.label)
        self.submenu.selected = self.submenu.menu[0]
        self.submenu.position = (config.sub_menu_x, config.sub_menu_y)
        self.add(self.submenu)

        self.action_handlers = {
            "pause": self.handle_pause,
            "resume": self.handle_resume
        }
        
        self.switch_submodule(0)
        
        if config.SOUND_ENABLED:
            self.module_change_sfx = pygame.mixer.Sound('sounds/module_change.ogg')

    def move(self, x, y):
        super(BaseModule, self).move(x, y)
        if hasattr(self, 'active'):
            self.active.move(x, y)

    def switch_submodule(self, module):
        pygame.display.flip()
        print("Changing to sub-module", module)
        if hasattr(self, 'active') and self.active:
            self.active.handle_action("pause")
            self.remove(self.active)
        if len(self.submodules) > module:
            self.active = self.submodules[module]
            self.active.parent = self
            self.active.handle_action("resume")
            self.submenu.select(self.submenu.menu[module])
            self.add(self.active)
        else:
            print("No submodule at %d" % module)

    def render(self, interval): 
        self.active.render(interval)
        super(BaseModule, self).render(interval)

    def handle_action(self, action, value=0):
        if action.startswith("knob_"):
            num = int(action[-1])
            self.switch_submodule(num - 1)
        elif action in self.action_handlers:
            self.action_handlers[action]()
        else:
            if hasattr(self, 'active') and self.active:
                self.active.handle_action(action, value)

    def handle_event(self, event):
        if hasattr(self, 'active') and self.active:
            self.active.handle_event(event)


    def handle_pause(self):
        self.paused = True
        self.currentSubmodule = 0
        self.switch_submodule(0)
        #if config.GPIO_AVAILABLE:
            #GPIO.output(self.GPIO_LED_ID, False)

    def handle_resume(self):
        self.paused = False
        self.currentSubmodule = 0
        self.switch_submodule(0)
        #if config.GPIO_AVAILABLE:
            #GPIO.output(self.GPIO_LED_ID, True)
        if config.SOUND_ENABLED:
            self.module_change_sfx.play()

class SubModule(game.EntityGroup):

    def __init__(self, parent, *args, **kwargs):
        super(SubModule, self).__init__()
        self.parent = parent

        self.action_handlers = {
            "pause": self.handle_pause,
            "resume": self.handle_resume
        }

        if config.SOUND_ENABLED:
            self.submodule_change_sfx = pygame.mixer.Sound('sounds/submodule_change.ogg')

    def handle_action(self, action, value=0):
        if action.startswith("dial_"):
            if hasattr(self, "menu"):
                self.menu.handle_action(action)
        elif action in self.action_handlers:
            self.action_handlers[action]()

    def handle_event(self, event):
        pass

    def handle_pause(self):
        self.paused = True

    def handle_resume(self):
        self.paused = False
        if config.SOUND_ENABLED:
            self.submodule_change_sfx.play()
    
    def handle_tap(self):
        pass
