
# stored data
savedData = {};

#	--------------------------------------------------- *\
#		[function] saveData(dataName, value)
#
#		* Save a temporary data in the specitif scene *
#		Return : nil
#	--------------------------------------------------- */
def saveData(sceneName, dataName, value):
	global savedData;
	savedData[sceneName][dataName] = value;

#	--------------------------------------------------- *\
#		[function] getSavedData(dataName)
#
#		* Return the saved data in the specitif scene *
#		Return : savedData
#	--------------------------------------------------- */
def getSavedData(sceneName, dataName):
	if (sceneName in savedData) and (dataName in savedData[sceneName]):
		return savedData[sceneName][dataName];
	else:
		return None;

def getData(sceneName):
	if sceneName in savedData:
		return savedData[sceneName];
	else:
		return None;