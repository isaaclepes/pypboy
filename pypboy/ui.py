import game
import config
import pygame
import datetime

# class Header(game.Entity):

    # def __init__(self, headline="", title=[]):
        # self.headline = headline
        # self.title = []
        # super(Header, self).__init__((config.WIDTH, config.header_height))
        # self._date = None

    # def update(self, *args, **kwargs):
        # super(Header, self).update(*args, **kwargs)

    # def render(self, *args, **kwargs):
        # new_date = datetime.datetime.now().strftime("%d.%m.%y.%H:%M:%S") #need to be moved to footer and under the data and maps section
        # if new_date != self._date:
            # #self.image.fill((0, 0, 0))
            # text = config.RobotoB[14].render(self._date, True, (95, 255, 177), (0, 0, 0))
            # self.image.blit(text, (10, 5))
            # self._date = new_date
        # super(Header, self).update(*args, **kwargs)


class TopMenu(game.Entity):

    def __init__(self):
        self.menu = []
        super(TopMenu, self).__init__((config.WIDTH, 128))
        self.rect[0] = config.top_menu_x
        self.rect[1] = config.top_menu_y
        
    def update(self, *args, **kwargs):
        super(TopMenu, self).update(*args, **kwargs)

    def select(self, module):
        self.selected = module
        self.image.fill((0, 0, 0))
        offset = 18
        for m in self.menu:
            padding = 1
            text_width = 0
            while text_width < 54:
                spaces = " ".join([" " for x in range(padding)])
                text = config.RobotoB[30].render("%s%s%s" % (spaces, m, spaces), True, (config.mid), (0, 0, 0))
                text_width = text.get_size()[0]
                padding += 1
            #print(m+" : "+str(text.get_size()))
            if m == self.selected:
                text = config.RobotoB[30].render("%s%s%s" % (spaces, m, spaces), True, (config.bright), (0, 0, 0))
            self.image.blit(text, (offset, 0))

            offset = offset + text_width


class SubMenu(game.Entity):

    def __init__(self):
        self.menu = []
        super(SubMenu, self).__init__((config.WIDTH, 128))
        self.rect[0] = config.sub_menu_x
        self.rect[1] = config.sub_menu_y

    def update(self, *args, **kwargs):
        super(SubMenu, self).update(*args, **kwargs)

    def select(self, module):
        self.selected = module
        self.image.fill((0, 0, 0))
        offset = 18
        for m in self.menu:
            padding = 1
            text_width = 0
            while text_width < 54:
                spaces = " ".join([" " for x in range(padding)])
                text = config.RobotoR[30].render("%s%s%s" % (spaces, m, spaces), True, (config.mid), (0, 0, 0))
                text_width = text.get_size()[0]
                padding += 1
            #print(m+" : "+str(text.get_size()))
            if m == self.selected:
                text = config.RobotoR[30].render("%s%s%s" % (spaces, m, spaces), True, (config.bright), (0, 0, 0))
            self.image.blit(text, (offset, 0))

            offset = offset + text_width


class Menu(game.Entity):

    def __init__(self, width, items=[], callbacks=[], selected=0, xoffset=5):
        super(Menu, self).__init__((width, config.HEIGHT))
        self.items = items
        self.callbacks = callbacks
        self.selected = 0
        self.select(selected)

        if config.SOUND_ENABLED:
            self.dial_move_sfx = pygame.mixer.Sound('sounds/dial_move.ogg')

    def select(self, item):
        self.selected = item
        self.image.fill((0, 0, 0))
        self.redraw()
        if len(self.callbacks) > item and self.callbacks[item]:
            self.callbacks[item]()

    def handle_action(self, action):
        if action == "dial_up":
            if self.selected > 0:
                if config.SOUND_ENABLED:
                    self.dial_move_sfx.play()
                self.select(self.selected - 1)
        if action == "dial_down":
            if self.selected < len(self.items) - 1:
                if config.SOUND_ENABLED:
                    self.dial_move_sfx.play()
                self.select(self.selected + 1)

    def redraw(self):
        self.image.fill((0, 0, 0))
        offset = 5
        for i in range(len(self.items)):
            text = config.RobotoB[28].render(" %s " % self.items[i], True, (config.bright), (0, 0, 0))
            if i == self.selected:
                text = config.RobotoB[28].render(" %s " % self.items[i], True, (0,0,0), (config.bright))
                #selected_rect = (self.menuXVal, offset - 2, text.get_size()[0] + 10, text.get_size()[1] + 3)
                #pygame.draw.rect(self.image, (95, 255, 177), selected_rect, 2)
            self.image.blit(text, (config.menu_x + 5, offset))
            offset += text.get_size()[1] + 6


   
class Scanlines(game.core.Entity):

    def __init__(self):
        super(Scanlines, self).__init__((config.WIDTH, config.HEIGHT))
        self.width = 720
        self.height = 149
        self.image = pygame.image.load('images/scanline.png').convert_alpha()
        self.rectimage = self.image.get_rect()
        self.rect[1] = 0
        self.top = -149
        self.speed = 100
        
    def render(self, interval, *args, **kwargs):
        self.top += self.speed * interval
        self.rect[1] = self.top
        self.dirty = 1
        if self.top >= config.HEIGHT + 149:
            self.top = -149
        super(Scanlines, self).render(self, *args, **kwargs)