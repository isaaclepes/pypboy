from pypboy import BaseModule
from pypboy.modules.stats import status
from pypboy.modules.stats import special
from pypboy.modules.stats import skills
from pypboy.modules.stats import perks
import config

class Module(BaseModule):

    label = "STAT"

    def __init__(self, *args, **kwargs):
        self.submodules = [
            status.Module(self),
            special.Module(self),
            perks.Module(self)
        ]
        super(Module, self).__init__(*args, **kwargs)
        
    def handle_resume(self):
        self.pypboy.topmenu.label = self.label
        self.pypboy.topmenu.title = config.MODULE_TEXT
        self.active.handle_action("resume")
