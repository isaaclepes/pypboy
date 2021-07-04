from pypboy import BaseModule
from pypboy.modules.items import weapons
from pypboy.modules.items import apparel
from pypboy.modules.items import aid
from pypboy.modules.items import misc
from pypboy.modules.items import ammo
import settings

class Module(BaseModule):

    label = "INV"

    def __init__(self, *args, **kwargs):
        self.submodules = [
            weapons.Module(self),
            apparel.Module(self),
            aid.Module(self),
            misc.Module(self),
            ammo.Module(self)
        ]
        super(Module, self).__init__(*args, **kwargs)
        
    def handle_resume(self):
        self.pypboy.topmenu.label = self.label
        self.pypboy.topmenu.title = settings.MODULE_TEXT
        self.active.handle_action("resume")