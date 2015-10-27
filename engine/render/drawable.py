#	--------------------------------------------------- *\
#		[class] Drawable()
#
#		* A drawable element *
#
#	--------------------------------------------------- */
class Drawable:
	#	--------------------------------------------------- *\
	#		[function] __init__():
	#
	#		* Constructor *
	#	--------------------------------------------------- */
	def __init__(self):
		self.position = [0,0];
		self.size = [0,0];
		self.opacity = 1;
		self.rotation = 0;
		self.type = None;
		self.texture = None;
		self.crop = None;
		self.affectedByCamera = True;

	#	--------------------------------------------------- *\
	#		[function] getPosition()
	#
	#		* Return the position of the element *
	#		Return : array
	#	--------------------------------------------------- */
	def getPosition(self):
		return self.position;

	#	--------------------------------------------------- *\
	#		[function] setPosition(x, y)
	#
	#		* Set the position of an element *
	#		Return : nil
	#	--------------------------------------------------- */
	def setPosition(self, x, y):
		self.position = [x, y];

	#	--------------------------------------------------- *\
	#		[function] setOpacity(opacity)
	#
	#		* Set the opacity of an element *
	#		Return : nil
	#	--------------------------------------------------- */
	def setOpacity(self, opacity):
		self.opacity = opacity;

	#	--------------------------------------------------- *\
	#		[function] getOpacity()
	#
	#		* Return the opacity of an element *
	#		Return : opacity
	#	--------------------------------------------------- */
	def getOpacity(self):
		return self.opacity;

	#	--------------------------------------------------- *\
	#		[function] setSize(width, height)
	#
	#		* Set the size of an element *
	#		Return : nil
	#	--------------------------------------------------- */
	def setSize(self, width, height):
		self.size = [width, height];

	#	--------------------------------------------------- *\
	#		[function] getSize()
	#
	#		* Return the size of an element *
	#		Return : array
	#	--------------------------------------------------- */
	def getSize(self):
		return self.size;

	#	--------------------------------------------------- *\
	#		[function] setTexture(texture)
	#
	#		* Set the texture of the drawable *
	#		Return : nil
	#	--------------------------------------------------- */
	def setTexture(self, texture):
		self.texture = texture;

	#	--------------------------------------------------- *\
	#		[function] getTexture()
	#
	#		* Return the texture of the drawable *
	#		Return : texture
	#	--------------------------------------------------- */
	def getTexture(self):
		return self.texture;

	#	--------------------------------------------------- *\
	#		[function] setRotation(angle)
	#
	#		* Set the rotation of the drawable *
	#		Return : nil
	#	--------------------------------------------------- */
	def setRotation(self, angle):
		self.rotation = angle;

	#	--------------------------------------------------- *\
	#		[function] getRotation()
	#
	#		* Return the rotation of the drawable *
	#		Return : rotation
	#	--------------------------------------------------- */
	def getRotation(self):
		return self.rotation;

	#	--------------------------------------------------- *\
	#		[function] getCrop()
	#
	#		* Return the cropped area *
	#		Return : tuple
	#	--------------------------------------------------- */
	def getCrop(self):
		return self.crop;

	#	--------------------------------------------------- *\
	#		[function] setCrop(x, y, width, height)
	#
	#		* Set the cropped area *
	#		Return : nil
	#	--------------------------------------------------- */
	def setCrop(self, x, y, width, height):
		self.crop = (x, y, width, height);

	#	--------------------------------------------------- *\
	#		[function] getType()
	#
	#		* Return the type of the drawable *
	#		Return : type
	#	--------------------------------------------------- */
	def getType(self):
		return self.type;

	#	--------------------------------------------------- *\
	#		[function] getAffectedByCamera()
	#
	#		* Return if the element positionning is affected by the camera *
	#		Return : true, false
	#	--------------------------------------------------- */
	def getAffectedByCamera(self):
		return self.affectedByCamera;

	#	--------------------------------------------------- *\
	#		[function] setAffectedByCamera(value)
	#
	#		* Set if the element should be affected by the camera or not *
	#		Return : nil
	#	--------------------------------------------------- */
	def setAffectedByCamera(self, value):
		self.affectedByCamera = value;