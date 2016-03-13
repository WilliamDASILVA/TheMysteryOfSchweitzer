from engine import Update;
from engine import Global;

isActive = False;
usedScene = None;
characters = [];

scale = Global.scale;

def stopMouvementForAllCharacters(value):
    for character in characters:
        character.isWalking(value);

#    --------------------------------------------------- *\
#        [function] setScene(scene)
#
#        * Set the used scene *
#        Return : nil
#    --------------------------------------------------- */
def setScene(scene):
    global usedScene;
    usedScene = scene;

#    --------------------------------------------------- *\
#        [function] setActive(value)
#
#        * Set if the character behaviour is active or not *
#        Return : nil
#    --------------------------------------------------- */
def setActive(value):
    global isActive;
    isActive = value;

#    --------------------------------------------------- *\
#        [function] updatePositions()
#
#        * Update the positions of each character *
#        Return : nil
#    --------------------------------------------------- */
def updatePositions():
    if isActive:
        for character in characters:
            position = character.getPosition();
            direction = character.getDirection();
            size = character.getSize();

            sceneSize = usedScene.getSize();
            if character.isWalking():
                if direction == "left":
                    character.setPosition(position[0] - (character.getSpeed() *scale), position[1]);
                else:
                    character.setPosition(position[0] + (character.getSpeed() *scale), position[1]);

                # hitbox
                if (position[0] > 0 and position[0] + size[0] < 100):
                    character.setDirection("right");

                if (position[0] > sceneSize[0] - 100 and position[0] + size[0] < sceneSize[0]):
                    character.setDirection("left");

                

Update.on(updatePositions);