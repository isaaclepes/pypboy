import pypboy
import pygame
import game
import settings
import pypboy.ui
import pypboy.core
import time

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
        font.render_to(surf, (x, y), None, settings.bright,None,1)
        x += bounds.width + space.width
    return x, y


class Module(pypboy.SubModule):

    label = "hidden"

    def __init__(self, *args, **kwargs):
        super(Module, self).__init__(*args, **kwargs)
        self.boot = Boot()
        self.boot.rect[0] = 0
        self.boot.rect[1] = 51
        self.add(self.boot)
        
    def handle_resume(self):
        self.boot.top = 0
        super(Module, self).handle_resume()


        
class Boot(game.Entity):

    def __init__(self):
        super(Boot, self).__init__()
        
        self.image = pygame.surface.Surface((settings.WIDTH, 1880))
        self.rect[1] = 0
        self.top = 0

        boot_text = ("* 1 0 0x0000A4 0x00000000000000000 start memory discovery 0 0x0000A4 "
            "0x00000000000000000 1 0 0x000014 0x00000000000000000 CPUO starting cell "
            "relocation0 0x0000A4 0x00000000000000000 1 0 0x000009 "
            "0x00000000000000000 CPUO launch EFI0 0x0000A4 0x00000000000000000 1 0 "
            "0x000009 0x000000000000E003D CPUO starting EFI0 0x0000A4 "
            "0x00000000000000000 1 0 0x0000A4 0x00000000000000000 start memory "
            "discovery0 0x0000A4 0x00000000000000000 1 0 0x0000A4 0x00000000000000000 "
            "start memory discovery 0 0x0000A4 0x00000000000000000 1 0 0x000014 "
            "0x00000000000000000 CPUO starting cell relocation0 0x0000A4 "
            "0x00000000000000000 1 0 0x000009 0x00000000000000000 CPUO launch EFI0 "
            "0x0000A4 0x00000000000000000 1 0 0x000009 0x000000000000E003D CPUO "
            "starting EFI0 0x0000A4 0x00000000000000000 1 0 0x0000A4 "
            "0x00000000000000000 start memory discovery0 0x0000A4 0x00000000000000000 "
            "1 0 0x0000A4 0x00000000000000000 start memory discovery 0 0x0000A4 "
            "0x00000000000000000 1 0 0x000014 0x00000000000000000 CPUO starting cell "
            "relocation0 0x0000A4 0x00000000000000000 1 0 0x000009 "
            "0x00000000000000000 CPUO launch EFI0 0x0000A4 0x00000000000000000 1 0 "
            "0x000009 0x000000000000E003D CPUO starting EFI0 0x0000A4 "
            "0x00000000000000000 1 0 0x0000A4 0x00000000000000000 start memory "
            "discovery0 0x0000A4 0x00000000000000000 1 0 0x0000A4 0x00000000000000000 "
            "start memory discovery 0 0x0000A4 0x00000000000000000 1 0 0x000014 "
            "0x00000000000000000 CPUO starting cell relocation0 0x0000A4  "
            "0x00000000000000000 1 0 0x000009 0x00000000000000000 CPUO launch EFI0  "
            "0x0000A4 0x00000000000000000 1 0 0x000009 0x000000000000E003D CPUO  "
            "starting EFI0 0x0000A4 0x00000000000000000 1 0 0x0000A4  "
            "0x00000000000000000 start memory discovery0 0x0000A4 0x00000000000000000  "
            "1 0 0x0000A4 0x00000000000000000 start memory discovery 0 0x0000A4  "
            "0x00000000000000000 1 0 0x000014 0x00000000000000000 CPUO starting cell  "
            "relocation0 0x0000A4 0x00000000000000000 1 0 0x000009  "
            "0x00000000000000000 CPUO launch EFI0 0x0000A4 0x00000000000000000 1 0  "
            "0x000009 0x000000000000E003D CPUO starting EFI0 0x0000A4  "
            "0x00000000000000000 1 0 0x0000A4 0x00000000000000000 start memory  "
            "discovery0 0x0000A4 0x00000000000000000 1 0 0x0000A4 0x00000000000000000  "
            "start memory discovery 0 0x0000A4 0x00000000000000000 1 0 0x000014  "
            "0x00000000000000000 CPUO starting cell relocation0 0x0000A4  "
            "0x00000000000000000 1 0 0x000009 0x00000000000000000 CPUO launch EFI0  "
            "0x0000A4 0x00000000000000000 1 0 0x000009 0x000000000000E003D CPUO  "
            "starting EFI0 0x0000A4 0x00000000000000000 1 0 0x0000A4  "
            "0x00000000000000000 start memory discovery0 0x0000A4 0x00000000000000000  "
            "1 0 0x0000A4 0x00000000000000000 start memory discovery 0 0x0000A4  "
            "0x00000000000000000 1 0 0x000014 0x00000000000000000 CPUO starting cell  "
            "relocation0 0x0000A4 0x00000000000000000 1 0 0x000009  "
            "0x00000000000000000 CPUO launch EFI0 0x0000A4 0x00000000000000000 1 0  "
            "0x000009 0x000000000000E003D CPUO starting EFI0 0x0000A4  "
            "0x00000000000000000 1 0 0x0000A4 0x00000000000000000 start memory  "
            "discovery0 0x0000A4 0x00000000000000000 1 0 0x0000A4 0x00000000000000000  "
            "start memory discovery 0 0x0000A4 0x00000000000000000 1 0 0x000014  "
            "0x00000000000000000 CPUO starting cell relocation0 0x0000A4  "
            "0x00000000000000000 1 0 0x000009 0x00000000000000000 CPUO launch EFI0  "
            "0x0000A4 0x00000000000000000 1 0 0x000009 0x000000000000E003D CPUO  "
            "starting EFI0 0x0000A4 0x00000000000000000 1 0 0x0000A4  "
            "0x00000000000000000 start memory discovery0 0x0000A4 0x00000000000000000  "
            "1 0 0x0000A4 0x00000000000000000 start memory discovery 0 0x0000A4  "
            "0x00000000000000000 1 0 0x000014 0x00000000000000000 CPUO starting cell  "
            "relocation0 0x0000A4 0x00000000000000000 1 0 0x000009  "
            "0x00000000000000000 CPUO launch EFI0 0x0000A4 0x00000000000000000 1 0  "
            "0x000009 0x000000000000E003D CPUO starting EFI0 0x0000A4  "
            "0x00000000000000000 1 0 0x0000A4 0x00000000000000000 start memory  "
            "discovery0 0x0000A4 0x00000000000000000 1 0 0x0000A4 0x00000000000000000  "
            "start memory discovery 0 0x0000A4 0x00000000000000000 1 0 0x000014  "
            "0x00000000000000000 CPUO starting cell relocation0 0x0000A4  "
            "0x00000000000000000 1 0 0x000009 0x00000000000000000 CPUO launch EFI0  "
            "0x0000A4 0x00000000000000000 1 0 0x000009 0x000000000000E003D CPUO  "
            "starting EFI0 0x0000A4 0x00000000000000000 1 0 0x0000A4  "
            "0x00000000000000000 start memory discovery0 0x0000A4 0x00000000000000000  "
            "1 0 0x0000A4 0x00000000000000000 start memory discovery 0 0x0000A4  "
            "0x00000000000000000 1 0 0x000014 0x00000000000000000 CPUO starting cell  "
            "relocation0 0x0000A4 0x00000000000000000 1 0 0x000009  "
            "0x00000000000000000 CPUO launch EFI0 0x0000A4 0x00000000000000000 1 0  "
            "0x000009 0x000000000000E003D CPUO starting EFI0 0x0000A4  "
            "0x00000000000000000 1 0 0x0000A4 0x00000000000000000 start memory  "
            "discovery0 0x0000A4 0x00000000000000000 1 0 0x0000A4 0x00000000000000000  "
            "start memory discovery 0 0x0000A4 0x00000000000000000 1 0 0x000014  "
            "0x00000000000000000 CPUO starting cell relocation0 0x0000A4  "
            "0x00000000000000000 1 0 0x000009 0x00000000000000000 CPUO launch EFI0  "
            "0x0000A4 0x00000000000000000 1 0 0x000009 0x000000000000E003D CPUO  "
            "starting EFI0 0x0000A4 0x00000000000000000 1 0 0x0000A4  "
            "0x00000000000000000 start memory discovery0 0x0000A4 0x00000000000000000  "
            "1 0 0x0000A4 0x00000000000000000 start memory discovery 0 0x0000A4  "
            "0x00000000000000000 1 0 0x000014 0x00000000000000000 CPUO starting cell  "
            "relocation0 0x0000A4 0x00000000000000000 1 0 0x000009  "
            "0x00000000000000000 CPUO launch EFI0 0x0000A4 0x00000000000000000 1 0  "
            "0x000009 0x000000000000E003D CPUO starting EFI0 0x0000A4  "
            "0x00000000000000000 1 0 0x0000A4 0x00000000000000000 start memory  "
            "discovery0 0x0000A4 0x00000000000000000 1 0 0x0000A4 0x00000000000000000  "
            "start memory discovery 0 0x0000A4 0x00000000000000000 1 0 0x000014  "
            "0x00000000000000000 CPUO starting cell relocation0 0x0000A4  "
            "0x00000000000000000 1 0 0x000009 0x00000000000000000 CPUO launch EFI0  "
            "0x0000A4 0x00000000000000000 1 0 0x000009 0x000000000000E003D CPUO  "
            "starting EFI0 0x0000A4 0x00000000000000000 1 0 0x0000A4  "
            "0x00000000000000000 start memory discovery0 0x0000A4 0x00000000000000000  "
            "1 0 0x0000A4 0x00000000000000000 start memory discovery 0 0x0000A4  "
            "0x00000000000000000 1 0 0x000014 0x00000000000000000 CPUO starting cell  "
            "relocation0 0x0000A4 0x00000000000000000 1 0 0x000009  "
            "0x00000000000000000 CPUO launch EFI0 0x0000A4 0x00000000000000000 1 0  "
            "0x000009 0x000000000000E003D CPUO starting EFI0 0x0000A4  "
            "0x00000000000000000 1 0 0x0000A4 0x00000000000000000 start memory  "
            "discovery0 0x0000A4 0x00000000000000000 1 0 0x0000A4 0x00000000000000000  "
            "start memory discovery 0 0x0000A4 0x00000000000000000 1 0 0x000014  "
            "0x00000000000000000 CPUO starting cell relocation0 0x0000A4  "
            "0x00000000000000000 1 0 0x000009 0x00000000000000000 CPUO launch EFI0  "
            "0x0000A4 0x00000000000000000 1 0 0x000009 0x000000000000E003D CPUO  "
            "starting EFI0 0x0000A4 0x00000000000000000 1 0 0x0000A4  "
            "0x00000000000000000 start memory discovery0 0x0000A4 0x00000000000000000 END"
        )
        
        self.prev_time = 0
        self.animation_time = 0.005
   
        word_wrap(self.image, boot_text, settings.FreeTechMono[17])
        
    def render(self, *args, **kwargs):
        self.current_time = time.time()
        if self.prev_time == 0:
            self.prev_time = self.current_time
        self.delta_time = self.current_time - self.prev_time
        self.prev_time = self.current_time

        if self.delta_time >= self.animation_time:
        
            if settings.PI == True:
                self.top -= int(20*int(round(1/self.delta_time))/50)    
            else:
                self.top -= int(20*int(round(1/self.delta_time))/100)
            self.rect[1] = round(self.top)

            if self.top <= -1880:
                self.top = 0
                pygame.event.post(pygame.event.Event(pygame.KEYDOWN,key=pygame.K_2))
        super(Boot, self).render(self, *args, **kwargs)

    def handle_resume(self):
        self.top = 0