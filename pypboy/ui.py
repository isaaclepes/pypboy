import game#
import pygame
import settings
import datetime

def word_wrap(surf, text, font):
    font.origin = True
    words = text.split(' ')
    width, height = surf.get_size()
    line_spacing = font.get_sized_height()
    x, y = 0, line_spacing
    space = font.get_rect(' ')
    for word in words:
        bounds = font.get_rect(word)
        if x + bounds.width + bounds.x >= width:
            x, y = 0, y + line_spacing
        #if x + bounds.width + bounds.x >= width:
        #    raise ValueError("word too wide for the surface")
        #if y + bounds.height - bounds.y >= height:
        #    raise ValueError("text to long for the surface")
        font.render_to(surf, (x, y), None, settings.bright,None,1)
        x += bounds.width + space.width
    return x, y

class TopMenu(game.Entity):

    def __init__(self, label=None, title=[]):
        self.label = None
        self.title = []
        super(TopMenu, self).__init__((settings.WIDTH, settings.HEIGHT))
        self.rect[0] = 0
        self.rect[1] = 51

    def update(self):
        #super(TopMenu, self).update(*args, **kwargs)
        self.image.fill((0, 0, 0)) #Clear text
        spacing = 40 #Set space between words
        prev_text_width = 74 # STAT width
        text_pos = 104 - spacing - prev_text_width #Set first location
        if self.label:  
            for section in self.title:
                text = settings.RobotoB[33].render(section, True, (settings.bright), (0, 0, 0)) #Setup text
                text_pos = text_pos + prev_text_width + spacing #Set draw location
                self.image.blit(text, (text_pos, 0)) #Draw text
                text_rect = text.get_rect() #Get text dimensions
                prev_text_width = text_rect.width            
                
                if section == self.label:
                    pygame.draw.line(self.image, (settings.bright), (0, 35), (text_pos - 10, 35), 3) # Line from left edge of screen
                    pygame.draw.line(self.image, (settings.bright), (text_pos + text_rect.width + 10, 35), (settings.WIDTH, 35), 3) # Line to the right edge of screen
                    pygame.draw.line(self.image, (settings.bright), (text_pos - 11, 10), (text_pos - 11, 35), 3)	#Left Vert bar
                    pygame.draw.line(self.image, (settings.bright), (text_pos - 12, 10), (text_pos - 3, 10), 3)	#Left Short bar
                    pygame.draw.line(self.image, (settings.bright), (text_pos + text_rect.width + 2, 10), (text_pos + text_rect.width + 12, 10), 3)	#Right Short bar
                    pygame.draw.line(self.image, (settings.bright), (text_pos + text_rect.width + 11, 10), (text_pos + text_rect.width + 11, 35), 3)	#Right Vert bar
                else:
                    pygame.draw.line(self.image, (settings.bright), (text_pos - 10, 35), (text_pos + text_rect.width + 10, 35), 3) # Horizontal Barclass TopMenu(game.Entity):

class Footer(game.Entity):
    def __init__(self, sections=[], bargraph=None):
        self.sections = []
        self.bargraph = None
        super(Footer, self).__init__((settings.WIDTH, settings.HEIGHT))
        self.rect[0] = 0
        self.rect[1] = settings.HEIGHT - 50

    def update(self, *args, **kwargs):
        super(Footer, self).update(*args, **kwargs)

    def render(self, label=None):
        self.image.fill((0, 0, 0)) #Clear text
        spacing = 4 #Set space between sections
        prev_text_width = 74 # STAT width
        text_pos = 104 - spacing - prev_text_width #Set first location

        for section in self.sections:
            text = settings.RobotoB[33].render(section, True, (settings.bright), (0, 0, 0)) #Setup text
            text_pos = text_pos + prev_text_width + spacing #Set draw location
            self.image.blit(text, (text_pos, 0)) #Draw text
            text_rect = text.get_rect() #Get text dimensions
            prev_text_width = text_rect.width            
            
            if section == self.label:
                pygame.draw.line(self.image, (settings.bright), (0, 35), (text_pos - 10, 35), 3) # Line from left edge of screen
                pygame.draw.line(self.image, (settings.bright), (text_pos + text_rect.width + 10, 35), (settings.WIDTH, 35), 3) # Line to the right edge of screen
                pygame.draw.line(self.image, (settings.bright), (text_pos - 11, 10), (text_pos - 11, 35), 3)	#Left Vert bar
                pygame.draw.line(self.image, (settings.bright), (text_pos - 12, 10), (text_pos - 3, 10), 3)	#Left Short bar
                pygame.draw.line(self.image, (settings.bright), (text_pos + text_rect.width + 2, 10), (text_pos + text_rect.width + 12, 10), 3)	#Right Short bar
                pygame.draw.line(self.image, (settings.bright), (text_pos + text_rect.width + 11, 10), (text_pos + text_rect.width + 11, 35), 3)	#Right Vert bar
            else:
                pygame.draw.line(self.image, (settings.bright), (text_pos - 10, 35), (text_pos + text_rect.width + 10, 35), 3) # Horizontal Bar


