from engine.Element import Element;
from engine import Global;
#	--------------------------------------------------- *\
#		[class] ActionDispatcher()
#
#		* Create an action dispatcher *
#
#	--------------------------------------------------- */
class ActionDispatcher(Element):
	#	--------------------------------------------------- *\
	#		[function] __init__():
	#
	#		* Constructor *
	#	--------------------------------------------------- */
	def __init__(self, dispatcherID, x, y):
		super().__init__();
		self.isOnZone = False;
		self.id = dispatcherID;
		self.setPosition(x, y);
		self.setSize(250,400);

		self.functionsToCallWhenZone = [];

		Global.dispatchers.append(self);

	#	--------------------------------------------------- *\
	#		[function] getID()
	#
	#		* Return the id of the action dispatcher *
	#		Return : id
	#	--------------------------------------------------- */
	def getID(self):
		return self.id;

	#	--------------------------------------------------- *\
	#		[function] setIsOnZone(value)
	#
	#		* Set if something is on zone *
	#		Return : nil
	#	--------------------------------------------------- */
	def setIsOnZone(self, value):
		self.isOnZone = value;
		if value:
			for function in self.functionsToCallWhenZone:
				function();

	#	--------------------------------------------------- *\
	#		[function] getIsOnZone()
	#
	#		* Return if something is on the zone *
	#		Return : boolean
	#	--------------------------------------------------- */
	def getIsOnZone(self):
		return self.isOnZone;

	#	--------------------------------------------------- *\
	#		[function] destroy()
	#
	#		* Destroy the dispatcher *
	#		Return : nil
	#	--------------------------------------------------- */
	def destroy(self):
		Global.dispatchers.remove(self);

	#	--------------------------------------------------- *\
	#		[function] onZone(functionToCall)
	#
	#		* Call the function every time something is on the zone *
	#		Return : nil
	#	--------------------------------------------------- */
	def onZone(self, functionToCall):
		self.functionsToCallWhenZone.append(functionToCall);