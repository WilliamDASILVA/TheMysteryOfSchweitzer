from engine import Global;
from engine import Update;
from engine.Input import Keyboard;


usedPlayer = None;
isActive = False;

#	--------------------------------------------------- *\
#		[function] assignPlayer(player)
#
#		* Assign a player for actions *
#		Return : nil
#	--------------------------------------------------- */
def assignPlayer(player):
	global usedPlayer;
	usedPlayer = player;

#	--------------------------------------------------- *\
#		[function] setActive(value)
#
#		* Set if the actionDispatcherBehavour is active or not *
#		Return : nil
#	--------------------------------------------------- */
def setActive(value):
	global isActive;
	isActive = value;

	keyboardEvent = Keyboard("action");
	keyboardEvent.on(actionKeyboard);


#	--------------------------------------------------- *\
#		[function] actionKeyboard()
#
#		* Function called when the user press action key *
#		Return : nil
#	--------------------------------------------------- */
def actionKeyboard(state):
	if state == "down":
		for receiver in Global.receivers:
			for dispatcher in Global.dispatchers:
				if receiver.getID() == dispatcher.getID() and dispatcher.getIsOnZone() == True:
					for function in receiver.getFunctions():
						function();


#	--------------------------------------------------- *\
#		On update
#	--------------------------------------------------- */
def checkForAction():
	if usedPlayer and isActive:
		position = usedPlayer.getPosition();
		for action in Global.dispatchers:
			actionPosition = action.getPosition();
			actionSize = action.getSize();

			if (position[0] >= actionPosition[0]) and (position[0] <= actionPosition[0] + actionSize[0]):
				action.setIsOnZone(True);
			else:
				action.setIsOnZone(False);


Update.on(checkForAction);