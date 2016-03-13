from engine import Global;
from engine.Interface import Interface;
from gameplay.behaviours import achievementBehaviour;

from engine.render.image import Image;
from engine.render.text import Text;

#	--------------------------------------------------- *\
#		[class] PauseInterface()
#
#		* The pause interface *
#
#	--------------------------------------------------- */
class PauseInterface(Interface):
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
		self.elements['background'].setPosition(0.29*sX, 0.3*sY);
		self.elements['background'].setSize(0.42*sX, 0.7*sY);
		self.elements['background'].setDepth(2);

		self.elements['title'] = Text("Pause", "arial");
		self.elements['title'].setFontSize(50);
		self.elements['title'].setDepth(3);
		self.elements['title'].setPosition(0.3*sX, 0.25*sY);

		self.elements['objective_title'] = Text("Votre objectif actuel:", "arial");
		self.elements['objective_title'].setFontSize(30);
		self.elements['objective_title'].setDepth(3);
		self.elements['objective_title'].setPosition(0.3*sX, 0.35*sY);

		self.elements['current_objective'] = Text("", "arial");
		self.elements['current_objective'].setFontSize(18);
		self.elements['current_objective'].setColor((230,230,230));
		self.elements['current_objective'].setDepth(3);
		self.elements['current_objective'].setPosition(0.3*sX, 0.42*sY);

		self.elements['save_button_background'] = Image("assets/darker2.png");
		self.elements['save_button_background'].setPosition(0.3*sX, 0.55*sY);
		self.elements['save_button_background'].setSize(0.4*sX, 0.05*sX);
		self.elements['save_button_background'].setDepth(3);
		self.elements['save_button_background'].setVisible(False);
		self.elements['save_button_label'] = Text("Save the game", "arial");
		self.elements['save_button_label'].setFontSize(18);
		self.elements['save_button_label'].setColor((230,230,230));
		self.elements['save_button_label'].setDepth(4);
		self.elements['save_button_label'].setAlign("center");
		self.elements['save_button_label'].setPosition(0.5*sX, 0.575*sY);

		self.elements['quit_button_background'] = Image("assets/darker2.png");
		self.elements['quit_button_background'].setPosition(0.3*sX, 0.65*sY);
		self.elements['quit_button_background'].setSize(0.4*sX, 0.05*sX);
		self.elements['quit_button_background'].setDepth(3);
		self.elements['quit_button_background'].setVisible(False);
		self.elements['quit_button_label'] = Text("Quit", "arial");
		self.elements['quit_button_label'].setFontSize(18);
		self.elements['quit_button_label'].setColor((230,230,230));
		self.elements['quit_button_label'].setDepth(4);
		self.elements['quit_button_label'].setAlign("center");
		self.elements['quit_button_label'].setPosition(0.5*sX, 0.675*sY);


	def create(self):
		sX = Global.screenSize[0];
		sY = Global.screenSize[1];

		super().create();

		self.setEntry("currentLine", 1);



	def update(self):
		currentLine = self.getEntry("currentLine");
		currentAchievement = achievementBehaviour.getCurrentAchievement();
		achievementName = currentAchievement.getDescription();
		if(achievementName):
			self.elements['current_objective'].setValue(achievementName);

		if(currentLine == 1):
			self.elements['save_button_background'].setVisible(True);
			self.elements['quit_button_background'].setVisible(False);
		else:
			self.elements['save_button_background'].setVisible(False);
			self.elements['quit_button_background'].setVisible(True);


		