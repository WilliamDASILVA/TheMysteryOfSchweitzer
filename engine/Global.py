from threading import Timer;
#	--------------------------------------------------- *\
#		Global module
#	--------------------------------------------------- */
isApplicationRunning = True;
screenSize = width, height = 960, 540;
windowTitle = "The Mystery of Schweitzer";
screen = None;

dispatchers = [];
receivers = [];


#	--------------------------------------------------- *\
#		[function] getPositionFromScreen(screenX, screenY)
#
#		* Return the position in the World from the screen *
#		Return : position
#	--------------------------------------------------- */
def getPositionFromScreen(screenX, screenY):
	return (screenX, screenY);

#	--------------------------------------------------- *\
#		[function] getPositionFromWorld(worldX, worldY)
#
#		* Return the position in the Screen from the world *
#		Return : position
#	--------------------------------------------------- */
def getPositionFromWorld(worldX, worldY):
	return (worldX, worldY);

#	--------------------------------------------------- *\
#		[function] setInterval(functionToCall, milliseconds)
#
#		* Call a function every x milliseconds *
#		Return : Timer
#	--------------------------------------------------- */
def setInterval(functionToCall, time):
	def wrapper():
		setInterval(functionToCall, time);
		functionToCall();

	t = Timer(time/1000, wrapper);
	t.start();

	return t;

#	--------------------------------------------------- *\
#		[function] destroyInterval(t)
#
#		* Destroy the interval *
#		Return : nil
#	--------------------------------------------------- */
def destroyInterval(interval):
	interval.cancel();

#	--------------------------------------------------- *\
#		[function] setTimeout(functionToCall, milliseconds)
#
#		* Call a function after x milliseconds *
#		Return : Timer
#	--------------------------------------------------- */
def setTimeout(functionToCall, time):
	t = Timer(time/1000, functionToCall);
	t.start();

	return t;