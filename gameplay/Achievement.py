from engine import Global;
#	--------------------------------------------------- *\
#		[class] Achievement()
#
#		* Create an achievement element *
#
#	--------------------------------------------------- */
class Achievement():

	def __init__(self, name = None, description = None, functionToCallWhenAchieve = None):
		self.isDone = False;

		self.name = name;
		self.description = description;
		self.functionToCallWhenAchieve = functionToCallWhenAchieve;

	def setName(self, name):
		self.name = name;

	def setDescription(self, description):
		self.description = description;

	def getStatus(self):
		return self.isDone;

	def getName(self):
		return self.name;

	def getDescription(self):
		return self.description;


	# set the achievement done
	def done(self):
		self.isDone = True;
		self.functionToCallWhenAchieve();

