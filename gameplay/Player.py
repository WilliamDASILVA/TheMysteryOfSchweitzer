from engine.Element import Element;
from engine import Render;
from engine.render.image import Image;
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
		self.speed = 5; # 2 pixels per second

		# assign a drawable for test
		drawable = Image("assets/characterTest.png");
		drawable.setSize(64,64);
		self.setDepth(100);
		self.assignDrawable(drawable);

		self.setSize(64,64);

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