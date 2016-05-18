from gameplay.behaviours import inventoryBehaviour;

class Inventory():
	def __init__(self):
		self.items = [];

	def addItem(self, item):
		self.items.append(item);
		self.updateItems();

	def removeItem(self, item):
		self.items.remove(item);
		self.updateItems();

	def getItems(self):
		return self.items;

	def updateItems(self):
		inventoryBehaviour.getInterface().setEntry("items", self.items);