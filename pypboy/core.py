import pygame
import config
import game
import pypboy.ui

from pypboy.modules import data
from pypboy.modules import items
from pypboy.modules import stats

if config.GPIO_AVAILABLE:
    import RPi.GPIO as GPIO


class Pypboy(game.core.Engine):

    currentModule = 0

    def __init__(self, *args, **kwargs):
        if hasattr(config, 'OUTPUT_WIDTH') and hasattr(config, 'OUTPUT_HEIGHT'):
            self.rescale = True
        super(Pypboy, self).__init__(*args, **kwargs)
        self.init_children()
        self.init_modules()
        
        self.gpio_actions = {}
        # if config.GPIO_AVAILABLE:
            # self.init_gpio_controls()

    def init_children(self):
        self.background = pygame.image.load('images/overlay.png')
        # border = pypboy.ui.Border()
        # self.root_children.add(border)
        scanlines = pypboy.ui.Scanlines(800, 480, 3, 1, [(0, 13, 3, 50), (6, 42, 22, 100), (0, 13, 3, 50)])
        self.root_children.add(scanlines)
        scanlines2 = pypboy.ui.Scanlines(800, 480, 8, 40, [(0, 10, 1, 0), (21, 62, 42, 90), (61, 122, 82, 100), (21, 62, 42, 90)] + [(0, 10, 1, 0) for x in range(50)], True)
        self.root_children.add(scanlines2)
        self.header = pypboy.ui.Header()
        self.root_children.add(self.header)

    def init_modules(self):
        self.modules = {
            "data": data.Module(self),
            "items": items.Module(self),
            "stats": stats.Module(self)
        }
        for module in self.modules.values():
            module.move(4, 40)
        self.switch_module("stats")

    def init_gpio_controls(self):
        for pin in config.GPIO_ACTIONS.keys():
            print("Intialising pin %s as action '%s'" % (pin, config.GPIO_ACTIONS[pin]))
            GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
            self.gpio_actions[pin] = config.GPIO_ACTIONS[pin]

    def check_gpio_input(self):
        for pin in self.gpio_actions.keys():
            if GPIO.input(pin) == False:
                self.handle_action(self.gpio_actions[pin])

    def update(self):
        if hasattr(self, 'active'):
            self.active.update()
        super(Pypboy, self).update()

    def render(self):
        interval = super(Pypboy, self).render()
        if hasattr(self, 'active'):
            self.active.render(interval)

    def switch_module(self, module):
        if module in self.modules:
            if hasattr(self, 'active'):
                self.active.handle_action("pause")
                self.remove(self.active)
            self.active = self.modules[module]
            self.active.parent = self
            self.active.handle_action("resume")
            self.add(self.active)
        else:
            print("Module '%s' not implemented." % module)

    def handle_swipe(self, swipe):
        if swipe == -1:
            return
        if swipe == 4: #UP
            self.currentModule += 1
            if self.currentModule > 2:
                self.currentModule = 0
            self.switch_module(config.MODULES[self.currentModule])
        elif swipe == 3: #DOWN
            self.currentModule -= 1
            if self.currentModule < 0:
                self.currentModule = 2
            self.switch_module(config.MODULES[self.currentModule])
        else:
            self.active.handle_swipe(swipe)

    def handle_action(self, action):
        if action.startswith('module_'):
            self.switch_module(action[7:])
        else:
            if hasattr(self, 'active'):
                self.active.handle_action(action)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_ESCAPE):
                self.running = False
            else:
                if event.key in config.ACTIONS:
                    self.handle_action(config.ACTIONS[event.key])
        elif event.type == pygame.QUIT:
            self.running = False
        elif event.type == config.EVENTS['SONG_END']:
            if config.SOUND_ENABLED:
                if hasattr(config, 'radio'):
                    config.radio.handle_event(event)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseDownTime = pygame.time.get_ticks()
            mouseDownPos = pygame.mouse.get_pos()
            pygame.mouse.get_rel()
        elif event.type == pygame.MOUSEBUTTONUP:
            swipe = self.getSwipeType()
            self.handle_swipe(swipe)
        else:
            if hasattr(self, 'active'):
                self.active.handle_event(event)

    # Function to detect swipes
    # -1 is that it was not detected as a swipe or click
    # It will return 1 , 2 for horizontal swipe
    # If the swipe is vertical will return 3, 4
    # If it was a click it will return 0
    def getSwipeType(self):
        mouseRel=pygame.mouse.get_rel()
        x = 0
        y = 0
        if config.invertPosition:
            x = mouseRel[1] / config.touchScale
            y = mouseRel[0] / config.touchScale
        else:
            x = mouseRel[0] / config.touchScale
            y = mouseRel[1] / config.touchScale

        print("X: " + str(x) + " Y: " + str(y))
        if abs(x)<=config.minSwipe:
            if abs(y)<=config.minSwipe:
                if abs(x) < config.maxClick and abs(y)< config.maxClick:
                    return 0
                else:
                    return -1
            elif y>config.minSwipe:
                return 3
            elif y<-config.minSwipe:
                return 4
        elif abs(y)<=config.minSwipe:
            if x>config.minSwipe:
                return 1
            elif x<-config.minSwipe:
                return 2
        return 0

    def run(self):
        self.running = True
        while self.running:
            self.check_gpio_input()
            for event in pygame.event.get():
                self.handle_event(event)
            self.update()
            self.render()
            pygame.time.wait(1)

        try:
            pygame.mixer.quit()
        except Exception as e:
            print(e)
            pass
