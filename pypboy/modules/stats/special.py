import pypboy
import pygame
import game
import config


class Module(pypboy.SubModule):

    label = "S.P.E.C.I.A.L."

    def __init__(self, *args, **kwargs):
        super(Module, self).__init__(*args, **kwargs)

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

    def show_str(self):
        print("Strength")

    def show_per(self):
        print("Perception")

    def show_end(self):
        print("Endurance")

    def show_cha(self):
        print("Charisma")

    def show_int(self):
        print("Intelligence")

    def show_agi(self):
        print("Agility")

    def show_luc(self):
        print("Luck")