from pypboy import BaseModule
from pypboy.modules.boot import passcode

class Module(BaseModule):

    label = "PASSCODE"

    def __init__(self, *args, **kwargs):
        self.submodules = [
            passcode.Module(self),
        ]
        super(Module, self).__init__(*args, **kwargs)
        
    def handle_resume(self):
        #self.pypboy.topmenu.headline = self.label
        #self.pypboy.topmenu.title = ["AP  75/99","HP  159/314", "LVL 31"]
        self.active.handle_action("resume")
 