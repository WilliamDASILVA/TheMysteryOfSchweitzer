from engine import Global;
#	--------------------------------------------------- *\
#		[class] ActionReceiver()
#
#		* Receive an action from the ActionDispatcher *
#
#	--------------------------------------------------- */
class ActionReceiver():
	#	--------------------------------------------------- *\
	#		[function] __init__():
	#
	#		* Constructor *
	#	--------------------------------------------------- */
	def __init__(self, receiverID):
		self.id = receiverID;
		self.functionsToCall = [];
		self.isOnZone = False;

		Global.receivers.append(self);

	#	--------------------------------------------------- *\
	#		[function] getID()
	#
	#		* Return the id of the receiver *
	#		Return : id
	#	--------------------------------------------------- */
	def getID(self):
		return self.id;

	#	--------------------------------------------------- *\
	#		[function] onZone(value)
	#
	#		* Set if is on zone *
	#		Return : nil
	#	--------------------------------------------------- */
	def onZone(self, value):
		self.isOnZone = value;

	#	--------------------------------------------------- *\
	#		[function] getOnZone()
	#
	#		* Return if is on zone *
	#		Return : isOnZone
	#	--------------------------------------------------- */
	def getOnZone(self):
		return self.isOnZone;

	#	--------------------------------------------------- *\
	#		[function] getFunctions()
	#
	#		* Return the list of the functions to call *
	#		Return : functions
	#	--------------------------------------------------- */
	def getFunctions(self):
		return self.functionsToCall;

	#	--------------------------------------------------- *\
	#		[function] on()
	#
	#		* Function to call when the action is triggered *
	#		Return : nil
	#	--------------------------------------------------- */
	def on(self, functionToCall):
		self.functionsToCall.append(functionToCall);

	#	--------------------------------------------------- *\
	#		[function] destroy()
	#
	#		* Destroy the dispatcher *
	#		Return : nil
	#	--------------------------------------------------- */
	def destroy(self):
		Global.receivers.remove(self);