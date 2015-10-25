from threading import Timer;
#	--------------------------------------------------- *\
#		Global module
#	--------------------------------------------------- */
isApplicationRunning = True;
screenSize = width, height = 960, 540;
windowTitle = "The Mystery of Schweitzer";
screen = None;

#	--------------------------------------------------- *\
#		[function] setInterval(functionToCall, milliseconds)
#
#		* Call a function every x milliseconds *
#		Return : nil
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