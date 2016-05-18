from engine import Global;
from engine.Cinematic import Cinematic;
from engine.render.image import Image;

class TestCinematic(Cinematic):
	def __init__(self):
		super().__init__();
		screenSize = Global.getScreenSize();

		background  = Image("assets/cinematics/test.png");
		background.setSize(screenSize[0], screenSize[1]);
		background.setDepth(200);

		character = Image("assets/characterTest.png");
		character.setPosition(100,100);
		character.setSize(100,100);
		character.setDepth(201);

		self.append(character, "character");

		self.moveElementTo("character", 200,200, 2000);
		Global.setTimeout(self.whenArriveToEnd, 2000);

		self.setBackground(background);

	def whenArriveToEnd(self):
		self.moveElementTo("character", 0,0,2000);
		Global.setTimeout(self.whenArriveToEnd2, 2000);

	def whenArriveToEnd2(self):
		self.moveElementTo("character", 200,0,2000);
		Global.setTimeout(self.stop, 2000);
