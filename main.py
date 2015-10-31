#	--------------------------------------------------- *\
#		Projet ISN - 2015 / 2016
#		William DA SILVA
#		Démarré le 6/10/15
#		License MIT
#
#
#
#		Import modules
#	--------------------------------------------------- */
import pygame;
import imp;
from engine.render.text import Text;
from engine.World import World;
from engine.Camera import Camera;
from engine import Update;
from engine import Global;
from engine import Render;
from engine import Data;
from engine import Input;
from engine.render.image import Image;

from gameplay.Scene import Scene;
from gameplay.Player import Player;

from gameplay.behaviours import cameraBehaviour;
from gameplay.behaviours import playerBehaviour;

from engine.Input import Keyboard;

#	--------------------------------------------------- *\
#		Init the application
#	--------------------------------------------------- */
pygame.init();
pygame.display.init();

Global.screen = pygame.display.set_mode(Global.screenSize, pygame.HWSURFACE);
pygame.display.set_caption(Global.windowTitle);

# world
world = World();

# camera
cam = Camera(world);
Render.setCamera(cam);
cameraBehaviour.setCamera(cam);

# get saved data before game start
Data.getSavedData();

# player element
player = Player();

myScene = Scene("scenetest");
myScene.assign(player);
player.setPosition(0, myScene.getGroundPosition(player));
cameraBehaviour.setCameraFixedTo(myScene);

Render.set(myScene);

playerBehaviour.setPlayer(player);
playerBehaviour.setActive();


#	--------------------------------------------------- *\
#		Main loop
#	--------------------------------------------------- */
while Global.isApplicationRunning:
	event = pygame.event.poll();
	if(event.type == pygame.QUIT):
		Global.isApplicationRunning = False;

	# Keyboard events
	if(event.type == pygame.KEYDOWN):
		for e in Input.events:
			for key in Input.events[e]['keys']:
				if(key == event.key):
					# call functions
					for func in Input.events[e]['functions']:
						func("down");
	elif event.type == pygame.KEYUP:
		for e in Input.events:
			for key in Input.events[e]['keys']:
				if(key == event.key):
					# call functions
					for func in Input.events[e]['functions']:
						func("up");

	Render.onUpdate();
	Update.onUpdate();

pygame.quit();