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
