from engine.Input import Keyboard;


isActive = None;
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
	if (state == "down") and isActive:
		# have dialog?
		if currentDialog != None:
			print(currentDialog.getText(currentIndex));

			currentIndex = nextIndex;
			nextIndex = currentDialog.getNext(currentIndex);

