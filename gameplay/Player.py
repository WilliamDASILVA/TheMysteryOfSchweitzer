from engine.Element import Element;
from engine import Render;
from engine.render.image import Image;
from engine.render.sprite import Sprite;
#	--------------------------------------------------- *\
#		[class] Player()
#
#		* Player element *
#
#	--------------------------------------------------- */
class Player(Element):
	#	--------------------------------------------------- *\
	#		[function] __init__():
	#
	#		* Constructor *
	#	--------------------------------------------------- */
	def __init__(self):
		super().__init__();
		self.setType("player");
		self.assignedScene = None;
		self.speed = 10;

		# assign a drawable for test
		drawable = Sprite("assets/characters/wared/walking.png", 7);
		drawable.setSpeed(12);
		drawable.setSize(256,256);
		self.setDepth(2);
		self.assignDrawable(drawable);

		self.setSize(256,256);

		Render.set(self);

	#	--------------------------------------------------- *\
	#		[function] getSpeed()
	#
	#		* Return the speed of the player *
	#		Return : speed
	#	--------------------------------------------------- */
	def getSpeed(self):
		return self.speed;

	#	--------------------------------------------------- *\
	#		[function] assign(scene)
	#
	#		* Assign a scene to the player *
	#		Return : nil
	#	--------------------------------------------------- */
	def assign(self, scene):
		self.assignedScene = scene;

	#	--------------------------------------------------- *\
	#		[function] getAssignedScene()
	#
	#		* Return the assigned scene *
	#		Return : scene
	#	--------------------------------------------------- */
	def getAssignedScene(self):
		return self.assignedScene;