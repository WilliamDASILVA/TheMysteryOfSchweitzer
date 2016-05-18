import pygame;
from interfaces.DialogInterface import DialogInterface;
from interfaces.TransitionInterface import TransitionInterface;
from interfaces.PauseInterface import PauseInterface;
from interfaces.MenuInterface import MenuInterface;

gv = None;

def setActive():
	global gv;
	gv = {
		"dialogInterface" : DialogInterface(),
		"transitionInterface" : TransitionInterface(),
		"menuInterface" : MenuInterface(),
		"pauseInterface" : PauseInterface(),
		"sounds" : {
			"thunder" : pygame.mixer.Sound("assets/sounds/ambient_thunder.ogg"),
			"bop" : pygame.mixer.Sound("assets/sounds/bop.ogg"),
			"thunder" : pygame.mixer.Sound("assets/sounds/thunder.ogg"),
			"creepy" : pygame.mixer.Sound("assets/sounds/ambient_creepy.ogg")
		}
	};
	

def setVar(varName, value):
	if varName in gv:
		gv[varName] = value;
	else:
		return None;


def getVar(varName):
	if varName in gv:
		return gv[varName];
	else:
		return None;