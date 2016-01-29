from gameplay.behaviours import cameraBehaviour;
from gameplay.behaviours import characterBehaviour;
import gameplay.Scene;
from interfaces.TransitionInterface import TransitionInterface;

usedScene = None;
usedPlayer = None;
transition = None;
_name = None;
_pos = None;

#	--------------------------------------------------- *\
#		[function] setActive()
#
#		Return : nil
#	--------------------------------------------------- */
def setActive():
	global transition;
	transition = TransitionInterface();

#	--------------------------------------------------- *\
#		[function] getTransition()
#
#		* Return the transition interface *
#		Return : transition
#	--------------------------------------------------- */
def getTransition():
	return transition;

#	--------------------------------------------------- *\
#		[function] setPlayer(player)
#
#		* Set the used player *
#		Return : nil
#	--------------------------------------------------- */
def setPlayer(player):
	global usedPlayer;
	usedPlayer = player;

#	--------------------------------------------------- *\
#		[function] setCurrentScene(scene)
#
#		* Set the scene *
#		Return : nil
#	--------------------------------------------------- */
def setCurrentScene(scene):
	global usedScene;
	usedScene = scene;

	usedScene.assign(usedPlayer);
	cameraBehaviour.setCameraFixedTo(usedPlayer);
	cameraBehaviour.setScene(usedScene);
	characterBehaviour.setScene(usedScene);

	cam = cameraBehaviour.getCamera();

	targetPosition = usedPlayer.getPosition();
	targetSize = usedPlayer.getSize();
	cam.setPosition(targetPosition[0], targetPosition[1] - targetSize[1] * 2);


#	--------------------------------------------------- *\
#		[function] getCurrentScene()
#
#		* Return the current scene *
#		Return : nil
#	--------------------------------------------------- */
def getCurrentScene():
	return usedScene;

#	--------------------------------------------------- *\
#		[function] switchScene(sceneName, targetPosition)
#
#		* Unload the old scene and import the new one *
#		Return : nil
#	--------------------------------------------------- */
def switchScene(sceneName, targetPosition):
	global _name;
	global _pos;
	if usedScene != None:
		transition.create();
		transition.whenDone(transitionDone);
		_name = sceneName;
		_pos = targetPosition;

def transitionDone():
	usedScene.destroy();
	scene = gameplay.Scene.Scene(_name);
	setCurrentScene(scene);
	usedPlayer.setPosition(_pos[0], scene.getGroundPosition(usedPlayer));
