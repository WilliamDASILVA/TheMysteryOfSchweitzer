from engine.render.text import Text;
from engine import Render;
from engine.Input import Keyboard;

isActive = False;
currentLine = 0;
lines = [];

#	--------------------------------------------------- *\
#		[function] setActive(value)
#
#		* Set active the debug mode *
#		Return : nil
#	--------------------------------------------------- */
def setActive(value):
	global isActive;
	isActive = value;

	keyboardAction = Keyboard("escape");
	keyboardAction.on(doClear);

#	--------------------------------------------------- *\
#		[function] output(text)
#
#		* Output a text in the screen *
#		Return : nil
#	--------------------------------------------------- */
def output(text):
	global currentLine;

	textElement = Text(text, "arial");
	textElement.setPosition(20, 20 + currentLine * 20);
	textElement.setAffectedByCamera(False);
	Render.set(textElement);
	lines.append(textElement);

	currentLine += 1;


#	--------------------------------------------------- *\
#		[function] clear()
#
#		* Clear the debug *
#		Return : nil
#	--------------------------------------------------- */
def clear():
	global lines;
	for line in lines:
		Render.delete(line);

	lines = [];

#	--------------------------------------------------- *\
#		[function] doClear()
#
#		Return : nil
#	--------------------------------------------------- */
def doClear(state):
	if state == "down" and isActive:
		clear();
