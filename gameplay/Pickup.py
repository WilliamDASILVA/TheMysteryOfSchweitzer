from engine.Element import Element;
from engine import Render;
from engine.render.image import Image;

#	--------------------------------------------------- *\
#		[class] Pickup()
#
#		* Pickup element *
#
#	--------------------------------------------------- */
class Pickup(Element):
	#	--------------------------------------------------- *\
	#		[function] __init__():
	#
	#		* Constructor *
	#	--------------------------------------------------- */
	def __init__(self, type, x, y):
		super().__init__();
		self.setType("pickup");

		# add texture
		texture = Image("assets/dickbutt.png");
		texture.setSize(64,64);
		if texture:
			texture.setDepth(10);
			self.assignDrawable(texture);
			self.size = texture.getSize();

		self.setDepth(10);
