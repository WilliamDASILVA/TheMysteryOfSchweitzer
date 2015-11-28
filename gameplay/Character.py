from engine.Element import Element;
from gameplay.behaviours.characterBehaviour import *;
from engine.render.image import Image;
from engine import Render;
from gameplay.ActionDispatcher import ActionDispatcher;
from gameplay.ActionReceiver import ActionReceiver;
from gameplay.behaviours import dialogBehaviour;
import uuid;
#    --------------------------------------------------- *\
#        [class] Character()
#
#        * Create a character element *
#
#    --------------------------------------------------- */
class Character(Element):

    #    --------------------------------------------------- *\
    #        [function] __init__()
    #
    #        * Constructor *
    #    --------------------------------------------------- */
    def __init__(self, direction = "right", speed = 2):
        super().__init__();
        self.setType("character");

        self.direction = direction;
        self.walking = True;
        self.speed = speed;
        self.reachBorder = False;

        self.assignedDialog = None;

        # assign a action dispatcher on the character
        self.uniqid = uuid.uuid4();
        self.functionsToCallWhenAction = [];
        self.dispatcher = ActionDispatcher(self.uniqid, 0,0);
        self.receiver = ActionReceiver(self.uniqid);
        self.receiver.on(self.callFunctions);

        # character texture
        texture = Image("assets/dickbutt.png");
        texture.setOpacity(0.5);
        self.assignSkin(texture);

        characters.append(self);

        Render.set(self);

    #    --------------------------------------------------- *\
    #        [function] callFunctions()
    #
    #        * Call all the functions when action event is fired *
    #        Return : nil
    #    --------------------------------------------------- */
    def callFunctions(self):
        for function in self.functionsToCallWhenAction:
            function();

    #    --------------------------------------------------- *\
    #        [function] setPosition()
    #
    #        * Reassign the position fonction for the action dispatcher *
    #        Return : nil
    #    --------------------------------------------------- */
    def setPosition(self, x, y):
        super().setPosition(x, y);
        if self.dispatcher != None:
            size = self.dispatcher.getSize();
            self.dispatcher.setPosition(x - size[0]/2, y);

    #    --------------------------------------------------- *\
    #        [function] setDirection(direction)
    #
    #        * Set the direction where the character is walking *
    #        Return : nil
    #    --------------------------------------------------- */
    def setDirection(self, direction):
        self.direction = direction;

    #    --------------------------------------------------- *\
    #        [function] getDirection()
    #
    #        * Return the direction where the character is walking *
    #        Return : direction
    #    --------------------------------------------------- */
    def getDirection(self):
        return self.direction;

    #    --------------------------------------------------- *\
    #        [function] getSpeed()
    #
    #        * Return the speed of mouvement *
    #        Return : speed
    #    --------------------------------------------------- */
    def getSpeed(self):
        return self.speed;

    #    --------------------------------------------------- *\
    #        [function] isWalking(value)
    #
    #        * Return if the character is walking or not *
    #        Return : boolean
    #    --------------------------------------------------- */
    def isWalking(self, value = None):
        if value != None:
            self.walking = value;
        else:
            return self.walking;

    #    --------------------------------------------------- *\
    #        [function] assignSkin(skin)
    #
    #        * Assign a skin to the character *
    #        Return : nil
    #    --------------------------------------------------- */
    def assignSkin(self, skin):
        skin.setSize(50,50);
        skinSize = skin.getSize();

        self.assignDrawable(skin);
        self.setSize(skinSize[0], skinSize[1]);

    #    --------------------------------------------------- *\
    #        [function] onAction(functionToCall)
    #
    #        * Call this function when an action is made nearby the character *
    #        Return : nil
    #    --------------------------------------------------- */
    def onAction(self, functionToCall):
        self.functionsToCallWhenAction.append(functionToCall);

    #    --------------------------------------------------- *\
    #        [function] assignDialog(dialogToAssign)
    #
    #        * Assign a dialog to the character *
    #        Return : nil
    #    --------------------------------------------------- */
    def assignDialog(self, dialog):
        self.assignedDialog = dialog;

    #    --------------------------------------------------- *\
    #        [function] destroy()
    #
    #        * Destroy the element *
    #        Return : nil
    #    --------------------------------------------------- */
    def destroy(self):
        self.dispatcher.destroy();
        self.receiver.destroy();