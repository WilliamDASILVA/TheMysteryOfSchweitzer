from engine import Render;
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
		if entryName in self.entries:
			return self.entries[entryName];
		else:
			return False;

	#	--------------------------------------------------- *\
	#		[function] create()
	#
	#		* Create all the defined elements and append to the screen *
	#		Return : nil
	#	--------------------------------------------------- */
	def create(self):
		for element in self.elements:
			self.elements[element].setAffectedByCamera(False);
			Render.set(self.elements[element]);

	#	--------------------------------------------------- *\
	#		[function] update()
	#
	#		* Function called when data is updated *
	#		Return : nil
	#	--------------------------------------------------- */
	def update(self):
		pass;

	#	--------------------------------------------------- *\
	#		[function] delete()
	#
	#		* Destroy all the defined elements and remove from the screen *
	#		Return : nil
	#	--------------------------------------------------- */
	def delete(self):
		for element in self.elements:
			Render.delete(self.elements[element]);

	#	--------------------------------------------------- *\
	#		[function] updateEntries()
	#
	#		* Update the entries according to the interface *
	#		Return : nil
	#	--------------------------------------------------- */
	def updateEntries(self):
		self.update();
		for entry in self.entries:
			for element in self.elements:
				if element == entry:
					type = self.elements[element].getType();
					if type == "text":
						text = self.getEntry(element);
						self.elements[element].setValue(text);
