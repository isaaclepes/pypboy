from pypboy import BaseModule
from pypboy.modules.radio import radio
# from pypboy.modules.radio import live_radio
import settings

class Module(BaseModule):

    label = "RADIO"

    def __init__(self, *args, **kwargs):
        self.submodules = [
            radio.Module(self),
            # live_radio.Module(self),
        ]
        super(Module, self).__init__(*args, **kwargs)
        
    def handle_resume(self):
        self.pypboy.topmenu.label = self.label
        self.pypboy.topmenu.title = settings.MODULE_TEXT