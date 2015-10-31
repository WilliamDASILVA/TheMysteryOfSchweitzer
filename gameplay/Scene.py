from engine.Element import Element;
from engine.render.image import Image;
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
	def __init__(self, sceneToLoad):
		super().__init__();
		self.setType("scene");
		if sceneToLoad:
			imageElement = Image("assets/scenes/" + sceneToLoad + ".png");
			if imageElement:
				self.assignDrawable(imageElement);
				self.size = imageElement.getSize();

		self.groundElement = Ground();
		# set the position and size of the ground
		self.groundElement.setSize(self.size[0], self.size[1]);
		self.groundElement.setPosition(0, self.size[1]);

		self.assignedPlayer = None;

	#	--------------------------------------------------- *\
	#		[function] getGroundPosition(playerElement)
	#
	#		* Return the ground position according to the element size *
	#		Return : positionY
	#	--------------------------------------------------- */
	def getGroundPosition(self, playerElement):
		size = self.getSize();
		playerSize = playerElement.getSize();

		return size[1] - playerSize[1];

	#	--------------------------------------------------- *\
	#		[function] assign()
	#
	#		* Assign a player to the scene *
	#		Return : nil
	#	--------------------------------------------------- */
	def assign(self, player):
		self.assignedPlayer = player;
		self.assignedPlayer.assign(self);