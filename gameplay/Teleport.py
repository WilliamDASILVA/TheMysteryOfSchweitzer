from gameplay.ActionDispatcher import ActionDispatcher;
from gameplay.ActionReceiver import ActionReceiver;
from engine.Element import Element;
from gameplay.behaviours import sceneBehaviour;
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
		self.setPosition(position[0], position[1]);

		self.uniqid = uuid.uuid4();
		self.action = ActionDispatcher(self.uniqid, position[0], position[1]);
		self.receiver = ActionReceiver(self.uniqid);
		self.receiver.on(self.doTeleport);

		self.targetScene = targetScene;
		self.targetPosition = targetPosition;

	
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