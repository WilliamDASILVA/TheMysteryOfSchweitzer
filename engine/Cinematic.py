from engine.render.image import Image;
from engine import Render;
from engine import Global;
class Cinematic():


	def __init__(self):
		self.backgroundElement = None;
		self.dynamicElements = [];

		screenSize = Global.getScreenSize();

		self.fade = {
			"direction" : None,
			"interval" : None,
			"running" : False,
			"element" : Image("assets/dot.png")
		};

		self.fade['element'].setSize(screenSize[0], screenSize[1]);
		self.fade['element'].setDepth(300);
		self.fade['element'].setAffectedByCamera(False);
		self.fade['element'].setOpacity(0);


	def append(self, elementToAdd, elementName):
		tempObject = {
			"name" : elementName,
			"element" : elementToAdd,
			"timer" : None,
			"vector" : [],
			"target" : [],
			"timeout" : None,
			"isMoving" : False
		};

		self.dynamicElements.append(tempObject);

	def setElementPosition(self, elementName, x, y):
		currentElement = self.getElementByName(elementName);
		if currentElement:
			currentElement['element'].setPosition(x, y);
		else:
			return None;
		
	def moveElementTo(self, elementName, x, y, time, steps = 24):
		currentElement = self.getElementByName(elementName);
		if currentElement:
			if currentElement['element']:
				currentPosition = currentElement['element'].getPosition();
				currentElement['isMoving'] = True;
				currentElement['target'] = [x, y];
				currentElement['vector'] = [(x - currentPosition[0])/steps, (y - currentPosition[1])/steps];
				currentElement['timer'] = Global.Interval((lambda: self.updatePosition(currentElement, x, y)), time / steps);
				currentElement['timeout'] = Global.setTimeout((lambda: self.destroyTimer(currentElement)), time);
		else:
			return None;

	def destroyTimer(self, elementToUse):
		elementToUse['timer'].destroy();
		elementToUse['isMoving'] = False;
		target = elementToUse['target'];
		elementToUse['element'].setPosition(target[0], target[1]);


	def updatePosition(self, elementToUpdate, targetX, targetY):
		if elementToUpdate['isMoving']:
			vector = elementToUpdate['vector'];
			currentPosition = elementToUpdate['element'].getPosition();
			elementToUpdate['element'].setPosition(currentPosition[0] + vector[0], currentPosition[1] + vector[1]);

	def setBackground(self, backgroundElement):
		self.backgroundElement = backgroundElement;

	def getElementByName(self, name):
		for element in self.dynamicElements:
			if "name" in element:
				if(element['name'] == name):
					return element;

	def updateElements(self):
		for element in self.dynamicElements:
			if "element" in element:
				element['element'].setAffectedByCamera(False);
				Render.set(element['element']);

		if self.backgroundElement:
			self.backgroundElement.setAffectedByCamera(False);
			Render.set(self.backgroundElement);

	def updateFade(self):
		if self.fade['running']:
			if self.fade['direction'] == "in":
				opacity = self.fade['element'].getOpacity();
				if opacity < 1:
					self.fade['element'].setOpacity(opacity + 0.02);
				else:
					# finis
					self.fadeDone();
					self.fade['element'].setOpacity(1);
					
			else:
				if opacity > 0:
					opacity = self.fade['element'].getOpacity();
					self.fade['element'].setOpacity(opacity - 0.02);
				else:
					self.fade['element'].setOpacity(0);

	def fadeInEnd(self):
		self.fade['running'] = False;
		Render.delete(self.fade['element']);
		self.fade['interval'].destroy();

		self.updateElements();

	def fadeOutEnd(self):
		self.fade['running'] = False;
		self.fade['interval'].destroy();
		
		for element in self.dynamicElements:
			Render.delete(element['element']);

			if self.backgroundElement:
				Render.delete(self.backgroundElement);


	def start(self, time = 0):
		if(time != 0):
			## doing fade in
			Render.set(self.fade['element']);
			self.fade['running'] = True;
			self.fade['interval'] = Interval(self.updateFade, 50);
			self.fade['direction'] = "in";

		else:
			self.updateElements();


	def stop(self, time = 0):
		if time != 0:
			for element in self.dynamicElements:
				Render.delete(element['element']);

			if self.backgroundElement:
				Render.delete(self.backgroundElement);
		else:
			## doing fade in
			Render.set(self.fade['element']);
			self.fade['running'] = True;
			self.fade['interval'] = Interval(self.updateFade, 50);
			self.fade['direction'] = "out";

