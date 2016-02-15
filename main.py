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
from engine import Cinematic;

from gameplay.Scene import Scene;
from gameplay.Player import Player;
from gameplay.Character import Character;
from gameplay.Inventory import Inventory;
from gameplay.Item import Item;
from gameplay.Background import Background;
from gameplay.Pickup import Pickup;

from gameplay.behaviours import cameraBehaviour;
from gameplay.behaviours import playerBehaviour;
from gameplay.behaviours import actiondispatcherBehaviour;
from gameplay.behaviours import characterBehaviour;
from gameplay.behaviours import sceneBehaviour;
from gameplay.behaviours import inventoryBehaviour;
from gameplay.behaviours import backgroundBehaviour;

from engine.Input import Keyboard;

from gameplay.ActionReceiver import ActionReceiver;
from engine.render.image import Image;

from gameplay.Dialog import Dialog;
from gameplay.behaviours import dialogBehaviour;

from engine import Debug
from interfaces.DialogInterface import DialogInterface;
from interfaces.InventoryInterface import InventoryInterface;
from interfaces.TransitionInterface import TransitionInterface;

from cinematics.TestCinematic import TestCinematic;

from gameplay import GlobalVars;

#	--------------------------------------------------- *\
#		Init the application
#	--------------------------------------------------- */
pygame.init();
pygame.display.init();

Global.screen = pygame.display.set_mode(Global.screenSize, pygame.HWSURFACE);
pygame.display.set_caption(Global.windowTitle);

# global vars
GlobalVars.setActive();

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

# player's inventory
playerInventory = Inventory();
inventoryBehaviour.setActive(True);
inventoryBehaviour.setInventory(playerInventory);

inventoryInterface = InventoryInterface();
inventoryBehaviour.setInterface(inventoryInterface);
def saySomething():
	print("HELLO WORLD!!!!");

myItem = Item("Test", "A test item", "assets/icons/inventory/test.png");
myItem.onSelection(saySomething);


playerInventory.addItem(myItem);
playerInventory.addItem(Item("Un autre truc", "Une description un peu plus longue..", "assets/icons/inventory/test.png"));

# debug active
Debug.setActive(True);

# action dispatcher active
actiondispatcherBehaviour.setActive(True);
actiondispatcherBehaviour.assignPlayer(player);

# player behaviours active
playerBehaviour.setPlayer(player);
playerBehaviour.setActive();

# load a scene for test
sceneBehaviour.setActive();

mainScene = Scene("scene2");
sceneBehaviour.setPlayer(player);
sceneBehaviour.setCurrentScene(mainScene);

# character behaviour active
characterBehaviour.setActive(True);

# enable dialog system
dialogBehaviour.setActive(True);

# background behaviour
backgroundBehaviour.setActive(True);
backgroundBehaviour.setPlayer(player);

testCinema = TestCinematic();
testCinema.start();

#	--------------------------------------------------- *\
#		Main loop
#	--------------------------------------------------- */
while Global.isApplicationRunning:
	Render.onUpdate();
	Update.onUpdate();

	event = pygame.event.poll();
	if(event.type == pygame.QUIT):
		Global.isApplicationRunning = False;
		pygame.quit();

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


