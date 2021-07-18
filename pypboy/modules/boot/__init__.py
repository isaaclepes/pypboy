from pypboy import BaseModule
from pypboy.modules.boot import boot_text
from pypboy.modules.boot import pip_os
from pypboy.modules.boot import thumbs

class Module(BaseModule):

    label = "hidden"

    def __init__(self, *args, **kwargs):
        self.submodules = [
            boot_text.Module(self),
            pip_os.Module(self),
            thumbs.Module(self),
        ]
        super(Module, self).__init__(*args, **kwargs)
        
    def handle_resume(self):
        self.pypboy.topmenu.label = "hidden"
        #self.pypboy.topmenu.title = ["AP  75/99","HP  159/314", "LVL 31"]
        self.active.handle_action("resume")
 