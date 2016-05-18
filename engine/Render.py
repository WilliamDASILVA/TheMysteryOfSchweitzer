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
paused = False;

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
#		[function] pause(value)
#
#		* Pause the render drawing *
#		Return : nil
#	--------------------------------------------------- */
def pause(value):
	global paused;
	paused = value;

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
#		[function] delete(element)
#
#		* Remove an element in the canvas *
#		Return : nil
#	--------------------------------------------------- */
def delete(element):
	if element in elementsToDraw:
		elementsToDraw.remove(element);


#	--------------------------------------------------- *\
#		[function] onUpdate()
#
#		* Function called when we update the canvas *
#		Return : nil
#	--------------------------------------------------- */
def onUpdate():
	if not paused:
		# Clean the screen
		Global.screen.fill((0,0,0));

		sX = Global.screenSize[0];
		sY = Global.screenSize[1];
		scale = Global.scale;

		# Redraw all the elements
		elementsToDraw.sort(key=lambda element: element.depth);
		for element in elementsToDraw:
			elements = [];
			if element.getEType() != "drawable":
				elements = element.getAssignedDrawables();
				elements.sort(key=lambda element: element.depth);

			if len(elements) == 0:
				elements.append(element);

			for e in elements:
				if e.isVisible():
					texture = e.getTexture();
					position = e.getPosition();
					size = e.getSize();
					size = round(size[0] * scale), round(size[1] * scale);
					offset = e.getOffsetPosition();

					renderPosition = [position[0] + offset[0], position[1] + offset[1]];

					# camera calculations
					if getCamera() != None and e.getAffectedByCamera() == True:
						camPosition = cameraToUse.getPosition();
						renderPosition[0] = position[0] + (sX/2) - camPosition[0] + offset[0];
						renderPosition[1] = position[1] + (sY/2) - camPosition[1] + offset[1];

					# element is on screen or not
					if((renderPosition[0] >= -size[0] and renderPosition[0] <= sX) and (renderPosition[1] >= -size[1] and renderPosition[1] <= sY)):
						# scale
						if not e.getType() == "sprite":
							texture = pygame.transform.scale(texture, (size[0], size[1]));
						# rotation
						texture = pygame.transform.rotate(texture, e.getRotation());
					

						# text alignement
						if e.getType() == "text":
							align = e.getAlign();
							if align == "center":
								renderPosition[0] = position[0] - (size[0] /2);
							elif align == "right":
								renderPosition[0] = position[0] - size[0];

						crop = None;
						if(e.getType() == "sprite"):
							currentImage = e.getCurrentImage();
							frameSize = e.getFrameSize();
							crop = (frameSize[0] * currentImage, 0, frameSize[0], frameSize[1]);
							newTexture = pygame.Surface((frameSize[0], frameSize[1]), pygame.SRCALPHA);
							newTexture.blit(texture, (0,0), crop);
							newTexture = pygame.transform.scale(newTexture, (size[0],size[1]));
							if(e.getFlip()):
								newTexture = pygame.transform.flip(newTexture, True, False);
								
							if(e.getOpacity() != 1):
								blit_alpha(Global.screen, newTexture, renderPosition, e.getOpacity() * 255);
							else:
								Global.screen.blit(newTexture, renderPosition);

						else:
							if(e.getOpacity() != 1):
								blit_alpha(Global.screen, texture, renderPosition, e.getOpacity() * 255);
							else:
								Global.screen.blit(texture, renderPosition, crop);
								
		# Call the functions
		for function in functionsToCall:
			function();

		pygame.display.flip();

def blit_alpha(target, source, location, opacity):
        x = location[0]
        y = location[1]
        temp = pygame.Surface((source.get_width(), source.get_height())).convert()
        temp.blit(target, (-x, -y))
        temp.blit(source, (0, 0))
        temp.set_alpha(opacity)        
        target.blit(temp, location)