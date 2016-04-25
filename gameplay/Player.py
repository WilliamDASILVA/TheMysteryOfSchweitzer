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
		self.sprites = {
			"walking" : Sprite("assets/characters/muller/walking.png"),
			"static" : Sprite("assets/characters/muller/static.png", 2)
		};

		# sprite settings
		self.sprites['walking'].setSpeed(12);
		self.sprites['walking'].setSize(256, 256);

		self.sprites['static'].setSpeed(1);
		self.sprites['static'].setSize(256, 256);

		self.setDepth(2);
		self.assignDrawable(self.sprites['static']);

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

	#	--------------------------------------------------- *\
	#		[function] useSprite(spriteName)
	#
	#		* Use a specific sprite in the character assets list *
	#	--------------------------------------------------- */
	def useSprite(self, spriteName):
		self.assignedDrawables[0] = self.sprites[spriteName];
		self.setPosition(self.position[0], self.position[1]);
