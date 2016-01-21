import json;
from engine.Element import Element;
from engine.render.image import Image;
from gameplay.Ground import Ground;
from engine import Render;
from gameplay.Wall import Wall;
from gameplay.Background import Background;
from gameplay.Door import Door;
from gameplay.Teleport import Teleport;
from gameplay.ActionDispatcher import ActionDispatcher;
from gameplay.behaviours import backgroundBehaviour;
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

		# load a scene
		if sceneToLoad:
			f = open("assets/scenes/" + sceneToLoad + ".json", "r");
			if f:
				self.sceneData = json.load(f);
				f.close();

		# generate the map
		for e in self.sceneData['data']:
			if e:
				_type = e[0];
				data = e[1]
				position = [e[2], e[3]];

				element = None;
				if _type == "wall":
					element = Wall(data, position[0], position[1]);
				elif _type == "door":
					element = Door(data, position[0], position[1], e[4]);
					if len(e) == 6:
						self.actions.append(Teleport(position, e[5], [125, 0]));

				elif _type == "action":
					self.actions.append(ActionDispatcher(data, position[0], position[1]));
				elif _type == "spawn":
					self.spawnPoint = position;
				elif _type == "teleport":
					targetScene = data;
					targetPosition = [e[4], e[5]];

					self.actions.append(Teleport(position, targetScene, targetPosition));


				if element:
					self.append(element, position[0], position[1]);

		# adding all the elements to the render
		for e in self.getAssignedElements():
			Render.set(e);

		# getting scene size
		self.setSize(250 * len(self.getAssignedElements()), 400);

		# check if the scene have a background
		if 'background' in self.sceneData:
			element = Background(self.sceneData['background'], 250 * len(self.getAssignedElements()));
			self.append(element, 0,0);

			backgroundBehaviour.setBackground(element);


		# set the position and size of the ground
		self.groundElement = Ground();
		self.groundElement.setSize(self.size[0], self.size[0]);
		self.groundElement.setPosition(0, self.size[1]);

		self.assignedPlayer = None;

	#	--------------------------------------------------- *\
	#		[function] getGroundPosition(playerElement)
	#
	#		* Return the ground position according to the element size *
	#		Return : positionY
	#	--------------------------------------------------- */
	def getGroundPosition(self, playerElement):
		size = self.getSize();
		playerSize = playerElement.getSize();

		return size[1] - playerSize[1];

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

		self.actions = [];
		self.assignedElements = [];