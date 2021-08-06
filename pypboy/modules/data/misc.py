import pypboy
import settings

class Module(pypboy.SubModule):

	label = "MISC"



	def __init__(self, *args, **kwargs):
		super(Module, self).__init__(*args, **kwargs)

		settings.FOOTER_TIME[2] = ""
		self.footer = pypboy.ui.Footer(settings.FOOTER_TIME)
		self.footer.rect[0] = settings.footer_x
		self.footer.rect[1] = settings.footer_y
		self.add(self.footer)
