from engine.Element import Element;
#	--------------------------------------------------- *\
#		[class] Drawable()
#
#		* A drawable element *
#
#	--------------------------------------------------- */
class Drawable(Element):
	#	--------------------------------------------------- *\
	#		[function] __init__():
	#
	#		* Constructor *
	#	--------------------------------------------------- */
	def __init__(self):
		super().__init__();

		self.opacity = 1;
		self.rotation = 0;
		self.eType = "drawable";
		self.texture = None;
		self.crop = None;
		self.depth = 0;
		self.affectedByCamera = True;
		self.visible = True;

	#	--------------------------------------------------- *\
	#		[function] setVisible(value)
	#
	#		* Set if the element should be visible *
	#		Return : nil
	#	--------------------------------------------------- */
	def setVisible(self, value):
		self.visible = value;

	#	--------------------------------------------------- *\
	#		[function] isVisible()
	#
	#		* Return if the element is visible or not *
	#		Return : boolean
	#	--------------------------------------------------- */
	def isVisible(self):
		return self.visible;

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
