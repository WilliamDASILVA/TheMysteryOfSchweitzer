from engine.Element import Element;
#	--------------------------------------------------- *\
#		[class] Ground()
#
#		* Ground element *
#
#	--------------------------------------------------- */
class Ground(Element):
	#	--------------------------------------------------- *\
	#		[function] __init__():
	#
	#		* Constructor *
	#	--------------------------------------------------- */
	def __init__(self):
		super().__init__();
		self.setType("ground");