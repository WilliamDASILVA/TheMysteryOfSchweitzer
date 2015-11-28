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
from engine.World import World;
from engine.Camera import Camera;
from engine import Update;
from engine import Global;
from engine import Render;
from engine import Data;
from engine import Input;

from gameplay.Scene import Scene;
from gameplay.Player import Player;
from gameplay.Character import Character;

from gameplay.behaviours import cameraBehaviour;
from gameplay.behaviours import playerBehaviour;
from gameplay.behaviours import actiondispatcherBehaviour;
from gameplay.behaviours import characterBehaviour;
from gameplay.behaviours import sceneBehaviour;

from engine.Input import Keyboard;

from gameplay.ActionReceiver import ActionReceiver;
from engine.render.image import Image;

from gameplay.Dialog import Dialog;
from gameplay.behaviours import dialogBehaviour;

from engine import Debug

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

# debug active
Debug.setActive(True);

# action dispatcher active
actiondispatcherBehaviour.setActive(True);
actiondispatcherBehaviour.assignPlayer(player);

# player behaviours active
playerBehaviour.setPlayer(player);
playerBehaviour.setActive();

# load a scene for test
mainScene = Scene("scene2");
sceneBehaviour.setPlayer(player);
sceneBehaviour.setCurrentScene(mainScene);

characterTest = Character();
mainScene.append(characterTest, 0,0);
characterTest.setPosition(0, mainScene.getGroundPosition(characterTest));

# character behaviour active
characterBehaviour.setActive(True);

# enable dialog system
dialogBehaviour.setActive(True);

dialogTest = Dialog("test");
characterTest.assignDialog(dialogTest);

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