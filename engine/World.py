#	--------------------------------------------------- *\
#		[class] World()
#
#		* World class *
#
#	--------------------------------------------------- */
class World():
	#	--------------------------------------------------- *\
	#		[function] __init__():
	#
	#		* Constructor *
	#	--------------------------------------------------- */
	def __init__(self):
		self.origin = [0,0];

	#	--------------------------------------------------- *\
	#		[function] getOrigin()
	#
	#		* Return the origin point of the world *
	#		Return : origin
	#	--------------------------------------------------- */
	def getOrigin(self):
		return self.origin;
