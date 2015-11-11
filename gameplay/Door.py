from engine.Element import Element;
from engine.render.image import Image;
from engine.render.text import Text;
#	--------------------------------------------------- *\
#		[class] Door()
#
#		* Create a door *
#
#	--------------------------------------------------- */
class Door(Element):
	#	--------------------------------------------------- *\
	#		[function] __init__():
	#
	#		* Constructor *
	#	--------------------------------------------------- */
	def __init__(self, category, x, y):
		super().__init__();
		self.category = category;
		self.setPosition(x, y);

		# add texture to the door
		texture = Image("assets/elements/doors/" + category + ".png");
		if texture:
			self.assignDrawable(texture);
			self.size = texture.getSize();