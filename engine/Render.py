import pygame;
from . import Global;
from .render.drawable import Drawable;
from .render.image import Image;
#	--------------------------------------------------- *\
#		Render module
#	--------------------------------------------------- */
elementsToDraw = [];
functionsToCall = [];
cameraToUse = None;

#	--------------------------------------------------- *\
#		[function] setCamera(camera)
#
#		* Use a specific camera *
#		Return : nil
#	--------------------------------------------------- */
def setCamera(camera):
	global cameraToUse
	cameraToUse = camera;


#	--------------------------------------------------- *\
#		[function] getCamera()
#
#		* Return camera *
#		Return : cam
#	--------------------------------------------------- */
def getCamera():
	return cameraToUse;

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

	sX = Global.screenSize[0];
	sY = Global.screenSize[1];

	# Redraw all the elements
	for element in elementsToDraw:
		texture = element.getTexture();
		position = element.getPosition();
		size = element.getSize();

		renderPosition = [position[0], position[1]];

		# camera calculations
		if getCamera() != None and element.getAffectedByCamera() == True:
			camPosition = cameraToUse.getPosition();
			renderPosition[0] = position[0] + (sX/2) - camPosition[0];
			renderPosition[1] = position[1] + (sY/2) - camPosition[1];


		if((position[0] >= -size[0] and position[0] <= Global.screenSize[0]) and (position[1] >= -size[1] and position[1] <= Global.screenSize[1])):
			# opacity
			texture.set_alpha(element.getOpacity() * 255);
			# scale
			if not element.getType() == "sprite":
				texture = pygame.transform.scale(texture, (size[0],size[1]));
			# rotation
			texture = pygame.transform.rotate(texture, element.getRotation());
		

			# text alignement
			if element.getType() == "text":
				align = element.getAlign();
				if align == "center":
					renderPosition[0] = position[0] - (size[0] /2);
				elif align == "right":
					renderPosition[0] = position[0] - size[0];

			crop = None;
			if(element.getType() == "sprite"):
				currentImage = element.getCurrentImage();
				frameSize = element.getFrameSize();
				crop = (frameSize[0] * currentImage, 0, frameSize[0], frameSize[1]);
				newTexture = pygame.Surface((frameSize[0], frameSize[1]), pygame.HWSURFACE);

				newTexture.blit(texture, (0,0), crop);
				newTexture = pygame.transform.scale(newTexture, (size[0],size[1]));

				Global.screen.blit(newTexture, position);
			else:
				Global.screen.blit(texture, renderPosition, crop);

	# Call the functions
	for function in functionsToCall:
		function();

	pygame.display.flip();