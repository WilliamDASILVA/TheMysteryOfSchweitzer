from engine import Global;
from engine.Interface import Interface;

from engine.render.image import Image;
from engine.render.text import Text;

#	--------------------------------------------------- *\
#		[class] TransitionInterface()
#
#		* Scene transition interface *
#
#	--------------------------------------------------- */
class TransitionInterface(Interface):
	#	--------------------------------------------------- *\
	#		[function] __init__():
	#
	#		* Constructor *
	#	--------------------------------------------------- */
	def __init__(self):
		super().__init__();
		self.define();
		self.currentOpacity = 0;
		self.fadeInterval = None;
		self.fadeDirection = "in";
		self.fadeDone = False;
		self.functionToCallWhenDone = None;

	def define(self):
		sX = Global.screenSize[0];
		sY = Global.screenSize[1];

		self.elements['background'] = Image("assets/dot.png");
		self.elements['background'].setPosition(0,0);
		self.elements['background'].setSize(sX, sY);
		self.elements['background'].setDepth(200);
		self.elements['background'].setOpacity(0);
	
	def create(self):
		sX = Global.screenSize[0];
		sY = Global.screenSize[1];

		self.currentOpacity = 0;

		self.fadeDone = False;
		self.fadeDirection = "in";
		self.fadeInterval = Global.setInterval(self.updateOpacity, 200);
		self.functionToCallWhenDone = None;

		super().create();

	def updateOpacity(self):
		if(self.fadeDone == False):
			if(self.fadeDirection == "in"):
				if(self.currentOpacity < 1):
					self.currentOpacity += 0.05;
				else:
					self.currentOpacity = 1;
					Global.destroyInterval(self.fadeInterval);
					self.fadeDone = True;
					if(self.functionToCallWhenDone != None):
						self.functionToCallWhenDone();
			else:
				if(self.currentOpacity > 0):
					self.currentOpacity -= 0.05;
				else:
					self.currentOpacity = 0;
					Global.destroyInterval(self.fadeInterval);
					self.fadeDone = True;
					self.delete();
					
		self.elements['background'].setOpacity(round(self.currentOpacity));

	def changeFade(self):
		self.fadeDirection = "out";
		self.fadeInterval = Global.setInterval(self.updateOpacity, 100);
		self.fadeDone = False;

	def whenDone(self, functionToCall):
		self.functionToCallWhenDone = functionToCall;

	def update(self):
		pass;		
