import pypboy
import pygame
import game
import config
import pypboy.ui

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
        font.render_to(surf, (x, y), None, config.bright,None,1)
        x += bounds.width + space.width
    return x, y


class Module(pypboy.SubModule):

    label = "BOOT_TEXT"

    def __init__(self, *args, **kwargs):
        super(Module, self).__init__(*args, **kwargs)
        boot = Boot()
        boot.rect[0] = 0
        boot.rect[1] = config.header_height + 1
        self.add(boot)
        

class Boot(game.Entity):

    def __init__(self):
        super(Boot, self).__init__()
        
        self.image = pygame.Surface((config.WIDTH, config.HEIGHT - config.header_height - config.footer_height))
        self.rect[1] = 0
        self.top = 0
        
        word_wrap(self.image, boot_text, config.FreeTechMono[17])
        
    def render(self, *args, **kwargs):
        self.top -= 5
        self.rect[1] = self.top
        super(Boot, self).render(self, *args, **kwargs)
     
    def handle_resume(self):
        print("Resumed boot_text")
        #self.parent.pypboy.header.headline = "Boot_text"
        #self.parent.pypboy.header.title = [self.title]
        self.top = 0
        self.rect[1] = self.top
        super(Module, self).handle_resume()