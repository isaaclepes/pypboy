import game#
import config
import pygame
import datetime

class TopMenu(game.Entity):

    def __init__(self, label=None, title=[]):
        self.label = None
        self.title = []
        super(TopMenu, self).__init__((config.WIDTH, config.HEIGHT))
        self.rect[0] = config.top_menu_x
        self.rect[1] = config.top_menu_y      

    def update(self):
        #super(TopMenu, self).update(*args, **kwargs)
        self.image.fill((0, 0, 0)) #Clear text
        spacing = 40 #Set space between words
        prev_text_width = 74 # STAT width
        text_pos = 104 - spacing - prev_text_width #Set first location
        if self.label:  
            for section in self.title:
                text = config.RobotoB[33].render(section, True, (config.bright), (0, 0, 0)) #Setup text
                text_pos = text_pos + prev_text_width + spacing #Set draw location
                self.image.blit(text, (text_pos, 0)) #Draw text
                text_rect = text.get_rect() #Get text dimensions
                prev_text_width = text_rect.width            
                
                if section == self.label:
                    pygame.draw.line(self.image, (config.bright), (0, 35), (text_pos - 10, 35), 3) # Line from left edge of screen
                    pygame.draw.line(self.image, (config.bright), (text_pos + text_rect.width + 10, 35), (config.WIDTH, 35), 3) # Line to the right edge of screen
                    pygame.draw.line(self.image, (config.bright), (text_pos - 11, 10), (text_pos - 11, 35), 3)	#Left Vert bar
                    pygame.draw.line(self.image, (config.bright), (text_pos - 12, 10), (text_pos - 3, 10), 3)	#Left Short bar
                    pygame.draw.line(self.image, (config.bright), (text_pos + text_rect.width + 2, 10), (text_pos + text_rect.width + 12, 10), 3)	#Right Short bar
                    pygame.draw.line(self.image, (config.bright), (text_pos + text_rect.width + 11, 10), (text_pos + text_rect.width + 11, 35), 3)	#Right Vert bar
                else:
                    pygame.draw.line(self.image, (config.bright), (text_pos - 10, 35), (text_pos + text_rect.width + 10, 35), 3) # Horizontal Barclass TopMenu(game.Entity):

class Footer(game.Entity):
    def __init__(self, sections=[], bargraph=None):
        self.sections = []
        self.bargraph = None
        super(Footer, self).__init__((config.WIDTH, config.HEIGHT))
        self.rect[0] = 0
        self.rect[1] = config.HEIGHT - config.footer_height

    def update(self, *args, **kwargs):
        super(Footer, self).update(*args, **kwargs)

    def render(self, label=None):
        self.image.fill((0, 0, 0)) #Clear text
        spacing = 4 #Set space between sections
        prev_text_width = 74 # STAT width
        text_pos = 104 - spacing - prev_text_width #Set first location

        for section in self.sections:
            text = config.RobotoB[33].render(section, True, (config.bright), (0, 0, 0)) #Setup text
            text_pos = text_pos + prev_text_width + spacing #Set draw location
            self.image.blit(text, (text_pos, 0)) #Draw text
            text_rect = text.get_rect() #Get text dimensions
            prev_text_width = text_rect.width            
            
            if section == self.label:
                pygame.draw.line(self.image, (config.bright), (0, 35), (text_pos - 10, 35), 3) # Line from left edge of screen
                pygame.draw.line(self.image, (config.bright), (text_pos + text_rect.width + 10, 35), (config.WIDTH, 35), 3) # Line to the right edge of screen
                pygame.draw.line(self.image, (config.bright), (text_pos - 11, 10), (text_pos - 11, 35), 3)	#Left Vert bar
                pygame.draw.line(self.image, (config.bright), (text_pos - 12, 10), (text_pos - 3, 10), 3)	#Left Short bar
                pygame.draw.line(self.image, (config.bright), (text_pos + text_rect.width + 2, 10), (text_pos + text_rect.width + 12, 10), 3)	#Right Short bar
                pygame.draw.line(self.image, (config.bright), (text_pos + text_rect.width + 11, 10), (text_pos + text_rect.width + 11, 35), 3)	#Right Vert bar
            else:
                pygame.draw.line(self.image, (config.bright), (text_pos - 10, 35), (text_pos + text_rect.width + 10, 35), 3) # Horizontal Bar


class SubMenu(game.Entity):

    def __init__(self):
        self.menu = []
        super(SubMenu, self).__init__((config.WIDTH, 128))
        self.rect[0] = config.sub_menu_x
        self.rect[1] = config.sub_menu_y
        self.hidden = False

    def update(self, *args, **kwargs):
        super(SubMenu, self).update(*args, **kwargs)

    def select(self, module):
        self.selected = module
        self.image.fill((0, 0, 0))
        if self.hidden == False:
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
                #pygame.draw.rect(self.image, (config.bright), selected_rect, 2)
            self.image.blit(text, (config.menu_x + 5, offset))
            offset += text.get_size()[1] + 6
   
class Scanlines(game.core.Entity):

    def __init__(self):
        super(Scanlines, self).__init__((config.WIDTH, config.HEIGHT))
        self.width = 720
        self.height = 1600
        self.image = pygame.image.load('images/scanline.png').convert_alpha()
        self.rectimage = self.image.get_rect()
        self.rect[1] = 0
        self.top = -870
        self.speed = 100
        
    def render(self, interval, *args, **kwargs):
        self.top += self.speed * interval
        self.rect[1] = self.top
        self.dirty = 1
        if self.top >= 0:
            self.top = -870
        super(Scanlines, self).render(self, *args, **kwargs)

        
class Overlay(game.Entity):
    def __init__(self):
        super(Overlay, self).__init__()
        self.image = pygame.image.load('images/overlay.png').convert_alpha()
        #self.image.set_colorkey((0,0,0))
        self.image.set_alpha(128)
        self.rect = self.image.get_rect()