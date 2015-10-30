from engine.Element import Element;
from engine.render.image import Image;
from engine import Render;
#	--------------------------------------------------- *\
#		[class] Ground()
#
#		* Ground physic element *
#
#	--------------------------------------------------- */
class Ground(Element):
	#	--------------------------------------------------- *\
	#		[function] __init__():
	#
	#		* Constructor *
	#	--------------------------------------------------- */
	def __init__(self):
		super().__init__();
		self.setType("ground");
		drawable = Image("assets/dickbutt.png");
		self.assignDrawable(drawable);
		self.setSize(500,500);
		self.setPosition(0,0);

		Render.set(drawable);