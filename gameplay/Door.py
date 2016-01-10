from gameplay.Teleport import Teleport;
from engine.Element import Element;
from engine.render.image import Image;
from engine.render.text import Text;
#	--------------------------------------------------- *\
#		[class] Door()
#
#		* Create a door *
#
#	--------------------------------------------------- */
class Door(Element):
	#	--------------------------------------------------- *\
	#		[function] __init__():
	#
	#		* Constructor *
	#	--------------------------------------------------- */
	def __init__(self, category, x, y, number = None):
		super().__init__();
		self.category = category;
		self.setPosition(x, y);
		self.number = None;
		
		# add texture to the door
		texture = Image("assets/elements/doors/" + category + ".png");
		if texture:
			self.assignDrawable(texture);
			self.size = texture.getSize();

		# add the number in the door
		self.setNumber(number);

	#	--------------------------------------------------- *\
	#		[function] setNumber(number)
	#
	#		* Set the number in the door *
	#		Return : nil
	#	--------------------------------------------------- */
	def setNumber(self,number):
		if number != None:
			self.number = number;
			text = Text(number, "arial");
			text.setColor((61,11,0));
			text.setFontSize(20);
			text.setOffsetPosition(110,150);
			self.assignDrawable(text);
