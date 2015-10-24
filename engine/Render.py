import pygame;
from . import Global;
from .render.drawable import Drawable;
from .render.image import Image;
#	--------------------------------------------------- *\
#		Render module
#	--------------------------------------------------- */
elementsToDraw = [];
functionsToCall = [];

#	--------------------------------------------------- *\
#		[function] on(functionToCall)
#
#		* Call the function when the render is updated *
#		Return : nil
#	--------------------------------------------------- */
def on(functionToCall):
	functionsToCall.append(functionToCall);

#	--------------------------------------------------- *\
#		[function] set(element Drawable)
#
#		* Set the element to the canvas *
#		Return : nil
#	--------------------------------------------------- */
def set(element):
	elementsToDraw.append(element);

#	--------------------------------------------------- *\
#		[function] onUpdate()
#
#		* Function called when we update the canvas *
#		Return : nil
#	--------------------------------------------------- */
def onUpdate():
	# Clean the screen
	Global.screen.fill((0,0,0));

	# Redraw all the elements
	for element in elementsToDraw:
		texture = element.getTexture();
		position = element.getPosition();
		size = element.getSize();

		if((position[0] >= -size[0] and position[0] <= Global.screenSize[0]) and (position[1] >= -size[1] and position[1] <= Global.screenSize[1])):
			# opacity
			texture.set_alpha(element.getOpacity() * 255);
			# scale
			texture = pygame.transform.scale(texture, (size[0],size[1]));
			# rotation
			texture = pygame.transform.rotate(texture, element.getRotation());

			Global.screen.blit(texture, position);

	# Call the functions
	for function in functionsToCall:
		function();

	pygame.display.flip();