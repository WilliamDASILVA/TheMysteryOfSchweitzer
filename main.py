#	--------------------------------------------------- *\
#		Import modules
#	--------------------------------------------------- */
import pygame;
from engine import Global;
from engine import Render;
from engine.render.image import Image;
from engine.render.sprite import Sprite;

#	--------------------------------------------------- *\
#		Init the application
#	--------------------------------------------------- */
pygame.init();
pygame.display.init();

Global.isApplicationRunning = True;
Global.screen = pygame.display.set_mode(Global.screenSize, pygame.HWSURFACE);
pygame.display.set_caption(Global.windowTitle);


while Global.isApplicationRunning:
	event = pygame.event.poll();
	if(event.type == pygame.QUIT):
		Global.isApplicationRunning = False;

	Render.onUpdate();

pygame.quit();