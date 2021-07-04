from pypboy import BaseModule
from pypboy.modules.data import quests
from pypboy.modules.data import misc
import settings


class Module(BaseModule):

    label = "DATA"

    def __init__(self, *args, **kwargs):
        self.submodules = [
            quests.Module(self),
            misc.Module(self)
        ]
        super(Module, self).__init__(*args, **kwargs)
        
    def handle_resume(self):
        self.pypboy.topmenu.label = self.label
        self.pypboy.topmenu.title = settings.MODULE_TEXT
        self.active.handle_action("resume")
        
