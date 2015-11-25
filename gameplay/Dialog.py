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
					return self.tree[k][0];

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
					nextIndex = self.tree[k][1]; 

			if nextIndex != None:
				return nextIndex;
			else:
				return "end";