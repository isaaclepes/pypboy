from game.core import Entity
import pypboy
import pygame
import game
import config


class Module(pypboy.SubModule):

    label = "S.P.E.C.I.A.L."

    def __init__(self, *args, **kwargs):
        super(Module, self).__init__(*args, **kwargs)

        self.stat = Stat('images/special_strength.png', 'Strength')
        self.stat.rect[0] = 4
        self.stat.rect[1] = 40
        self.add(self.stat)

        self.menu = pypboy.ui.Menu(240, [
            "Strength               4", 
            "Perception             7", 
            "Endurance              5", 
            "Charisma               6", 
            "Intelligence           9", 
            "Agility                4", 
            "Luck                   6"], [self.show_str, self.show_per, self.show_end, self.show_cha, self.show_int, self.show_agi, self.show_luc], 0)
        self.menu.rect[0] = 4
        self.menu.rect[1] = 60
        self.add(self.menu)

    def changeStat(self, imageUrl, description):
        self.stat.image = pygame.image.load(imageUrl)
        self.stat.rect = self.stat.image.get_rect()
        self.stat.rect[0] = 100
        self.stat.rect[1] = 0
        self.stat.image = self.stat.image.convert()
        #text = config.FONTS[18].render(description, True, (105, 251, 20), (0, 0, 0))
        #text_width = text.get_size()[0]
        #self.stat.image.blit(text, (config.WIDTH / 2 - 8 - text_width / 2, 200))

    def show_str(self):
        self.changeStat('images/special_strength.png', config.SPECIAL['strength'])
        print("Strength")

    def show_per(self):
        self.changeStat('images/special_perception.png', config.SPECIAL['perception'])
        print("Perception")

    def show_end(self):
        self.changeStat('images/special_endurance.png', config.SPECIAL['endurance'])
        print("Endurance")

    def show_cha(self):
        self.changeStat('images/special_charisma.png', config.SPECIAL['charisma'])
        print("Charisma")

    def show_int(self):
        self.changeStat('images/special_intelligence.png', config.SPECIAL['intelligence'])
        print("Intelligence")

    def show_agi(self):
        self.changeStat('images/special_agility.png', config.SPECIAL['agility'])
        print("Agility")

    def show_luc(self):
        self.changeStat('images/special_luck.png', config.SPECIAL['luck'])
        print("Luck")

class Stat(game.Entity):
    def __init__(self, imageUrl, description):
        super(Stat, self).__init__()
        self.image = pygame.image.load(imageUrl)
        self.rect = self.image.get_rect()
        self.image = self.image.convert()
        #text = config.FONTS[18].render(description, True, (105, 251, 20), (0, 0, 0))
        #text_width = text.get_size()[0]
        #self.image.blit(text, (config.WIDTH / 2 - 8 - text_width / 2, 150))
