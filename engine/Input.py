from engine import Data;
#	--------------------------------------------------- *\
#		[class] KeyboardInput()
#
#		* Keyboard input class *
#
#	--------------------------------------------------- */
events = {};
class Keyboard():
	#	--------------------------------------------------- *\
	#		[function] __init__():
	#
	#		* Constructor *
	#	--------------------------------------------------- */
	def __init__(self, keyName):
		self.name = keyName;
		self.keys = Data.getData("k_" + keyName);

		global events;
		events[keyName] = {
			"keys" : self.keys,
			"functions" : []
		};
	#	--------------------------------------------------- *\
	#		[function] on(functionToCall)
	#
	#		* Call the function when the event fired *
	#		Return : ni
	#	--------------------------------------------------- */
	def on(self, functionToCall):
		events[self.name]['functions'].append(functionToCall);