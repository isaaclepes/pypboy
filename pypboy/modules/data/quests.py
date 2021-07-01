import pypboy
import config


class Module(pypboy.SubModule):

    label = "QUESTS"

    def __init__(self, *args, **kwargs):
        super(Module, self).__init__(*args, **kwargs)

        self.menu = pypboy.ui.Menu(350, config.QUESTS, [], 0)
        self.menu.rect[0] = config.menu_x
        self.menu.rect[1] = config.menu_y
        self.add(self.menu)
