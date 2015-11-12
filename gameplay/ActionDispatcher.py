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
		self.id = dispatcherID;
		self.setPosition(x, y);
		self.setSize(250,400);

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
	#		[function] destroy()
	#
	#		* Destroy the dispatcher *
	#		Return : nil
	#	--------------------------------------------------- */
	def destroy(self):
		Global.dispatchers.remove(self);
