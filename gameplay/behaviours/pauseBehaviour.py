from gameplay.behaviours import characterBehaviour;
from gameplay.behaviours import playerBehaviour;
from gameplay.behaviours import sceneBehaviour;
from engine.Input import Keyboard;
from engine import Global;
from gameplay import GlobalVars;
from engine import Render;
from engine import Update;
from engine import Data;
import os;

isActive = False;
isOpen = False;
usedInterface = None;

#	--------------------------------------------------- *\
#		[function] setActive(value)
#
#		* Set the pause behaviour active *
#		Return : nil
#	--------------------------------------------------- */
def setActive(value):
	global isActive;
	global usedInterface;
	isActive = value;

	if value:
		keyboardInput = Keyboard("escape");
		keyboardInput.on(keyboardOpenPause);
		usedInterface = GlobalVars.getVar("pauseInterface");

		selectItem = Keyboard("action");
		selectItem.on(selectionItem);

		arrowUp = Keyboard("up");
		arrowUp.on(moveSelectionUp);
		arrowDown = Keyboard("down");
		arrowDown.on(moveSelectionDown);


#	--------------------------------------------------- *\
#		[function] moveSelectionUp(state)
#
#		* Move the selection up, called from keyboard event *
#		Return : nil
#	--------------------------------------------------- */
def moveSelectionUp(state):
	if state == "down":
		if isActive and isOpen and (usedInterface != None):
			currentLine = usedInterface.getEntry("currentLine");
			if((currentLine - 1) >= 1):
				usedInterface.setEntry("currentLine", currentLine-1);
			else:
				usedInterface.setEntry("currentLine", 2);

#	--------------------------------------------------- *\
#		[function] moveSelectionDown(statz)
#
#		* Called from keyboard event *
#		Return : nil
#	--------------------------------------------------- */
def moveSelectionDown(state):
	if state == "down":
		if isActive and isOpen and (usedInterface != None):
			currentLine = usedInterface.getEntry("currentLine");
			if((currentLine + 1) <= 2):
				usedInterface.setEntry("currentLine", currentLine+1);
			else:
				usedInterface.setEntry("currentLine", 1);

#	--------------------------------------------------- *\
#		[function] selectionItem()
#
#		* Called from keyboard event *
#		Return : nil
#	--------------------------------------------------- */
def selectionItem(state):
	global isOpen;
	if state == "down":
		if isActive and isOpen and (usedInterface != None):
			currentItem = usedInterface.getEntry("currentLine");
			if(currentItem == 1):
				# save the game
				Data.setData("isNewGame", False);
				Data.setData("lastPosition", playerBehaviour.getPlayer().getPosition());
				Data.setData("lastScene", sceneBehaviour.getCurrentScene().getFileName());

				Data.saveData();
				print('Game saved...');

				usedInterface.delete();
				Global.setInterfaceOpen(False);
				playerBehaviour.setControlsEnabled(True);
				isOpen = False;

				characterBehaviour.stopMouvementForAllCharacters(True);

			else:
				os._exit(99);


def keyboardOpenPause(state):
	global isOpen;
	if(state == "down" and isActive):
		if isOpen:
			usedInterface.delete();
			Global.setInterfaceOpen(False);
			playerBehaviour.setControlsEnabled(True);
			isOpen = False;

			characterBehaviour.stopMouvementForAllCharacters(True);
		else:
			if not Global.isInterfaceOpen():
				usedInterface.create();
				isOpen = True;
				Global.setInterfaceOpen(True);
				playerBehaviour.setControlsEnabled(False);
				characterBehaviour.stopMouvementForAllCharacters(False);
