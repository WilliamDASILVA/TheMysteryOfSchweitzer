import time;
#	--------------------------------------------------- *\
#		Update module
#	--------------------------------------------------- */
lastTime = 0;
firstLoop = True;
functionsToCall = [];
minFPS = 10;
maxFPS = 60;

#	--------------------------------------------------- *\
#		[function] on(functionToCall)
#
#		* When update *
#		Return : nil
#	--------------------------------------------------- */
def on(functionToCall):
	functionsToCall.append(functionToCall);

#	--------------------------------------------------- *\
#		[function] onUpdate()
#
#		* Function called every frame *
#		Return : nil
#	--------------------------------------------------- */
def onUpdate():
    global lastTime;
    global firstLoop;
    currentTime = time.time()*1000.0;

    elapsed = currentTime - lastTime;
    if firstLoop:
        lastTime = currentTime;
        elapsed = currentTime - lastTime;
        firstLoop = False;

    if (elapsed >= 1000/maxFPS) and (elapsed <= 1000/minFPS):
        lastTime = currentTime;
        for function in functionsToCall:
            function();

    # time exceded
    if elapsed > 30:
        lastTime = currentTime;
