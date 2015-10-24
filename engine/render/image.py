import pygame;
from .drawable import Drawable;
#	--------------------------------------------------- *\
#		[class] Image()
#
#		* Image element *
#
#	--------------------------------------------------- */
class Image(Drawable):
	#	--------------------------------------------------- *\
	#		[function] __init__():
	#
	#		* Constructor *
	#	--------------------------------------------------- */
	def __init__(self, imagePath):
		super().__init__();
		surface = pygame.image.load(imagePath).convert();
		if surface:
			self.setTexture(surface);
		else:
			print("Couldn't load the image...");