from engine import Global;
from engine.Interface import Interface;

from engine.render.image import Image;
from engine.render.text import Text;
from engine.render.sprite import Sprite;

#	--------------------------------------------------- *\
#		[class] DialogInterface()
#
#		* The dialog interface *
#
#	--------------------------------------------------- */
class DialogInterface(Interface):
	#	--------------------------------------------------- *\
	#		[function] __init__()
	#
	#	--------------------------------------------------- */
	def __init__(self):
		super().__init__();
		self.define();

		print(self.elements);

	#	--------------------------------------------------- *\
	#		[function] define()
	#
	#		* Define the elements *
	#		Return : nil
	#	--------------------------------------------------- */
	def define(self):
		sX = Global.screenSize[0];
		sY = Global.screenSize[1];

		self.elements['background'] = Image("assets/darker.png");
		self.elements['background'].setPosition(0, sY/2);
		self.elements['background'].setSize(sX, sY/2);

		self.elements['characterFace'] = Image("assets/characters/test/face.png");
		self.elements['characterFace'].setPosition(0.05*sX, 0.78 * sY);
		self.elements['characterFace'].setSize(0.1*sX, 0.1*sX);
		self.elements['characterFace'].setDepth(5);

		self.elements['author'] = Text("None", "arial");
		self.elements['author'].setPosition(0.2*sX,0.82*sY);
		self.elements['author'].setColor((255,255,255));
		self.elements['author'].setFontSize(20);
		self.elements['author'].setDepth(5);

		self.elements['text'] = Text("None", "arial");
		self.elements['text'].setPosition(0.2*sX,0.87*sY);
		self.elements['text'].setColor((255,255,255));
		self.elements['text'].setFontSize(16);
		self.elements['text'].setDepth(5);

		self.elements['help'] = Text("( Press 'Enter' to skip )", "arial");
		self.elements['help'].setPosition(0.2*sX,0.92*sY);
		self.elements['help'].setColor((200,200,200));
		self.elements['help'].setFontSize(12);
		self.elements['help'].setDepth(5);
