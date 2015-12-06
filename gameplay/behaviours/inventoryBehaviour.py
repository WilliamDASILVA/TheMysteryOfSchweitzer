from engine.Input import Keyboard;
from engine import Global;

isActive = False;
isOpen = False;
usedInventory = None;
usedInterface = None;

def setActive(value):
	global isActive;
	isActive = value;

	if value:
		keyboardInput = Keyboard("inventory");
		keyboardInput.on(keyboardOpenInventory);

		arrowUp = Keyboard("up");
		arrowUp.on(moveSelectionUp);
		arrowDown = Keyboard("down");
		arrowDown.on(moveSelectionDown);


def setInventory(inventoryElement):
	global usedInventory;
	usedInventory = inventoryElement;

def setInterface(interfaceElement):
	global usedInterface;
	usedInterface = interfaceElement;

def getInterface():
	return usedInterface;

def moveSelectionUp(state):
	if state == "down":
		if isActive and isOpen and (usedInterface != None) and (usedInventory != None):
			print("MOVE UP");

def moveSelectionDown(state):
	if state == "down":
		if isActive and isOpen and (usedInterface != None) and (usedInventory != None):
			print("MOVE DOWN");


def keyboardOpenInventory(state):
	global isOpen;

	if (state == "down") and isActive and (usedInventory != None) and (usedInterface != None):
		if isOpen:
			# close it
			Global.setInterfaceOpen(False);
			usedInterface.delete();
			isOpen = False;
		else:
			# open it
			if not Global.isInterfaceOpen():
				usedInterface.create();
				isOpen = True;
				Global.setInterfaceOpen(True);


