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
		self.texture = None;

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