class SubMenu(game.Entity):

    def __init__(self):
        self.menu = []
        super(SubMenu, self).__init__((settings.WIDTH, 128))
        self.rect[0] = 73
        self.rect[1] = 93
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
                    text = settings.RobotoR[30].render("%s%s%s" % (spaces, m, spaces), True, (settings.mid), (0, 0, 0))
                    text_width = text.get_size()[0]
                    padding += 1
                #print(m+" : "+str(text.get_size()))
                if m == self.selected:
                    text = settings.RobotoR[30].render("%s%s%s" % (spaces, m, spaces), True, (settings.bright), (0, 0, 0))
                self.image.blit(text, (offset, 0))

                offset = offset + text_width


#Menu_array Structure: [["Menu item",Quantity,"Image (or folder for animation")","Description text","Stat Text","Stat Number"],],
#Probably not the correct way to do this.
class Menu(game.Entity):

    def __init__(self, menu_array=[], callbacks=[], selected=0):
        super(Menu, self).__init__((settings.WIDTH, settings.HEIGHT))
        self.items = [] #List of items to display
        self.number = [] #Numbers to put next to those items
        self.image_url = [] # Path to image or folder for animation
        self.description = []
        self.stat_text = []
        self.stat_number = []
        #print(" ")
        #print("menu_array =",menu_array)
        #print(" ")

        for i in range(len(menu_array)):
            try:
                self.items.append(menu_array[i][0])
            except:
                pass
            try:
                self.number.append(menu_array[i][1])
            except:
                pass
            try:
                self.image_url.append(menu_array[i][2])
            except:
                pass
            try:    
                self.description.append(menu_array[i][3])
            except:
                pass
            try:
                self.stat_text.append(menu_array[i][4])
            except:
                pass
            try:    
                self.stat_number.append(menu_array[i][5])
            except:
                continue
            #print ("Item to append =",menu_array[i][0])
        #print("self.number = ", self.number)
        #print("self.image_url = ", self.image_url)
        #print("self.description = ", self.description)
        try:
            self.callbacks = callbacks
            #print("self.callbacks = ", self.callbacks)
        except:
            self.callbacks = []

        #print(" ")
        
        self.selected = 0
        self.select(selected)

        if settings.SOUND_ENABLED:
            self.dial_move_sfx = pygame.mixer.Sound('sounds/dial_move.ogg')

    def select(self, item):
        #print ("item = ",item)
        self.selected = item
        self.redraw()
        if len(self.callbacks) > item and self.callbacks[item]:
            self.callbacks[item]()

    def handle_action(self, action):
        if action == "dial_up":
            if self.selected > 0:
                if settings.SOUND_ENABLED:
                    self.dial_move_sfx.play()
                self.select(self.selected - 1)
        if action == "dial_down":
            if self.selected < len(self.items) - 1:
                if settings.SOUND_ENABLED:
                    self.dial_move_sfx.play()
                self.select(self.selected + 1)

    def redraw(self):
        self.image.fill((0, 0, 0))
        offset = 5
        for i in range(len(self.items)):
            text = settings.RobotoB[30].render(" %s " % self.items[i], True, (settings.bright), (0, 0, 0))

            if i == self.selected:
                text = settings.RobotoB[30].render(" %s " % self.items[i], True, (0,0,0), (settings.bright))
                try: #Try loading a image if there is one
                    image_url = self.image_url[i]
                    self.graphic = pygame.image.load(image_url).convert_alpha()
                    self.image.blit(self.graphic, (350,0))
                except:
                    image_url = ""
                try: #Try loading decription
                    description = settings.RobotoB[24].render(self.description[i], True, (settings.bright), (0, 0, 0))
                    #word_wrap(self.image, description, settings.RobotoR[20])
                    self.image.blit(description, (350,240))
                except:
                    image_url = ""
                 

                #selected_rect = (self.menuXVal, offset - 2, text.get_size()[0] + 10, text.get_size()[1] + 3)
                #pygame.draw.rect(self.image, (settings.bright), selected_rect, 2)
            self.image.blit(text, (settings.menu_x, offset))
            offset += text.get_size()[1] + 6

   
class Scanlines(game.core.Entity):

    def __init__(self):
        super(Scanlines, self).__init__((settings.WIDTH, settings.HEIGHT))
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