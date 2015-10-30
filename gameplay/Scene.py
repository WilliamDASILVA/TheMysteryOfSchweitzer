from engine.Element import Element;
from gameplay.Ground import Ground;
#	--------------------------------------------------- *\
#		[class] Scene()
#
#		* Scene element *
#
#	--------------------------------------------------- */
class Scene(Element):
	#	--------------------------------------------------- *\
	#		[function] __init__():
	#
	#		* Constructor *
	#	--------------------------------------------------- */
	def __init__(self, imageElement):
		super().__init__();
		self.setType("scene");
		if imageElement:
			self.assignDrawable(imageElement);
			self.size = imageElement.getSize();

		self.groundElement = Ground();
		# set the position and size of the ground
		self.groundElement.setSize(self.size[0], self.size[1]);
		self.groundElement.setPosition(0, self.size[1]);
