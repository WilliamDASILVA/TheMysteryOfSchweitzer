from engine.Input import Keyboard;
from engine import Update;
from engine import Global;
#	--------------------------------------------------- *\
#		Player behaviour
#	--------------------------------------------------- */

player = None;

#	--------------------------------------------------- *\
#		[function] setActive()
#
#		* Active the player behaviour *
#		Return : nil
#	--------------------------------------------------- */
def setActive():
	leftKey = Keyboard("left");
	leftKey.on(moveLeft);
	rightKey = Keyboard("right");
	rightKey.on(moveRight);

	Update.on(lambda: updatePosition());
	

#	--------------------------------------------------- *\
#		[function] setPlayer(playerElement)
#
#		* Set the behaviour on a specifi player element *
#		Return : nil
#	--------------------------------------------------- */
def setPlayer(playerElement):
	global player;
	player = playerElement;

#	--------------------------------------------------- *\
#		[function] getPlayer()
#
#		* Return the player element used *
#		Return : player
#	--------------------------------------------------- */
def getPlayer():
	return player;

#	--------------------------------------------------- *\
#		Input events
#	--------------------------------------------------- */

isMoving = False;
movingDirection = None;

#	--------------------------------------------------- *\
#		[function] moveLeft()
#
#		* Move the player element to the left *
#		Return : nil
#	--------------------------------------------------- */
def moveLeft(state):
	global isMoving
	global movingDirection;
	if state == "down":
		isMoving = True;
		movingDirection = "left";
	else:
		isMoving = False;

#	--------------------------------------------------- *\
#		[function] moveRight()
#
#		* Move the player element to the right *
#		Return : nil
#	--------------------------------------------------- */
def moveRight(state):
	global isMoving
	global movingDirection;
	if state == "down":
		isMoving = True;
		movingDirection = "right";
	else:
		isMoving = False;
		
#	--------------------------------------------------- *\
#		[function] onUpdate()
#
#		* Updating player's position *
#		Return : nil
#	--------------------------------------------------- */
def updatePosition():
	if isMoving and player:
		position = player.getPosition();
		size = player.getSize();
		k = [position[0], position[1]];

		# check for collisions with the scene before
		scene = player.getAssignedScene();
		sceneSize = scene.getSize();
		scenePosition = scene.getPosition();

		canMoveLeft = True;
		canMoveRight = True;
		if position[0] <= scenePosition[0]:
			canMoveLeft = False;
			canMoveRight = True;

		if position[0] >= scenePosition[0] + sceneSize[0] - size[0]:
			canMoveLeft = True;
			canMoveRight = False;

		if movingDirection == "left" and canMoveLeft:
			k[0] -= player.getSpeed();
		elif movingDirection == "right" and canMoveRight:
			k[0] += player.getSpeed();
		
		player.setPosition(k[0], position[1]);
