from engine import Update;
#	--------------------------------------------------- *\
#		Background Behaviour
#	--------------------------------------------------- */

currentPlayer = None;
currentBackground = None;


#	--------------------------------------------------- *\
#		[function] setActive()
#
#		* Active the background's behaviour *
#		Return : nil
#	--------------------------------------------------- */
def setActive(value):
	Update.on(updateBackground);

#	--------------------------------------------------- *\
#		[function] setPlayer(player)
#
#		* Set the used player *
#		Return : nil
#	--------------------------------------------------- */
def setPlayer(player):
	global currentPlayer;
	currentPlayer = player;

#	--------------------------------------------------- *\
#		[function] setBackground(element)
#
#		* Set the current background *
#		Return : nil
#	--------------------------------------------------- */
def setBackground(element):
	global currentBackground;
	currentBackground = element;


#	--------------------------------------------------- *\
#		[function] updateBackground()
#
#		* Update the background position *
#		Return : nil
#	--------------------------------------------------- */
def updateBackground():
	if(currentBackground != None):
		bgPos = currentBackground.getPosition();
		pPos = currentPlayer.getPosition();
		currentBackground.setPosition(-pPos[0] / 5, 0);