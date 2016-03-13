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

		self.elements['title'] = Text("A test title", "arial");
		self.elements['title'].setPosition(0.1*sX,0.75*sY);
		self.elements['title'].setColor((255,255,255));
		self.elements['title'].setFontSize(40);
		self.elements['title'].setDepth(201);
	
	def create(self):
		sX = Global.screenSize[0];
		sY = Global.screenSize[1];

		self.currentOpacity = 0;

		self.fadeDone = False;
		self.fadeDirection = "in";
		self.fadeInterval = Global.Interval(self.updateOpacity, 100);
		self.functionToCallWhenDone = None;

		super().create();

	def updateOpacity(self):
		if(self.fadeDone == False):
			if(self.fadeDirection == "in"):
				if(self.currentOpacity <= 1):
					self.currentOpacity = self.currentOpacity + 0.05;
				else:
					self.currentOpacity = 1;
					self.fadeDone = True;
					self.fadeInterval.destroy();
					if(self.functionToCallWhenDone != None):
						self.functionToCallWhenDone();
			else:
				if(self.currentOpacity >= 0):
					self.currentOpacity = self.currentOpacity - 0.05;
				else:
					self.currentOpacity = 0;
					self.fadeInterval.destroy();
					self.fadeDone = True;

					self.delete();


		self.elements['background'].setOpacity(self.currentOpacity);
		self.elements['title'].setOpacity(self.currentOpacity);

	def changeFade(self):
		self.fadeDirection = "out";
		self.fadeInterval = Global.Interval(self.updateOpacity, 100);
		self.fadeDone = False;

	def whenDone(self, functionToCall):
		self.functionToCallWhenDone = functionToCall;

	def update(self):
		title = self.getEntry("title");
		self.elements['title'].setValue(title);
