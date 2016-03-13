import pygame;
from engine import Global;
from threading import Timer;
from engine.render.image import Image;
#	--------------------------------------------------- *\
#		[class] Sprite()
#
#		* Sprite element *
#
#	--------------------------------------------------- */
class Sprite(Image):
	#	--------------------------------------------------- *\
	#		[function] __init__():
	#
	#		* Constructor *
	#	--------------------------------------------------- */
	def __init__(self, imagePath, frames, uniqueLoop = False):
		super().__init__(imagePath);
		self.type = "sprite";
		self.speed = 24; # images per second
		self.isPaused = False;
		self.currentImage = 0;
		self.maxImage = frames;
		self.isUniqueLoop = uniqueLoop;
		self.loopFinished = False;

		texture = self.getTexture();
		textureSize = texture.get_size();
		self.frameWidth = textureSize[0] / self.maxImage;
		self.frameHeight = textureSize[1];

		self.timer = None;
		self.timer = Global.Interval(self.updateFrames, 1000/self.getSpeed());

	#	--------------------------------------------------- *\
	#		[function] updateFrames()
	#
	#		* Called from timer *
	#		Return : nil
	#	--------------------------------------------------- */
	def updateFrames(self):
		if not self.isPaused:
			if(self.currentImage < self.maxImage-1):
				self.currentImage += 1;
			else:
				self.currentImage = 0;

			if self.isUniqueLoop:
				if self.currentImage == self.maxImage-1:
					self.loopFinished = True;
					self.isPaused = True;
	
	#	--------------------------------------------------- *\
	#		[function] getCurrentImage()
	#
	#		* Return the current image *
	#		Return : imageNumber
	#	--------------------------------------------------- */
	def getCurrentImage(self):
		return self.currentImage;

	#	--------------------------------------------------- *\
	#		[function] setCurrentImage(image)
	#
	#		* Set the current image *
	#		Return : nil
	#	--------------------------------------------------- */
	def setCurrentImage(self, image):
		self.currentImage = image;

	#	--------------------------------------------------- *\
	#		[function] getFrameSize()
	#
	#		* Return the size of a frame *
	#		Return : size
	#	--------------------------------------------------- */
	def getFrameSize(self):
		return (self.frameWidth, self.frameHeight);

	#	--------------------------------------------------- *\
	#		[function] setSpeed(speed)
	#
	#		* Set the speed of the animation *
	#		Return : nil
	#	--------------------------------------------------- */
	def setSpeed(self, speed):
		self.speed = speed;
		# update the interval since we edited the speed
		if not self.timer is None:
			self.timer.destroy();
			self.timer = Global.Interval(self.updateFrames, 1000/self.getSpeed());


	#	--------------------------------------------------- *\
	#		[function] getSpeed()
	#
	#		* Get the speed of the animation *
	#		Return : speed
	#	--------------------------------------------------- */
	def getSpeed(self):
		return self.speed;

	#	--------------------------------------------------- *\
	#		[function] pause()
	#
	#		* Pause the animation *
	#		Return : nil
	#	--------------------------------------------------- */
	def pause(self):
		self.isPaused = True;

	#	--------------------------------------------------- *\
	#		[function] play()
	#
	#		* Play the animation if it was paused *
	#		Return : nil
	#	--------------------------------------------------- */
	def play(self):
		self.isPaused = False;
		if self.isUniqueLoop and self.loopFinished:
			self.reset();

	#	--------------------------------------------------- *\
	#		[function] reset()
	#
	#		* Reset the animation to the beginning *
	#		Return : nil
	#	--------------------------------------------------- */
	def reset(self):
		self.currentImage = 0;
