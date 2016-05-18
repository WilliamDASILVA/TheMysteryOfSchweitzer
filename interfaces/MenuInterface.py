from engine import Global;
from engine.Interface import Interface;

from engine.render.image import Image;
from engine.render.text import Text;
from random import randint;

thunderInterval = None;

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


		self.currentButton = "play";
		self.buttons = ['play', 'settings', 'credits', 'quit'];
		self.gameButtons = ['continue', 'new'];
		self.isGameOpen = False;
		self.callOutsider = None;

		self.setEntry("currentLine", 1);
		self.setEntry("numberOfItems", 4);

	def delete(self):
		if(thunderInterval):
			thunderInterval.destroy();

		super().delete();

	def setOutside(self, function):
		self.callOutsider = function;


	def editSky2(self):
		self.elements['sky'].setVisible(False);
		self.elements['sky_darker'].setVisible(False);
		

	def editSky(self):
		isFlash = randint(1,10);
		if(isFlash == 2):
			self.elements['sky'].setVisible(True);
			self.elements['sky_darker'].setVisible(True);

			if(self.callOutsider):
				self.callOutsider();

			Global.setTimeout(self.editSky2, 80);


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
		self.elements['sky'].setVisible(False);

		self.elements['sky_darker'] = Image("assets/sky_darker.png");
		self.elements['sky_darker'].setPosition(0, 0);
		self.elements['sky_darker'].setSize(1*sX, 1*sY);
		self.elements['sky_darker'].setDepth(20);
		self.elements['sky_darker'].setVisible(False);

		self.elements['menu_background'] = Image("assets/dot.png");
		self.elements['menu_background'].setPosition(0, 0);
		self.elements['menu_background'].setSize(0.5*sX, 1*sY);
		self.elements['menu_background'].setDepth(23);
		self.elements['menu_background'].setOpacity(0.25);

		self.elements['logo'] = Image("assets/logo_white.png");
		self.elements['logo'].setPosition(((0.5 * sX) / 2) - ((0.5*sX)-180)/2, 60);
		self.elements['logo'].setSize((0.5*sX) - 180, ((0.5 * sX) - 180) / (649/186));
		self.elements['logo'].setDepth(24);

		button_width = (0.5*sX) - 180;
		button_height = ((0.5*sX) - 180) / (269/68);

		# play button
		self.elements['play_background'] = Image("assets/white.png");
		self.elements['play_background'].setPosition(((0.5 * sX) / 2) - ((0.5*sX)-180)/2, 60 + ((0.5 * sX) - 180) / (649/186) + 20);
		self.elements['play_background'].setSize(button_width, button_height);
		self.elements['play_background'].setDepth(24);
		self.elements['play_background'].setVisible(False);

		self.elements['play_text'] = Text("Jouer", "arial");
		self.elements['play_text'].setFontSize(25);
		self.elements['play_text'].setColor((43,56,66));
		self.elements['play_text'].setDepth(25);
		self.elements['play_text'].setAlign("center");
		self.elements['play_text'].setPosition(((0.5 * sX) / 2), 60 + ((0.5 * sX) - 180) / (649/186) + 20 + button_height/2 - 20);

		# settings button
		self.elements['settings_background'] = Image("assets/white.png");
		self.elements['settings_background'].setPosition(((0.5 * sX) / 2) - ((0.5*sX)-180)/2, self.elements['play_background'].position[1] + 80);
		self.elements['settings_background'].setSize(button_width, button_height);
		self.elements['settings_background'].setDepth(24);
		self.elements['settings_background'].setVisible(False);

		self.elements['settings_text'] = Text("Paramètres", "arial");
		self.elements['settings_text'].setFontSize(25);
		self.elements['settings_text'].setColor((43,56,66));
		self.elements['settings_text'].setDepth(25);
		self.elements['settings_text'].setAlign("center");
		self.elements['settings_text'].setPosition(((0.5 * sX) / 2), self.elements['play_text'].position[1] + 80);

		# credits button
		self.elements['credits_background'] = Image("assets/white.png");
		self.elements['credits_background'].setPosition(((0.5 * sX) / 2) - ((0.5*sX)-180)/2, self.elements['settings_background'].position[1] + 80);
		self.elements['credits_background'].setSize(button_width, button_height);
		self.elements['credits_background'].setDepth(24);
		self.elements['credits_background'].setVisible(False);

		self.elements['credits_text'] = Text("Crédits", "arial");
		self.elements['credits_text'].setFontSize(25);
		self.elements['credits_text'].setColor((43,56,66));
		self.elements['credits_text'].setDepth(25);
		self.elements['credits_text'].setAlign("center");
		self.elements['credits_text'].setPosition(((0.5 * sX) / 2), self.elements['settings_text'].position[1] + 80);

		# quit button
		self.elements['quit_background'] = Image("assets/white.png");
		self.elements['quit_background'].setPosition(((0.5 * sX) / 2) - ((0.5*sX)-180)/2, self.elements['credits_background'].position[1] + 80);
		self.elements['quit_background'].setSize(button_width, button_height);
		self.elements['quit_background'].setDepth(24);
		self.elements['quit_background'].setVisible(False);

		self.elements['quit_text'] = Text("Quitter", "arial");
		self.elements['quit_text'].setFontSize(25);
		self.elements['quit_text'].setColor((43,56,66));
		self.elements['quit_text'].setDepth(25);
		self.elements['quit_text'].setAlign("center");
		self.elements['quit_text'].setPosition(((0.5 * sX) / 2), self.elements['credits_text'].position[1] + 80);


		# game menu
		self.elements['game_background'] = Image("assets/dot.png");
		self.elements['game_background'].setPosition(0.5*sX + 20, 60 + ((0.5 * sX) - 180) / (649/186) + 20);
		self.elements['game_background'].setSize(0.5*sX - 40, 160);
		self.elements['game_background'].setDepth(25);
		self.elements['game_background'].setOpacity(0.25);
		self.elements['game_background'].setVisible(False);

		self.elements['continue_background'] = Image("assets/white.png");
		self.elements['continue_background'].setPosition(0.5*sX + 20, self.elements['game_background'].position[1]);
		self.elements['continue_background'].setSize(0.5*sX - 40, button_height);
		self.elements['continue_background'].setDepth(26);
		self.elements['continue_background'].setVisible(False);

		self.elements['continue_text'] = Text("Continuer", "arial");
		self.elements['continue_text'].setFontSize(25);
		self.elements['continue_text'].setColor((243,243,243));
		self.elements['continue_text'].setDepth(27);
		self.elements['continue_text'].setAlign("center");
		self.elements['continue_text'].setVisible(False);
		self.elements['continue_text'].setPosition(((0.5 * sX) / 2) + 0.5*sX + 20, self.elements['game_background'].position[1] + 20);

		self.elements['new_background'] = Image("assets/white.png");
		self.elements['new_background'].setPosition(0.5*sX + 20, self.elements['continue_background'].position[1] + 80);
		self.elements['new_background'].setSize(0.5*sX - 40, button_height);
		self.elements['new_background'].setDepth(26);
		self.elements['new_background'].setVisible(False);

		self.elements['new_text'] = Text("Nouvelle partie", "arial");
		self.elements['new_text'].setFontSize(25);
		self.elements['new_text'].setColor((243,243,243));
		self.elements['new_text'].setDepth(27);
		self.elements['new_text'].setAlign("center");
		self.elements['new_text'].setVisible(False);
		self.elements['new_text'].setPosition(((0.5 * sX) / 2) + 0.5*sX + 20, self.elements['continue_text'].position[1] + 80);

		global thunderInterval;
		thunderInterval = Global.Interval(self.editSky, 1000);

	def create(self):
		sX = Global.screenSize[0];
		sY = Global.screenSize[1];

		super().create();

	def update(self):

		currentLine = self.getEntry("currentLine");
		currentButton = self.buttons[currentLine-1];

		for button in self.buttons:
			self.elements[button + "_background"].setVisible(False);
			self.elements[button + '_text'].setColor((243, 243, 243));

		self.elements[currentButton + "_background"].setVisible(True);
		self.elements[currentButton + "_text"].setColor((43,56,66));

		# game
		if(self.isGameOpen):

			gameLine = self.getEntry("currentGameLine");
			gameButton = self.gameButtons[gameLine-1];

			for btn in self.gameButtons:
				self.elements[btn + "_background"].setVisible(False);
				self.elements[btn + '_text'].setColor((243, 243, 243));

			self.elements[gameButton + "_background"].setVisible(True);
			self.elements[gameButton + "_text"].setColor((43,56,66));

			canContinue = self.getEntry("canContinue");
			if(canContinue):
				self.elements['continue_background'].setOpacity(1);
				self.elements['continue_text'].setOpacity(1);
			else:
				self.elements['continue_background'].setOpacity(0.5);
				self.elements['continue_text'].setOpacity(0.5);
				


	def closeMenu(self):
		# close
		self.elements['game_background'].setVisible(False);
		self.elements['new_text'].setVisible(False);
		self.elements['new_background'].setVisible(False);
		self.elements['continue_background'].setVisible(False);
		self.elements['continue_text'].setVisible(False);

		self.isGameOpen = False;

	def openMenu(self):
		# open
		self.elements['game_background'].setVisible(True);
		self.elements['new_text'].setVisible(True);
		self.elements['new_background'].setVisible(False);
		self.elements['continue_background'].setVisible(False);
		self.elements['continue_text'].setVisible(True);

		self.isGameOpen = True;