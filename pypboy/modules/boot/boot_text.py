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
        
        self.image = pygame.surface.Surface((config.WIDTH, config.HEIGHT * 3))
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
        
        word_wrap(self.image, boot_text, config.FreeTechMono[17])

    # def update(self, *args, **kwargs):
        # super(Boot, self).update(self, *args, **kwargs)
        
    def render(self, *args, **kwargs):
        self.top -= 5
        self.rect[1] = self.top
        super(Boot, self).render(self, *args, **kwargs)
     
    def handle_resume(self):
        print("I need help getting this damn part working")
        #self.parent.pypboy.header.headline = "Boot_text"
        #self.parent.pypboy.header.title = [self.title]
        self.top = 0