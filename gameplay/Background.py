from engine import Global;
from engine.Element import Element;
from engine.render.image import Image;
from engine import Render;
#	--------------------------------------------------- *\
#		[class] Background()
#
#		* Background element *
#
#	--------------------------------------------------- */
class Background(Element):
	#	--------------------------------------------------- *\
	#		[function] __init__():
	#
	#		* Constructor *
	#	--------------------------------------------------- */
	def __init__(self, path, sceneWidth):
		super().__init__();

		self.setType("background");

        # texture
		texture = Image(path);
		texture.setDepth(-10);

		# size
		self.assignDrawable(texture);
		self.setDepth(-10);

		# left
		leftPanel = Image("assets/dot.png");
		leftPanel.setSize(texture.getSize()[0]/2,400);
		leftPanel.setOffsetPosition(-texture.getSize()[0]/2,0);
		leftPanel.setAffectedByParent(False);
		self.assignDrawable(leftPanel);
		# right
		rightPanel = Image("assets/dot.png");
		rightPanel.setSize(texture.getSize()[0]/2,400);
		rightPanel.setOffsetPosition(sceneWidth,0);
		rightPanel.setAffectedByParent(False);
		self.assignDrawable(rightPanel);

		Render.set(self);