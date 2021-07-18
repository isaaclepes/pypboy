import game#
import pygame
import settings
import time
import os
import imp

def word_wrap(surf, text, font):
    text = str(text)
    font.origin = True
    words = text.split()
    width, height = surf.get_size()
    line_spacing = font.get_sized_height()
    x, y = 0, line_spacing
    for word in words:
        word = word + str("  ")
        bounds = font.get_rect(word)
        if x + bounds.width + bounds.x >= width:
            x, y = 0, y + line_spacing
        #if x + bounds.width + bounds.x >= width:
        #    raise ValueError("word too wide for the surface")
        #if y + bounds.height - bounds.y >= height:
        #    raise ValueError("text to long for the surface")
        font.render_to(surf, (x, y), word, settings.bright,None,1)
        x += bounds.width
    return x, y

class TopMenu(game.Entity):

    def __init__(self, label=None, title=[]):
        self.label = None
        self.prev_label = 0
        self.title = []
        super(TopMenu, self).__init__((settings.WIDTH, 40))
        self.rect[0] = 0
        self.rect[1] = 51

    def render(self):
        # super(TopMenu, self).render(*args, **kwargs)
        spacing = 40 #Set space between words
        prev_text_width = 74 # STAT width
        text_pos = 104 - spacing - prev_text_width #Set first location
        if self.label:
            if self.label != self.prev_label:
                self.image.fill((0, 0, 0)) #Clear text
                if self.label != "hidden":
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
            self.prev_label = self.label

        if settings.glitch == True:
            if settings.glitch_next == 1 or settings.glitch_next == 3 or settings.glitch_next == 5:
                self.rect[1] = -149
            elif settings.glitch_next == 2 or settings.glitch_next == 4 or settings.glitch_next == 6:
                self.rect[1] = 251
            elif settings.glitch_next >= 7:
                self.rect[1] = 51


   
class Scanlines(game.core.Entity):

    def __init__(self):
        super(Scanlines, self).__init__((settings.WIDTH, 129))
        # self.width = 720
        # self.height = 1600
        self.image = pygame.image.load('images/scanline.png').convert_alpha()
        self.rectimage = self.image.get_rect()
        self.rect[1] = 0
        self.top = -130
        self.speed = 10
        self.clock = pygame.time.Clock()
        self.animation_time = 0.05
        self.prev_time = 0
        self.dirty = 2
        
    def render(self, *args, **kwargs):
        
        self.current_time = time.time()
        self.delta_time = self.current_time - self.prev_time
        
        if self.delta_time >= self.animation_time:
            self.prev_time = self.current_time
            self.top = self.top + self.speed        
            if self.top >= settings.HEIGHT + 130:
                self.top = -130
            self.rect[1] = self.top
        super(Scanlines, self).render(self, *args, **kwargs)
        
class Overlay(game.Entity):
    def __init__(self):
        super(Overlay, self).__init__()
        self.image = pygame.image.load('images/overlay.png').convert_alpha()


class SubMenu(game.Entity):

    def __init__(self):
        super(SubMenu, self).__init__((settings.WIDTH, 36))
        self.menu = []
        self.rect[0] = 73
        self.rect[1] = 93
        self.hidden = False
        self.prev_time = 0
        
    def render(self):
        if settings.glitch == True:
            if settings.glitch_next == 1 or settings.glitch_next == 3 or settings.glitch_next == 5:
                self.rect[1] = -107
            elif settings.glitch_next == 2 or settings.glitch_next == 4 or settings.glitch_next == 6:
                self.rect[1] = 293
            elif settings.glitch_next >= 7:
                self.rect[1] = 93
    # def update(self, *args, **kwargs):
    #     super(SubMenu, self).update(*args, **kwargs)

    def select(self, module):
        self.selected = module

        self.image.fill((0, 0, 0))
        self.textoffset = 18
        if module != "hidden":
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
                self.image.blit(text, (self.textoffset, 0))
                self.textoffset = self.textoffset + text_width

           

class Footer(game.Entity):
    def __init__(self, sections=[], bargraph=None):
        super(Footer, self).__init__((settings.WIDTH, 50))
        self.sections = []
        self.bargraph = None
        self.rect[0] = 0
        self.rect[1] = settings.HEIGHT - 50
        self.image.fill((0, 0, 0)) #Clear text
        

    def render(self, label=None):
        pass
        # #self.image.fill((0, 0, 0)) #Clear text
        # spacing = 4 #Set space between sections
        # prev_text_width = 74 # STAT width
        # text_pos = 104 - spacing - prev_text_width #Set first location

        # for section in self.sections:
        #     text = settings.RobotoB[33].render(section, True, (settings.bright), (0, 0, 0)) #Setup text
        #     text_pos = text_pos + prev_text_width + spacing #Set draw location
        #     self.image.blit(text, (text_pos, 0)) #Draw text
        #     text_rect = text.get_rect() #Get text dimensions
        #     prev_text_width = text_rect.width            
            
        #     if section == self.label:
        #         pygame.draw.line(self.image, (settings.bright), (0, 35), (text_pos - 10, 35), 3) # Line from left edge of screen
        #         pygame.draw.line(self.image, (settings.bright), (text_pos + text_rect.width + 10, 35), (settings.WIDTH, 35), 3) # Line to the right edge of screen
        #         pygame.draw.line(self.image, (settings.bright), (text_pos - 11, 10), (text_pos - 11, 35), 3)	#Left Vert bar
        #         pygame.draw.line(self.image, (settings.bright), (text_pos - 12, 10), (text_pos - 3, 10), 3)	#Left Short bar
        #         pygame.draw.line(self.image, (settings.bright), (text_pos + text_rect.width + 2, 10), (text_pos + text_rect.width + 12, 10), 3)	#Right Short bar
        #         pygame.draw.line(self.image, (settings.bright), (text_pos + text_rect.width + 11, 10), (text_pos + text_rect.width + 11, 35), 3)	#Right Vert bar
        #     else:
        #         pygame.draw.line(self.image, (settings.bright), (text_pos - 10, 35), (text_pos + text_rect.width + 10, 35), 3) # Horizontal Bar


