from engine import Global;
from engine.Interface import Interface;

from engine.render.image import Image;
from engine.render.text import Text;
from random import randint;

#	--------------------------------------------------- *\
#		[class] MenuInterface()
#
#		* The pause interface *
#
#	--------------------------------------------------- */
class MenuInterface(Interface):
	#	--------------------------------------------------- *\
	#		[function] __init__()
	#
	#	--------------------------------------------------- */
	def __init__(self):
		super().__init__();
		self.define();

	def editSky(self):
		isFlash = randint(1,3);
		if(isFlash == 2):
			self.elements['sky'].setVisible(False);
			Global.setTimeout(lambda: self.elements['sky'].setVisible(True), 500);

	def define(self):
		sX = Global.screenSize[0];
		sY = Global.screenSize[1];

		self.elements['background'] = Image("assets/homescreen.png");
		self.elements['background'].setPosition(0, 0);
		self.elements['background'].setSize(1*sX, 1*sY);
		self.elements['background'].setDepth(22);

		self.elements['sky'] = Image("assets/sky.png");
		self.elements['sky'].setPosition(0, 0);
		self.elements['sky'].setSize(1*sX, 1*sY);
		self.elements['sky'].setDepth(21);

		self.elements['dot'] = Image("assets/dot.png");
		self.elements['dot'].setPosition(0, 0);
		self.elements['dot'].setSize(1*sX, 1*sY);
		self.elements['dot'].setDepth(20);

		Global.Interval(self.editSky, 3000);

	def create(self):
		sX = Global.screenSize[0];
		sY = Global.screenSize[1];

		super().create();

	def update(self):
		pass;

		