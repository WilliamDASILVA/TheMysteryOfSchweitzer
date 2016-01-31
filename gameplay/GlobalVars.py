from interfaces.DialogInterface import DialogInterface;
from interfaces.TransitionInterface import TransitionInterface;

gv = None;

def setActive():
	global gv;
	gv = {
		"dialogInterface" : DialogInterface(),
		"transitionInterface" : TransitionInterface()
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