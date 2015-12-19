from gameplay.behaviours import playerBehaviour;
from engine.Input import Keyboard;
from engine import Global;

isActive = False;
isOpen = False;
usedInventory = None;
usedInterface = None;

#	--------------------------------------------------- *\
#		[function] setActive(value)
#
#		* Set the inventory behaviour active *
#		Return : nil
#	--------------------------------------------------- */
def setActive(value):
	global isActive;
	isActive = value;

	if value:
		keyboardInput = Keyboard("inventory");
		keyboardInput.on(keyboardOpenInventory);

		selectItem = Keyboard("action");
		selectItem.on(selectionItem);

		arrowUp = Keyboard("up");
		arrowUp.on(moveSelectionUp);
		arrowDown = Keyboard("down");
		arrowDown.on(moveSelectionDown);

#	--------------------------------------------------- *\
#		[function] setInventory(element)
#
#		* Set the inventory element to use *
#		Return : nil
#	--------------------------------------------------- */
def setInventory(inventoryElement):
	global usedInventory;
	usedInventory = inventoryElement;

#	--------------------------------------------------- *\
#		[function] setInterface(element)
#
#		* Set the interface to use *
#		Return : nil
#	--------------------------------------------------- */
def setInterface(interfaceElement):
	global usedInterface;
	usedInterface = interfaceElement;

#	--------------------------------------------------- *\
#		[function] getInterface()
#
#		* Return the interface used *
#		Return : element
#	--------------------------------------------------- */
def getInterface():
	return usedInterface;

#	--------------------------------------------------- *\
#		[function] moveSelectionUp(state)
#
#		* Move the selection up, called from keyboard event *
#		Return : nil
#	--------------------------------------------------- */
def moveSelectionUp(state):
	if state == "down":
		if isActive and isOpen and (usedInterface != None) and (usedInventory != None):
			maxItems = usedInterface.getEntry("numberOfItems");
			currentLine = usedInterface.getEntry("currentLine");
			if((currentLine - 1) >= 1):
				usedInterface.setEntry("currentLine", currentLine-1);
			else:
				usedInterface.setEntry("currentLine", maxItems);

#	--------------------------------------------------- *\
#		[function] moveSelectionDown(statz)
#
#		* Called from keyboard event *
#		Return : nil
#	--------------------------------------------------- */
def moveSelectionDown(state):
	if state == "down":
		if isActive and isOpen and (usedInterface != None) and (usedInventory != None):
			maxItems = usedInterface.getEntry("numberOfItems");
			currentLine = usedInterface.getEntry("currentLine");
			if((currentLine + 1) <= maxItems):
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
	if state == "down":
		if isActive and isOpen and (usedInterface != None) and (usedInventory != None):
			items = usedInterface.getEntry("items");
			currentItem = usedInterface.getEntry("currentLine");

			i = 1;
			for item in items:
				if currentItem == i:
					item.callFunction();
				i += 1;


#	--------------------------------------------------- *\
#		[function] keyboardOpenInventory()
#
#		* To open the inventory, called from keyboard event *
#		Return : nil
#	--------------------------------------------------- */
def keyboardOpenInventory(state):
	global isOpen;

	if (state == "down") and isActive and (usedInventory != None) and (usedInterface != None):
		if isOpen:
			# close it
			Global.setInterfaceOpen(False);
			usedInterface.delete();
			isOpen = False;
			playerBehaviour.setControlsEnabled(True);
		else:
			# open it
			if not Global.isInterfaceOpen():
				usedInterface.create();
				isOpen = True;
				Global.setInterfaceOpen(True);
				playerBehaviour.setControlsEnabled(False);


