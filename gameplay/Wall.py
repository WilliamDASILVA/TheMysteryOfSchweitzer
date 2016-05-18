from engine.Element import Element;
from engine.render.image import Image;
#	--------------------------------------------------- *\
#		[class] Wall()
#
#		* Create a wall *
#
#	--------------------------------------------------- */
class Wall(Element):
	#	--------------------------------------------------- *\
	#		[function] __init__():
	#
	#		* Constructor *
	#	--------------------------------------------------- */
	def __init__(self, category, x, y):
		super().__init__();
		self.category = category;
		self.setPosition(x, y);

		# add texture to the wall
		texture = Image("assets/elements/wall/" + category + ".png");
		if texture:
			self.assignDrawable(texture);
			self.size = texture.getSize();