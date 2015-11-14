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

from engine.Input import Keyboard;

from gameplay.ActionReceiver import ActionReceiver;
from engine.render.image import Image;

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

# scene
currentScene = None;

# load a scene for test
currentScene = Scene("scene2");
currentScene.assign(player);
cameraBehaviour.setCameraFixedTo(player);
cameraBehaviour.setScene(currentScene);

def changeScene(state):
	global currentScene;
	if state == "down":

		cameraBehaviour.shakeCamera(2, 2000);
		# currentScene.destroy();
		# currentScene = Scene("lol");
		# cameraBehaviour.setScene(currentScene);
		# currentScene.assign(player);

actiondispatcherBehaviour.assignPlayer(player);

myAction = ActionReceiver("test");
myAction.on(lambda: print("HELLOW WORLD"));

keyboardInput = Keyboard("action");
keyboardInput.on(changeScene);

characterTest = Character();
characterTest.setPosition(0, currentScene.getGroundPosition(characterTest));

characterTest2 = Character("left", 10);
characterTest2.setPosition(300, currentScene.getGroundPosition(characterTest2));

skinTest = Image("assets/characterTest.png");
characterTest2.assignSkin(skinTest);

playerBehaviour.setPlayer(player);
playerBehaviour.setActive();
actiondispatcherBehaviour.setActive(True);

characterBehaviour.setScene(currentScene);
characterBehaviour.setActive(True);


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