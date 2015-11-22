from gameplay.behaviours import cameraBehaviour;
from gameplay.behaviours import characterBehaviour;
import gameplay.Scene;

usedScene = None;
usedPlayer = None;

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
	if usedScene != None:
		usedScene.destroy();

		scene = gameplay.Scene.Scene(sceneName);
		setCurrentScene(scene);
		usedPlayer.setPosition(targetPosition[0], scene.getGroundPosition(usedPlayer));

		print("SCENE DESTROYED");