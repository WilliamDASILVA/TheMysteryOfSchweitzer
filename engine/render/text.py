import pygame;
from .drawable import Drawable;
#	--------------------------------------------------- *\
#		[class] Text()
#
#		* Create text *
#
#	--------------------------------------------------- */
class Text(Drawable):
	#	--------------------------------------------------- *\
	#		[function] __init__():
	#
	#		* Constructor *
	#	--------------------------------------------------- */
	def __init__(self, textValue, font):
		super().__init__();

		self.type = "text";

		self.value = textValue or "";
		self.fontSize = 12;
		self.font = font;
		self.align = "left";
		self.color = (255,255,255);
		self.fontElement = None;

		self.updateFontElement();


	#	--------------------------------------------------- *\
	#		[function] updateFontElement()
	#
	#		* Update the fontElement *
	#		Return : Font
	#	--------------------------------------------------- */
	def updateFontElement(self):
		self.fontElement = pygame.font.Font("assets/fonts/" + self.getFont() + ".ttf", self.getFontSize());

		surface = self.fontElement.render(self.getValue(), False, self.getColor());
		self.setTexture(surface);
		size = self.fontElement.size(self.getValue());
		self.setSize(size[0], size[1]);

	#	--------------------------------------------------- *\
	#		[function] getFont()
	#
	#		* Return the font path *
	#		Return : nil
	#	--------------------------------------------------- */
	def getFont(self):
		return self.font;

	#	--------------------------------------------------- *\
	#		[function] setFont(fontPath)
	#
	#		* Set the font *
	#		Return : nil
	#	--------------------------------------------------- */
	def setFont(self, fontPath):
		self.font = fontPath;
		self.updateFontElement();

	#	--------------------------------------------------- *\
	#		[function] setValue(value)
	#
	#		* Set the text value *
	#		Return : nil
	#	--------------------------------------------------- */
	def setValue(self, value):
		self.value = value;
		self.updateFontElement();

	#	--------------------------------------------------- *\
	#		[function] getValue()
	#
	#		* Return the text value *
	#		Return : value
	#	--------------------------------------------------- */
	def getValue(self):
		return self.value;

	#	--------------------------------------------------- *\
	#		[function] setColor(color)
	#
	#		* Set the text color *
	#		Return : nil
	#	--------------------------------------------------- */
	def setColor(self, color):
		self.color = color;
		self.updateFontElement();

	#	--------------------------------------------------- *\
	#		[function] getColor()
	#
	#		* Return the text color *
	#		Return : color
	#	--------------------------------------------------- */
	def getColor(self):
		return self.color;

	#	--------------------------------------------------- *\
	#		[function] setFontSize(size)
	#
	#		* Set the text size *
	#		Return : nil
	#	--------------------------------------------------- */
	def setFontSize(self, size):
		self.fontSize = size;
		self.updateFontElement();

	#	--------------------------------------------------- *\
	#		[function] getFontSize()
	#
	#		* Return the font size *
	#		Return : fontSize
	#	--------------------------------------------------- */
	def getFontSize(self):
		return self.fontSize;

	#	--------------------------------------------------- *\
	#		[function] setAlign(alignement)
	#
	#		* Set the alignement of the text *
	#		Return : nil
	#	--------------------------------------------------- */
	def setAlign(self, alignement):
		self.align = alignement;
		self.updateFontElement();

	#	--------------------------------------------------- *\
	#		[function] getAlign()
	#
	#		* Return the alignement of the text *
	#		Return : align
	#	--------------------------------------------------- */
	def getAlign(self):
		return self.align;