from gameplay.ActionDispatcher import ActionDispatcher;
from gameplay.ActionReceiver import ActionReceiver;
from engine.Element import Element;
from gameplay.behaviours import sceneBehaviour;
from engine.render.image import Image;
from engine import Render;
import uuid;
#	--------------------------------------------------- *\
#		[class] Teleport()
#
#		* Create a teleport to a new scene *
#
#	--------------------------------------------------- */
class Teleport(Element):
	#	--------------------------------------------------- *\
	#		[function] __init__():
	#
	#		* Constructor *
	#	--------------------------------------------------- */
	def __init__(self, position, targetScene, targetPosition):
		super().__init__();
		self.setType("teleportation");
		self.setPosition(position[0], position[1]);

		self.uniqid = uuid.uuid4();
		self.action = ActionDispatcher(self.uniqid, position[0], position[1]);
		self.receiver = ActionReceiver(self.uniqid);
		self.receiver.on(self.doTeleport);

		texture = Image("assets/icons/door.png");
		texture.setSize(64,64);
		texture.setPosition(position[0] + 93, position[1] + 336);
		texture.setDepth(101);
		self.assignDrawable(texture);

		self.targetScene = targetScene;
		self.targetPosition = targetPosition;


		Render.set(texture);
	
	#	--------------------------------------------------- *\
	#		[function] doTeleport()
	#
	#		* Teleport the player where he should be *
	#		Return : nil
	#	--------------------------------------------------- */
	def doTeleport(self):
		sceneBehaviour.switchScene(self.targetScene, self.targetPosition);
		print("TELEPORT" + self.targetScene);


	#	--------------------------------------------------- *\
	#		[function] destroy()
	#
	#		* Destroy the element *
	#		Return : nil
	#	--------------------------------------------------- */
	def destroy(self):
		self.action.destroy();
		self.receiver.destroy();

		for element in self.getAssignedDrawables():
			Render.delete(element);