#Menu_array Structure: [["Menu item",Quantity,"Image (or folder for animation")","Description text","Stat Text","Stat Number"],],
#Probably not the correct way to do this.
class Menu(game.Entity):

    def __init__(self, menu_array=[], callbacks=[], selected=0):
        super(Menu, self).__init__((settings.WIDTH-settings.menu_x, 450))
        self.items = [] #List of items to display
        self.number = [] #Numbers to put next to those items
        self.image_list = [] # Path to image or folder for animation
        self.description = []
        self.stat_text = []
        self.stat_number = []
        self.images = []
        self.frameorder = []
        
        self.prev_time = 0
        self.prev_fps_time = 0
        self.clock = pygame.time.Clock()
        self.animation_time = 0.2
        self.index = 0

        self.descriptionbox = pygame.Surface((360,300))
        self.imagebox = pygame.Surface((240,240))

        for i in range(len(menu_array)):
            try:
                self.items.append(menu_array[i][0])
            except:
                continue
            try:
                self.number.append(menu_array[i][1])
            except:
                continue
            try:
                self.image_list.append(menu_array[i][2])
            except:
                continue
            try:    
                self.description.append(menu_array[i][3])
            except:
                continue
            try:
                self.stat_text.append(menu_array[i][4])
            except:
                continue
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
        
        self.selected = 0
        self.select(selected)

        if settings.SOUND_ENABLED:
            self.dial_move_sfx = pygame.mixer.Sound('sounds/pipboy/RotaryVertical/UI_PipBoy_RotaryVertical_01.wav')
            self.dial_move_sfx.set_volume(settings.VOLUME)

    def select(self, item):
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
            if i == self.selected:
                text = settings.RobotoB[30].render(" %s " % self.items[i], True, (0,0,0), (settings.bright))
                try:
                    number = settings.RobotoB[30].render(" %s " % self.number[i], True, (0,0,0), (settings.bright))
                except:
                    number = ""
                
                selected_rect = (0, offset, settings.menu_x+300, text.get_size()[1])
                pygame.draw.rect(self.image, (settings.bright), selected_rect)
                

                self.images = []
                try: #Try loading a image if there is one
                    self.image_url = self.image_list[i]
                except:
                    self.image_url = ""

                if os.path.isdir(self.image_url):
                    for filename in sorted(os.listdir(self.image_url)):
                        if filename.endswith(".png"):
                            filename = self.image_url + "/" + filename
                            self.images.append(pygame.image.load(filename).convert_alpha())
                            self.frameorder = []
                            #print(filename)
                        if filename  == "frameorder.py":
                            url = self.image_url + "/" + filename
                            #print ("url =",url)
                            file = imp.load_source("frameorder.py", os.path.join(self.image_url,"frameorder.py"))
                            self.frameorder = file.frameorder
                            self.frame = 0
                         
                else:
                    if self.image_url:
                        self.frameorder = []
                        self.imagebox.fill((0,0,0))
                        self.graphic = pygame.image.load(self.image_url).convert_alpha()               
                        self.image.blit(self.graphic, (400,0))
                    
                try:
                    description = self.description[i]
                except:
                    description = ""

                if description:
                    self.descriptionbox.fill((0,0,0))
                    #  description = settings.RobotoB[24].render(self.description[i], True, (settings.bright), (0, 0, 0))
                    word_wrap(self.descriptionbox, self.description[i], settings.FreeRobotoR[20])
                    self.image.blit(self.descriptionbox, (350,240))
                
            else:
                text = settings.RobotoB[30].render(" %s " % self.items[i], True, (settings.bright), (0, 0, 0))
                try:
                    number = settings.RobotoB[30].render(" %s " % self.number[i], True, (settings.bright), (0, 0, 0))
                except:
                    number = None
            
            self.image.blit(text, (settings.menu_x, offset))

            if number:
                self.image.blit(number, (settings.menu_x+300, offset))
            offset += text.get_size()[1] + 6


    def render(self, *args, **kwargs):
        self.current_time = time.time()
        self.delta_time = self.current_time - self.prev_time
        
        if self.images: #If there is an animation list
            if self.delta_time >= self.animation_time:
                self.prev_time = self.current_time

                self.imagebox.fill((0,0,0))

                if self.index >= len(self.images):
                    self.index = 0 
                
                if self.frameorder: #Support non-linear frames
                    if self.frame >= len(self.frameorder):
                        self.frame = 0 
                    self.index = self.frameorder[self.frame]
                    self.frame += 1
                
                self.file = self.images[self.index]
                self.imagebox.blit(self.file,(0,0))
                self.image.blit(self.imagebox,(400,0))

                self.index += 1