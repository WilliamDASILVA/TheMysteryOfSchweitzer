#	--------------------------------------------------- *\
#		Update module
#	--------------------------------------------------- */

functionsToCall = [];

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
	for function in functionsToCall:
		function();