from threading import Timer;
#	--------------------------------------------------- *\
#		Global module
#	--------------------------------------------------- */
isApplicationRunning = True;
screenSize = width, height = 960, 540;
ratio = screenSize[0]/screenSize[1];
scale = (1/ratio)*(width/530);
windowTitle = "The Mystery of Schweitzer";
screen = None;

dispatchers = [];
receivers = [];

haveInterfaceOpen = False;

def getScreenSize():
	return screenSize;

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
#		[class] Interval(functionToCall, time)
#
#		* Class function for interval, fixing the previous method *
#	--------------------------------------------------- */
class Interval():
	def __init__(self, functionToCall, time):

		self.running = True;
		self.time = time;

		self.timer = None;
		self.timer = Timer(self.time / 1000, self.wrapper);
		self.timer.start();
		self.functionToCall = functionToCall;

	def wrapper(self):
		self.functionToCall();

		if self.timer:
			self.timer.cancel();

			if self.running:
				self.timer = Timer(self.time / 1000, self.wrapper);
				self.timer.start();

	def destroy(self):
		self.running = False;
		self.timer.cancel();

#	--------------------------------------------------- *\
#		[function] setInterval(functionToCall, milliseconds)
#
#		* Call a function every x milliseconds *
#		Return : Timer
#	--------------------------------------------------- */
def setInterval(functionToCall, time):
	def wrapper():
		functionToCall();
		setInterval(functionToCall, time);

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

def isInterfaceOpen():
	return haveInterfaceOpen;

def setInterfaceOpen(value):
	global haveInterfaceOpen;
	haveInterfaceOpen = value;