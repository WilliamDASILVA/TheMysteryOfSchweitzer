from engine import Global;
from engine.Interface import Interface;

from engine.render.image import Image;
from engine.render.text import Text;
from engine.render.sprite import Sprite;

#	--------------------------------------------------- *\
#		[class] InventoryInterface()
#
#		* The inventory interface *
#
#	--------------------------------------------------- */
class InventoryInterface(Interface):
	#	--------------------------------------------------- *\
	#		[function] __init__()
	#
	#	--------------------------------------------------- */
	def __init__(self):
		super().__init__();
		self.define();

	def define(self):
		sX = Global.screenSize[0];
		sY = Global.screenSize[1];

		self.elements['background'] = Image("assets/darker.png");
		self.elements['background'].setPosition(0.1*sX, 0.3*sY);
		self.elements['background'].setSize(0.8*sX, 0.7*sY);

		self.elements['face'] = Image("assets/characterTest.png");
		self.elements['face'].setPosition(0.1*sX, 0.15*sY);
		self.elements['face'].setSize(0.1*sX, 0.1*sX);

		self.elements['title'] = Text("Inventaire", "arial");
		self.elements['title'].setFontSize(30);
		self.elements['title'].setDepth(3);
		self.elements['title'].setPosition(0.22*sX, 0.15*sY);

		self.elements['description1'] = Text("Tous les items que vous avez récoltés au cours de votre aventure.", "arial");
		self.elements['description1'].setFontSize(18);
		self.elements['description1'].setColor((230,230,230));
		self.elements['description1'].setDepth(3);
		self.elements['description1'].setPosition(0.22*sX, 0.21*sY);

		self.elements['description2'] = Text("( Appuyez sur 'F' pour ouvrir / fermer l'inventaire )", "arial");
		self.elements['description2'].setFontSize(15);
		self.elements['description2'].setColor((230,230,230));
		self.elements['description2'].setDepth(3);
		self.elements['description2'].setPosition(0.22*sX, 0.25*sY);


	def create(self):
		sX = Global.screenSize[0];
		sY = Global.screenSize[1];

		items = self.getEntry("items");
		i = 0;
		for item in items:
			name = item.getName();
			description = item.getDescription();

			self.elements[name+'face'] = item.getIcon();
			self.elements[name+'face'].setPosition(0.12*sX, 0.4*sY + (0.075*sX) * i);
			self.elements[name+'face'].setSize(0.06*sX, 0.06*sX);
			self.elements[name+'face'].setDepth(4);

			self.elements[name+'darker'] = Image("assets/darker2.png");
			self.elements[name+'darker'].setPosition(0.11*sX, 0.39*sY  + (0.075*sX) * i);
			self.elements[name+'darker'].setSize(0.78*sX, 0.075*sX);
			self.elements[name+'darker'].setDepth(3);

			self.elements[name+'name'] = Text(name, "arial");
			self.elements[name+'name'].setFontSize(20);
			self.elements[name+'name'].setDepth(4);
			self.elements[name+'name'].setPosition(0.2*sX, 0.4*sY  + (0.075*sX) * i);

			self.elements[name+'description'] = Text(description, "arial");
			self.elements[name+'description'].setFontSize(15);
			self.elements[name+'description'].setDepth(4);
			self.elements[name+'description'].setPosition(0.2*sX, 0.45*sY  + (0.075*sX) * i);
			i += 1;


		super().create();