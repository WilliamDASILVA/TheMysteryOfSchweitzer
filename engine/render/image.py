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
		self.type = "image";
		surface = pygame.image.load(imagePath).convert();
		if surface:
			self.setTexture(surface);
			size = surface.get_size();
			self.setSize(size[0], size[1]);
		else:
			print("Couldn't load the image...");