from engine.Input import Keyboard;
from gameplay.behaviours import playerBehaviour;

isActive = None;
isDialogStarted = False;
currentDialog = None;
currentIndex = 1;
nextIndex = None;

#	--------------------------------------------------- *\
#		[function] setActive(value)
#
#		* Set if the dialog is active or not *
#		Return : nil
#	--------------------------------------------------- */
def setActive(value):
	global isActive;
	isActive = value;

	if value:
		keyboardEvent = Keyboard("action");
		keyboardEvent.on(keyboardInput);

		cancelEvent = Keyboard("escape");
		cancelEvent.on(cancelInput);

#	--------------------------------------------------- *\
#		[function] start()
#
#		* Start the dialog *
#		Return : nil
#	--------------------------------------------------- */
def start():
	global isDialogStarted;
	isDialogStarted = True;
	playerBehaviour.setControlsEnabled(False);
	interface = currentDialog.getAssignedInterface();
	interface.create();

	characterElement = currentDialog.getCharacter();
	characterElement.isWalking(False);


#	--------------------------------------------------- *\
#		[function] stop()
#
#		* Stop the dialog *
#		Return : nil
#	--------------------------------------------------- */
def stop():
	global isDialogStarted;
	global currentDialog;
	global currentIndex;

	playerBehaviour.setControlsEnabled(True);
	isDialogStarted = False;
	currentDialog.setStarted(False);
	interface = currentDialog.getAssignedInterface();
	interface.delete();

	characterElement = currentDialog.getCharacter();
	characterElement.isWalking(True);

	currentDialog = None;
	currentIndex = 1;


#	--------------------------------------------------- *\
#		[function] setDialog(dialog)
#
#		* Set the currend dialog *
#		Return : nil
#	--------------------------------------------------- */
def setDialog(dialog):
	global nextIndex;
	global currentDialog;
	currentDialog = dialog;

	nextIndex = currentDialog.getNext(currentIndex);


#	--------------------------------------------------- *\
#		[function] keyboardInput()
#
#		* Check for actions  *
#		Return : nil
#	--------------------------------------------------- */
def keyboardInput(state):
	global nextIndex;
	global currentIndex;
	if (state == "down") and isActive and isDialogStarted:
		# have dialog?
		if currentDialog != None:
			if currentIndex == "end":
				# close dialog
				stop();
			else:
				interface = currentDialog.getAssignedInterface();
				interface.setEntry("author", currentDialog.getAuthor(currentIndex));
				interface.setEntry("text", currentDialog.getText(currentIndex));

				currentIndex = nextIndex;
				nextIndex = currentDialog.getNext(currentIndex);

#	--------------------------------------------------- *\
#		[function] cancelInput()
#
#		* Cancel the dialog *
#		Return : nil
#	--------------------------------------------------- */
def cancelInput(state):
	if state == "down" and isActive and isDialogStarted:
		stop();