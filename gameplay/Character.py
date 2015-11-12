from engine.Element import Element;
from gameplay.behaviours.characterBehaviour import *;
from engine.render.image import Image;
from engine import Render;
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

        # character texture
        texture = Image("assets/dickbutt.png");
        texture.setSize(50,50);
        textureSize = texture.getSize();

        self.assignDrawable(texture);
        self.setSize(textureSize[0], textureSize[1]);

        characters.append(self);

        Render.set(self);

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
    #        [function] isWalking()
    #
    #        * Return if the character is walking or not *
    #        Return : boolean
    #    --------------------------------------------------- */
    def isWalking(self):
        return self.walking;