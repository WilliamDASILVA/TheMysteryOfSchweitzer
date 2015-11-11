#	--------------------------------------------------- *\
#		[class] Element()
#
#		* Element class *
#
#	--------------------------------------------------- */
class Element():
	#	--------------------------------------------------- *\
	#		[function] __init__():
	#
	#		* Constructor *
	#	--------------------------------------------------- */
	def __init__(self):
		self.position = [0,0];
		self.size = [0,0];
		self.type = None;
		self.depth = 0;
		self.eType = "element";
		self.assignedDrawable = None;

	#	--------------------------------------------------- *\
	#		[function] getEType()
	#
	#		* Return the EType *
	#		Return : eType
	#	--------------------------------------------------- */
	def getEType(self):
		return self.eType;

	#	--------------------------------------------------- *\
	#		[function] setType(type)
	#
	#		* Set the type of the element *
	#		Return : nil
	#	--------------------------------------------------- */
	def setType(self, t):
		self.type = t;

	#	--------------------------------------------------- *\
	#		[function] getType()
	#
	#		* Return the type of the element *
	#		Return : type
	#	--------------------------------------------------- */
	def getType(self):
		return self.type;


	#	--------------------------------------------------- *\
	#		[function] setPosition()
	#
	#		* Set the position of the element in the world *
	#		Return : nil
	#	--------------------------------------------------- */
	def setPosition(self, x, y):
		self.position = [x, y];
		if self.assignedDrawable:
			self.assignedDrawable.setPosition(x, y);

	#	--------------------------------------------------- *\
	#		[function] getPosition()
	#
	#		* Return the position of the element in the world *
	#		Return : position
	#	--------------------------------------------------- */
	def getPosition(self):
		return self.position;

	#	--------------------------------------------------- *\
	#		[function] getSize()
	#
	#		* Return the size of the element *
	#		Return : size
	#	--------------------------------------------------- */
	def getSize(self):
		return self.size;

	#	--------------------------------------------------- *\
	#		[function] setSize(width, height)
	#
	#		* Set the size of the element *
	#		Return : nil
	#	--------------------------------------------------- */
	def setSize(self, width, height):
		self.size = [width, height];
		if self.assignedDrawable:
			self.assignedDrawable.setSize(width, height);

	#	--------------------------------------------------- *\
	#		[function] assignDrawable(drawable)
	#
	#		* Assign a texture (aka drawable) to an element *
	#		Return : nil
	#	--------------------------------------------------- */
	def assignDrawable(self, drawable):
		self.assignedDrawable = drawable;

	#	--------------------------------------------------- *\
	#		[function] getAssignedDrawable()
	#
	#		* Return the assigned drawable *
	#		Return : assignedDrawable
	#	--------------------------------------------------- */
	def getAssignedDrawable(self):
		return self.assignedDrawable;

	#	--------------------------------------------------- *\
	#		[function] setDepth(depth)
	#
	#		* Set the depth field of an element *
	#		Return : nil
	#	--------------------------------------------------- */
	def setDepth(self, depth):
		self.depth = depth;
		
	#	--------------------------------------------------- *\
	#		[function] getDepth()
	#
	#		* Return the depth field of an element *
	#		Return : depth
	#	--------------------------------------------------- */
	def getDepth(self):
		return self.depth;
