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

    modules = []
    currentModule = 0
    submodules = []
    currentSubmodule = 0

    def __init__(self, boy, *args, **kwargs):
        super(BaseModule, self).__init__()

        #if config.GPIO_AVAILABLE:
            #GPIO.setup(self.GPIO_LED_ID, GPIO.OUT)
            #GPIO.output(self.GPIO_LED_ID, False)

        self.pypboy = boy
        self.position = (0, config.header_height)


        # self.topmenu = pypboy.ui.TopMenu()
        # self.topmenu.menu = []
        # for mod in self.modules:
           # self.topmenu.menu.append(mod.label)
        # self.topmenu.selected = self.topmenu.menu[0]
        # self.topmenu.position = (config.top_menu_x, config.top_menu_y)
        # self.add(self.topmenu)


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
        print("Changing submodules")
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

    def handle_swipe(self, swipe):
        pass
        # print("Handle Swipe " + str(swipe))
        # if swipe == 2:
            # self.currentSubmodule -= 1
            # if self.currentSubmodule < 0:
                # self.currentSubmodule = self.submodules.__len__() - 1
            # self.switch_submodule(self.currentSubmodule)
        # elif swipe == 1:
            # self.currentSubmodule += 1
            # if self.currentSubmodule >= self.submodules.__len__():
                # self.currentSubmodule = 0
            # self.switch_submodule(self.currentSubmodule)
        # else:
            # self.active.handle_tap()


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
