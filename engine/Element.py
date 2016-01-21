from engine import Global;
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
		self.offset = [0,0];
		self.size = [0,0];
		self.type = None;
		self.depth = 0;
		self.eType = "element";
		self.assignedDrawables = [];

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
	#		[function] setPosition(x, y)
	#
	#		* Set the position of the element in the world *
	#		Return : nil
	#	--------------------------------------------------- */
	def setPosition(self, x, y):
		scale = Global.scale;
		self.position = [x, y];
		for drawable in self.assignedDrawables:
			if drawable.isAffectedByParent():
				drawable.setPosition(x *scale, y *scale);

	#	--------------------------------------------------- *\
	#		[function] setOffsetPosition(x, y)
	#
	#		* Set the offset position *
	#		Return : nil
	#	--------------------------------------------------- */
	def setOffsetPosition(self, x, y):
		scale = Global.scale;
		self.offset = [x *scale, y *scale];

	#	--------------------------------------------------- *\
	#		[function] getPosition()
	#
	#		* Return the position of the element in the world *
	#		Return : position
	#	--------------------------------------------------- */
	def getPosition(self):
		return self.position;

	#	--------------------------------------------------- *\
	#		[function] getOffsetPosition()
	#
	#		* Return the offset position *
	#		Return : offset
	#	--------------------------------------------------- */
	def getOffsetPosition(self):
		return self.offset;

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
		for drawable in self.assignedDrawables:
			drawable.setSize(width, height);

	#	--------------------------------------------------- *\
	#		[function] assignDrawable(drawable)
	#
	#		* Assign a texture (aka drawable) to an element *
	#		Return : nil
	#	--------------------------------------------------- */
	def assignDrawable(self, drawable):
		self.assignedDrawables.append(drawable);

	#	--------------------------------------------------- *\
	#		[function] getAssignedDrawables()
	#
	#		* Return the assigned drawables *
	#		Return : assignedDrawable
	#	--------------------------------------------------- */
	def getAssignedDrawables(self):
		return self.assignedDrawables;

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

	#	--------------------------------------------------- *\
	#		[function] destroy()
	#
	#		* Destroy the element *
	#		Return : nil
	#	--------------------------------------------------- */
	def destroy(self):
		pass;