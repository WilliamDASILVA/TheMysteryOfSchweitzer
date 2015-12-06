from engine.render.image import Image;

class Item():
	def __init__(self, name = None, description = None, iconPath = None):
		
		self.setName(name);
		self.setDescription(description);
		self.functionsToCallWhenAction = [];
		self.icon = None;

		# icon
		if iconPath != None:
			drawable = Image(iconPath);
			self.icon = drawable;


	#	--------------------------------------------------- *\
	#		[function] setName(name)
	#
	#		* Set the item's name *
	#		Return : nil
	#	--------------------------------------------------- */
	def setName(self, name):
		self.name = name;

	#	--------------------------------------------------- *\
	#		[function] getName()
	#
	#		* Return the item's name *
	#		Return : name
	#	--------------------------------------------------- */
	def getName(self):
		return self.name;

	#	--------------------------------------------------- *\
	#		[function] setDescription(description)
	#
	#		* Set the item's description *
	#		Return : nil
	#	--------------------------------------------------- */
	def setDescription(self, description):
		self.description = description;

	#	--------------------------------------------------- *\
	#		[function] getDescription()
	#
	#		* Return the description of the item *
	#		Return : description
	#	--------------------------------------------------- */
	def getDescription(self):
		return self.description;

	#	--------------------------------------------------- *\
	#		[function] getIcon()
	#
	#		* Return the icon of the item *
	#		Return : drawable
	#	--------------------------------------------------- */
	def getIcon(self):
		return self.icon;
