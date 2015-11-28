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
		# check if the keyname already exists, if not create a new one
		if not self.name in events:
			events[self.name] = {
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