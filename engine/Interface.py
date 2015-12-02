#	--------------------------------------------------- *\
#		[class] Interface()
#
#		* Interface element *
#
#	--------------------------------------------------- */
class Interface():
	def __init__(self):
		self.entries = {};
		self.elements = {};

	#	--------------------------------------------------- *\
	#		[function] setEntry(entryName, value)
	#
	#		* Set an entry value *
	#		Return : nil
	#	--------------------------------------------------- */
	def setEntry(self, entryName, entryValue):
		self.entries[entryName] = entryValue;
		self.updateEntries();

	#	--------------------------------------------------- *\
	#		[function] getEntry(entryName)
	#
	#		* Return the entry value *
	#		Return : value
	#	--------------------------------------------------- */
	def getEntry(self, entryName):
		return self.entries[entryName];

	#	--------------------------------------------------- *\
	#		[function] create()
	#
	#		* Create the interface *
	#		Return : nil
	#	--------------------------------------------------- */
	def create(self):
		pass;

	#	--------------------------------------------------- *\
	#		[function] updateEntries()
	#
	#		* Update the entries according to the interface *
	#		Return : nil
	#	--------------------------------------------------- */
	def updateEntries(self):
		for entry in self.entries:
			for element in self.elements:
				if element == entry:
					type = self.elements[element].getType();
					if type == "text":
						text = self.getEntry(element);
						self.elements[element].setValue(text);
