import json;
#	--------------------------------------------------- *\
#		Data save
#	--------------------------------------------------- */
saveFile = "data.json";
currentJson = {};

#	--------------------------------------------------- *\
#		[function] setData(dataName, value)
#
#		* Set a specific data to the json *
#		Return : nil
#	--------------------------------------------------- */
def setData(dataName, value):
	currentJson[dataName] = value;

#	--------------------------------------------------- *\
#		[function] getData(dataName)
#
#		* Return a data from the json *
#		Return : data
#	--------------------------------------------------- */
def getData(dataName):
	if(currentJson[dataName]):
		return currentJson[dataName];
	else:
		return None;

#	--------------------------------------------------- *\
#		[function] saveData()
#
#		* Save the data in the file *
#		Return : nil
#	--------------------------------------------------- */
def saveData():
	f = open(saveFile, "w");
	if f:
		f.write(json.dumps(currentJson));
		f.close();

#	--------------------------------------------------- *\
#		[function] getSavedData()
#
#		* Return the saved data *
#		Return : nil
#	--------------------------------------------------- */
def getSavedData():
	global currentJson;

	f = open(saveFile, "r");
	if f:
		currentJson = json.load(f);
		f.close();
