from engine import Global;
from random import randint;
from engine import Update;
#	--------------------------------------------------- *\
#		Camera behaviour
#	--------------------------------------------------- */
cameraToUse = None;
shakeIntensity = 0;
isCameraShaking = False;
isCameraFixed = False;
fixeTarget = None;
usedScene = None;

#	--------------------------------------------------- *\
#		[function] setCameraFixedTo(targetScene)
#
#		* Fix the camera mouvement on the scene *
#		Return : nil
#	--------------------------------------------------- */
def setCameraFixedTo(targetScene):
	global isCameraFixed;
	global fixeTarget;
	isCameraFixed = True;
	fixeTarget = targetScene;

#	--------------------------------------------------- *\
#		[function] setScene(scene)
#
#		* Specify a scene for the camera behaviour *
#		Return : nil
#	--------------------------------------------------- */
def setScene(scene):
	global usedScene;
	usedScene = scene;

#	--------------------------------------------------- *\
#		[function] setCamera(camera)
#
#		* Set the camera to use in the behaviour *
#		Return : nil
#	--------------------------------------------------- */
def setCamera(camera):
	global cameraToUse;
	cameraToUse = camera;

savedPositionBeforeShaking = [0,0];

#	--------------------------------------------------- *\
#		[function] shakeCamera(intensity, time)
#
#		* Shake the camera for a certain amount of time *
#		Return : nil
#	--------------------------------------------------- */
def shakeCamera(intensity, time):
	global isCameraShaking;
	global shakeIntensity;
	if not isCameraShaking:
		isCameraShaking = True;
		shakeIntensity = intensity;

		camPosition = cameraToUse.getPosition();
		savedPositionBeforeShaking = [camPosition[0], camPosition[1]];
		Global.setInterval(camRandomPosition, 100/intensity);
		Global.setTimeout(stopShaking, time);


#	--------------------------------------------------- *\
#		[function] camRandomPosition()
#
#		* Set the camera to a random position according to the intensity *
#		Return : nil
#	--------------------------------------------------- */
def camRandomPosition():
	if isCameraShaking:
		randPosition = [randint(-5*shakeIntensity, 5*shakeIntensity), randint(-5*shakeIntensity, 5*shakeIntensity)];

		cameraToUse.setPosition(savedPositionBeforeShaking[0] + randPosition[0], savedPositionBeforeShaking[1] +randPosition[1]);

#	--------------------------------------------------- *\
#		[function] stopShaking()
#
#		* Stop the shaking *
#		Return : nil
#	--------------------------------------------------- */
def stopShaking():
	global isCameraShaking;
	isCameraShaking = False;
	cameraToUse.setPosition(savedPositionBeforeShaking[0], savedPositionBeforeShaking[1]);

#	--------------------------------------------------- *\
#		[function] onUpdate()
#
#		* Camera behaviour on each frame *
#		Return : nil
#	--------------------------------------------------- */
appendToElement = True;
def cameraUpdate():
	global appendToElement;
	position = cameraToUse.getPosition();
	if isCameraFixed:
		if fixeTarget != None:
			targetPosition = fixeTarget.getPosition();
			if appendToElement:
				targetSize = fixeTarget.getSize();
				cameraToUse.setPosition(targetPosition[0], targetPosition[1] - targetSize[1] * 2);

			# check for scene boudaries
			if usedScene:
				sceneSize = usedScene.getSize();
				sX = Global.screenSize[0];
				if(targetPosition[0] <= sX/2) or (targetPosition[0] >= sceneSize[0] - (sX/2)):
					appendToElement = False;
				else:
					appendToElement = True;



Update.on(cameraUpdate);