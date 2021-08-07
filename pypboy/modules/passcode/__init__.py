from pypboy import BaseModule
from pypboy.modules.passcode import passcode
import settings

class Module(BaseModule):

    label = "PASSCODE"

    def __init__(self, *args, **kwargs):
        self.submodules = [
            passcode.Module(self),
        ]
        super(Module, self).__init__(*args, **kwargs)
        
    def handle_resume(self):
        self.pypboy.topmenu.label = "hidden"
        self.active.handle_action("resume")