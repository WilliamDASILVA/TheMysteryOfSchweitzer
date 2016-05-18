from gameplay.behaviours import playerBehaviour;
from engine.Input import Keyboard;
from engine import Global;
from gameplay import GlobalVars;

isActive = False;
isOpen = False;
usedInterface = None;
keys = {};
buttons  = ['play', 'settings', 'credits', 'quit'];
gameButtons  = ['continue', 'new'];
isGameMenu = False;

#	--------------------------------------------------- *\
#		[function] setActive(value)
#
#		* Set the menu behaviour active *
#		Return : nil
#	--------------------------------------------------- */
def setActive(value):
	global isActive;
	global isOpen;
	global usedInterface;

	isActive = value;

	usedInterface = GlobalVars.getVar("menuInterface");
	usedInterface.setOutside(outsider);

	if value:
		selectItem = Keyboard("action");
		selectItem.on(selectionItem);

		arrowUp = Keyboard("up");
		arrowUp.on(moveSelectionUp2);
		arrowDown = Keyboard("down");
		arrowDown.on(moveSelectionDown2);
		arrowLeft = Keyboard("left");
		arrowLeft.on(closeGameMenu);

#	--------------------------------------------------- *\
#		[function] moveSelectionUp(state)
#
#		* Move the selection up, called from keyboard event *
#		Return : nil
#	--------------------------------------------------- */
def moveSelectionUp2(state):
	if state == "down":
		if isActive and isOpen and (usedInterface != None):

			GlobalVars.getVar("sounds")['bop'].play();

			if not isGameMenu:
				maxItems = usedInterface.getEntry("numberOfItems");
				currentLine = usedInterface.getEntry("currentLine");

				if((currentLine - 1) >= 1):
					usedInterface.setEntry("currentLine", currentLine-1);
				else:
					usedInterface.setEntry("currentLine", maxItems);
			else:
				maxItems = 2;
				currentLine = usedInterface.getEntry("currentGameLine");

				if((currentLine - 1) >= 1):
					usedInterface.setEntry("currentGameLine", currentLine-1);
				else:
					usedInterface.setEntry("currentGameLine", maxItems);

def closeGameMenu(state):
	global isGameMenu;

	if(state == "down"):
		if isActive and isOpen and (usedInterface != None) and isGameMenu:
			isGameMenu = False;
			usedInterface.closeMenu();

#	--------------------------------------------------- *\
#		[function] moveSelectionDown(statz)
#
#		* Called from keyboard event *
#		Return : nil
#	--------------------------------------------------- */
def moveSelectionDown2(state):
	if state == "down":
		if isActive and isOpen and (usedInterface != None):

			GlobalVars.getVar("sounds")['bop'].play();

			if not isGameMenu:
				maxItems = usedInterface.getEntry("numberOfItems");
				currentLine = usedInterface.getEntry("currentLine");
				if((currentLine + 1) <= maxItems):
					usedInterface.setEntry("currentLine", currentLine+1);
				else:
					usedInterface.setEntry("currentLine", 1);
			else:
				maxItems = 2;
				currentLine = usedInterface.getEntry("currentGameLine");
				if((currentLine + 1) <= maxItems):
					usedInterface.setEntry("currentGameLine", currentLine+1);
				else:
					usedInterface.setEntry("currentGameLine", 1);

def assign(button, function):
	keys[button] = function;

	print(keys);

def playMenu():
	pass;

def callAssignedFunction(button):
	for key in keys:
		if(button == key):
			keys[key]();

#	--------------------------------------------------- *\
#		[function] selectionItem()
#
#		* Called from keyboard event *
#		Return : nil
#	--------------------------------------------------- */
def selectionItem(state):
	if state == "down":
		if isActive and isOpen and (usedInterface != None):

			GlobalVars.getVar("sounds")['bop'].play();

			if not isGameMenu:
				currentLine = usedInterface.getEntry("currentLine");
				currentButton = buttons[currentLine-1];

				callAssignedFunction(currentButton);
			else:
				currentLine = usedInterface.getEntry("currentGameLine");
				currentButton = gameButtons[currentLine-1];
				if(currentButton == "continue"):
					if(usedInterface.getEntry("canContinue")):
						callAssignedFunction("continue");
					else:
						print("can't continue");
				else:
					callAssignedFunction(currentButton);



def open():
	global isOpen;
	if isActive and (usedInterface != None):
		if isOpen:
			# close it
			Global.setInterfaceOpen(False);
			usedInterface.delete();
			isOpen = False;
			playerBehaviour.setControlsEnabled(True);
			
			GlobalVars.getVar("sounds")['thunder'].stop();
			GlobalVars.getVar("sounds")['creepy'].stop();
		else:
			# open it
			if not Global.isInterfaceOpen():
				usedInterface.create();
				isOpen = True;
				Global.setInterfaceOpen(True);
				playerBehaviour.setControlsEnabled(False);


def playMenu():
	global isGameMenu;
	if(usedInterface != None):
		isGameMenu = True;
		usedInterface.openMenu();

def setNewGame(value):
	if(usedInterface != None):
		if value:
			value = False;
		else:
			value = True;

		usedInterface.setEntry("canContinue", value);

def outsider():
	GlobalVars.getVar("sounds")['thunder'].play();