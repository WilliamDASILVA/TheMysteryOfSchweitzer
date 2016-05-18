from engine import Global;

isActive = False;
currentAchievementToDo = None;

def setActive(value):
	global isActive;
	isActive = value;

def setAchievement(achievement):
	global currentAchievementToDo;
	currentAchievementToDo = achievement;

def getCurrentAchievement():
	return currentAchievementToDo;