from engine import Global;
from engine.Element import Element;
from gameplay.behaviours.characterBehaviour import *;
from engine.render.image import Image;
from engine.render.sprite import Sprite;
from engine import Render;
from gameplay.ActionDispatcher import ActionDispatcher;
from gameplay.ActionReceiver import ActionReceiver;
from gameplay.behaviours import dialogBehaviour;
from gameplay.behaviours import playerBehaviour;
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
    def __init__(self, direction = "right", speed = 2, characterName = None):
        super().__init__();
        self.setType("character");

        self.direction = direction;
        self.walking = True;
        self.speed = speed;
        self.reachBorder = False;
        self.characterName = characterName;

        self.dialogStarted = False;
        self.assignedDialog = None;

        # assign a action dispatcher on the character
        self.uniqid = uuid.uuid4();
        self.functionsToCallWhenAction = [];
        self.dispatcher = ActionDispatcher(self.uniqid, 0,0);
        self.receiver = ActionReceiver(self.uniqid);
        self.receiver.on(self.callFunctions);

        # character texture
        self.sprites = {
            "walking" : Sprite("assets/characters/" + characterName + "/walking.png"),
            "static" : Sprite("assets/characters/" + characterName + "/static.png")
        };

        # sprite settings
        self.sprites['walking'].setSpeed(6);
        self.sprites['walking'].setSize(256, 256);

        self.sprites['static'].setSpeed(1);
        self.sprites['static'].setSize(256, 256);

        self.setSize(256,256);
        self.assignDrawable(self.sprites['static']);
        self.setDepth(50);

        characters.append(self);

    #   --------------------------------------------------- *\
    #       [function] useSprite(spriteName)
    #
    #       * Use a specific sprite in the character assets list *
    #   --------------------------------------------------- */
    def useSprite(self, spriteName):
        self.assignedDrawables[0] = self.sprites[spriteName];
        self.setPosition(self.position[0], self.position[1]);


    #    --------------------------------------------------- *\
    #        [function] callFunctions()
    #
    #        * Call all the functions when action event is fired *
    #        Return : nil
    #    --------------------------------------------------- */
    def callFunctions(self):
        for function in self.functionsToCallWhenAction:
            function();

        if self.assignedDialog != None and self.assignedDialog.getStarted() == False:
            if not Global.isInterfaceOpen():
                dialogBehaviour.setDialog(self.assignedDialog);
                self.assignedDialog.setCharacter(self);
                self.assignedDialog.setStarted(True);
                dialogBehaviour.start();
                Global.setInterfaceOpen(True);
                playerBehaviour.enableMouvement(False);

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
        skin.setSize(256,256);
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