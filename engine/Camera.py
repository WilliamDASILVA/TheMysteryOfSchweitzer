#	--------------------------------------------------- *\
#		[class] Camera()
#
#		* Camera element *
#
#	--------------------------------------------------- */
class Camera():
	#	--------------------------------------------------- *\
	#		[function] __init__():
	#
	#		* Constructor *
	#	--------------------------------------------------- */
	def __init__(self, world):
		self.position = [0,0];
		self.parentWorld = world;


	#	--------------------------------------------------- *\
	#		[function] setPosition()
	#
	#		* Set the position of the camera in the world *
	#		Return : nil
	#	--------------------------------------------------- */
	def setPosition(self, x, y):
		origin = self.parentWorld.getOrigin();
		self.position = [origin[0] + x, origin[1] + y];

	#	--------------------------------------------------- *\
	#		[function] getPosition()
	#
	#		* Return the position of the camera in the world *
	#		Return : position
	#	--------------------------------------------------- */
	def getPosition(self):
		return self.position;