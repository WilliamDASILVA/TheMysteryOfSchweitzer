import json;
from engine import Global;
from engine.Element import Element;
from engine.render.image import Image;
from gameplay.Ground import Ground;
from engine import Render;
from gameplay.Wall import Wall;
from gameplay.Background import Background;
from gameplay.Door import Door;
from gameplay.Teleport import Teleport;
from gameplay.Pickup import Pickup;
from gameplay.ActionDispatcher import ActionDispatcher;
from gameplay.behaviours import backgroundBehaviour;
from gameplay.behaviours import sceneBehaviour;
from gameplay.Character import Character;
from gameplay.Dialog import Dialog;
from gameplay import SceneData;
from gameplay import GlobalVars;

#	--------------------------------------------------- *\
#		[class] Scene()
#
#		* Scene element *
#
#	--------------------------------------------------- */
class Scene(Element):
	#	--------------------------------------------------- *\
	#		[function] __init__():
	#
	#		* Constructor *
	#	--------------------------------------------------- */
	def __init__(self, sceneToLoad):
		super().__init__();
		self.setType("scene");
		self.assignedElements = [];
		self.actions = [];

		self.sceneData = None;
		self.spawnPoint = None;
		self.name = "";
		self.file = sceneToLoad;

		# load a scene
		if sceneToLoad:
			f = open("assets/scenes/" + sceneToLoad + ".json", "r", encoding='utf-8');
			if f:
				self.sceneData = json.load(f);
				f.close();
		# getting scene size
		self.setSize(0, 400);

		# set the position and size of the ground
		self.groundElement = Ground();
		self.groundElement.setSize(self.size[0], self.size[0]);
		self.groundElement.setPosition(0, self.size[1]);

		mapSize = 0;

		self.name = self.sceneData['name'];

		# generate the map
		for e in self.sceneData['data']:
			if e:
				_type = e[0];
				data = e[1]
				position = [e[2], e[3]];

				element = None;
				if _type == "wall":
					element = Wall(data, position[0], position[1]);
					mapSize += 1;
				elif _type == "pickup":
					element = Pickup(data, position[0], position[1]);
				elif _type == "door":
					element = Door(data, position[0], position[1], e[4]);
					mapSize += 1;
					if len(e) == 6:
						self.actions.append(Teleport(position, e[5], [125, 0]));
				elif _type == "action":
					self.actions.append(ActionDispatcher(data, position[0], position[1]));
				elif _type == "spawn":
					self.spawnPoint = position;
				elif _type == "character":
					element = Character(e[5], e[6], e[1]);
					position = [e[2], self.getGroundPosition(element)];

					if(e[4] != None):
						dialog = Dialog(e[4]);
						dialog.assignInterface(GlobalVars.getVar("dialogInterface"));
						element.assignDialog(dialog);

				elif _type == "teleport":
					targetScene = data;
					targetPosition = [e[4], e[5]];

					self.actions.append(Teleport(position, targetScene, targetPosition));


				if element:
					self.append(element, position[0], position[1]);

		self.setSize(250 * mapSize, 400);

		# check if the scene have a background
		if 'background' in self.sceneData:
			element = Background(self.sceneData['background'], 250 * mapSize);
			self.append(element, 250 * mapSize,0);
			backgroundBehaviour.setBackground(element);


		self.assignedPlayer = None;

		Global.setTimeout(self.appendToRender, 500);


	def appendToRender(self):
		# adding all the elements to the render
		k = 0;
		for e in self.getAssignedElements():
			k += 1;
			Render.set(e);

		if(k == len(self.getAssignedElements())):
			Global.setTimeout(self.resetRender, 1000);

	def resetRender(self):
		sceneBehaviour.getTransition().changeFade();

	#	--------------------------------------------------- *\
	#		[function] getGroundPosition(playerElement)
	#
	#		* Return the ground position according to the element size *
	#		Return : positionY
	#	--------------------------------------------------- */
	def getGroundPosition(self, playerElement):
		size = self.getSize();
		playerSize = playerElement.getSize();

		return 400 - playerSize[1];

	#	--------------------------------------------------- *\
	#		[function] getName()
	#
	#		* Return the scene's name *
	#		Return : name
	#	--------------------------------------------------- */
	def getName(self):
		return self.name;

	#	--------------------------------------------------- *\
	#		[function] getFileName()
	#
	#		* Return the scene's filename *
	#		Return : file
	#	--------------------------------------------------- */
	def getFileName(self):
		return self.file;

	#	--------------------------------------------------- *\
	#		[function] assign()
	#
	#		* Assign a player to the scene *
	#		Return : nil
	#	--------------------------------------------------- */
	def assign(self, player):
		self.assignedPlayer = player;
		self.assignedPlayer.assign(self);

		if self.spawnPoint:
			self.assignedPlayer.setPosition(self.spawnPoint[0], self.getGroundPosition(self.assignedPlayer));

	#	--------------------------------------------------- *\
	#		[function] append(element, x, y)
	#
	#		* Append an element to the scene to a specific position *
	#		Return : nil
	#	--------------------------------------------------- */
	def append(self, element, x, y):
		self.assignedElements.append(element);
		element.setPosition(x, y);

	#	--------------------------------------------------- *\
	#		[function] getAssignedElements()
	#
	#		* Return the list of assigned elements *
	#		Return : assignedElements
	#	--------------------------------------------------- */
	def getAssignedElements(self):
		return self.assignedElements;

	#	--------------------------------------------------- *\
	#		[function] destroy()
	#
	#		* Destroy the scene and remove all the elements that she contains *
	#		Return : nil
	#	--------------------------------------------------- */
	def destroy(self):
		for element in self.getAssignedElements():
			element.destroy();
			Render.delete(element);
		
		for action in self.actions:
			action.destroy();
			Render.delete(action);

		self.actions = [];
		self.assignedElements = [];