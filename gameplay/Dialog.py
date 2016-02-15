import json;
#	--------------------------------------------------- *\
#		[class] Dialog()
#
#		* Start a dialog tree *
#
#	--------------------------------------------------- */
class Dialog():
	#	--------------------------------------------------- *\
	#		[function] __init__():
	#
	#		* Constructor *
	#	--------------------------------------------------- */
	def __init__(self, dialogTree):
		self.file = dialogTree;
		self.tree = None;
		self.started = False;
		self.assignedInterface = None;
		self.character = None;

		# load the dialog tree
		if self.file:
			f = open("assets/dialogs/" + self.file + ".json", "r");
			if f:
				self.tree = json.load(f);
				f.close();

	#	--------------------------------------------------- *\
	#		[function] getText(index)
	#
	#		* Return the text from the index *
	#		Return : text
	#	--------------------------------------------------- */
	def getText(self, index):
		if self.tree != None:
			for k in self.tree:
				if k == str(index):
					return self.tree[k][1];

	#	--------------------------------------------------- *\
	#		[function] getFace(index)
	#
	#		* Return the face from the index *
	#		Return : face
	#	--------------------------------------------------- */
	def getFace(self, index):
		if self.tree != None:
			for k in self.tree:
				if k == str(index):
					return self.tree[k][3];

	#	--------------------------------------------------- *\
	#		[function] getNext(index)
	#
	#		* Return the next text from index *
	#		Return : nextIndex
	#	--------------------------------------------------- */
	def getNext(self,index):
		if self.tree != None:
			nextIndex = None;
			for k in self.tree:
				if k == str(index):
					nextIndex = self.tree[k][2]; 

			if nextIndex != None:
				return nextIndex;
			else:
				return "end";

	#	--------------------------------------------------- *\
	#		[function] getAuthor(ID)
	#
	#		* Return the author of the dialog from the id *
	#		Return : author
	#	--------------------------------------------------- */
	def getAuthor(self, index):
		if self.tree != None:
			for k in self.tree:
				if k == str(index):
					return self.tree[str(index)][0];

	#	--------------------------------------------------- *\
	#		[function] setStarted(value)
	#
	#		* Set if the dialog is started or not *
	#		Return : nil
	#	--------------------------------------------------- */
	def setStarted(self, value):
		self.started = value;

	#	--------------------------------------------------- *\
	#		[function] getStarted()
	#
	#		* Return if the dialog is started or not *
	#		Return : boolean
	#	--------------------------------------------------- */
	def getStarted(self):
		return self.started;

	#	--------------------------------------------------- *\
	#		[function] assignInterface(interface)
	#
	#		* Assign a interface to the dialog *
	#		Return : nil
	#	--------------------------------------------------- */
	def assignInterface(self, dialogInterface):
		self.assignedInterface = dialogInterface;

	#	--------------------------------------------------- *\
	#		[function] getAssignedInterface()
	#
	#		* Returns the assigned interface *
	#		Return : assignedInterface
	#	--------------------------------------------------- */
	def getAssignedInterface(self):
		return self.assignedInterface;

	#	--------------------------------------------------- *\
	#		[function] setCharacter(character)
	#
	#		* Set a character *
	#		Return : nil
	#	--------------------------------------------------- */
	def setCharacter(self, character):
		self.character = character;

	#	--------------------------------------------------- *\
	#		[function] getCharacter()
	#
	#		* Get the assigned character *
	#		Return : character
	#	--------------------------------------------------- */
	def getCharacter(self):
		return self.character;