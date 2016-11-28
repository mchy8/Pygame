#required
from pygame import *
from pygame.sprite import *
import pygame
import random

WIDTH = 800
HEIGHT = 600

paused = False
muted = False

screen_height = 800

white = (255,255,255)
black = (0,0,0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

x_pos = 0
y_pos = 0
clock = pygame.time.Clock()

meatballspeed = 2
maxmeatballs = 5
meatballScore = 5

spaghettispeed = 3
maxspaghettis = 5
spaghettiScore = 3

speed = 5

score = 0
maxscore = 100
#create a surface

#pygame.display.flip() 		#similar to a flip book, updates entire surface
# pygame.display.update()		#only updates portion specified
# this is the play sound function
def play(soundFile):
	soundFile = pygame.mixer.Sound(file=soundFile)
	if not muted:
		soundFile.play(loops=0)

class Meatball(Sprite):
	def __init__(self):
		Sprite.__init__(self)
		self.image = image.load("meatball_v2.bmp").convert()
		self.rect = self.image.get_rect()

	def update(self, action):
		global score
		global meatballScore
		if action == "move down":
			self.rect.y += meatballspeed
			if self.rect.y > screen_height:
				self.rect.x = random.randint(1,WIDTH -20)
				self.rect.y = (random.randint(0, HEIGHT-30))*(-1)
		elif action == "gotToTop":
			self.rect.x = random.randint(1,WIDTH -20)
			self.rect.y = (random.randint(0, HEIGHT-30))*(-1)
		if self.rect.colliderect(bowl1):
			self.rect.x = random.randint(1,WIDTH -20)
			self.rect.y = (random.randint(0, HEIGHT-30))*(-1)
			score = score + meatballScore


	def gotToTop(self):
		self.rect.x = random.randint(1,WIDTH -20)
		self.rect.y = (random.randint(0, HEIGHT-30))*(-1)

class Spaghetti(Sprite):
	def __init__(self):
		Sprite.__init__(self)
		self.image = image.load("spaghetti.bmp").convert()
		self.rect = self.image.get_rect()


	def update(self, action):
		global score
		global spaghettiScore
		if action == "move down":
			self.rect.y += spaghettispeed
			if self.rect.y > screen_height:
				self.rect.x = random.randint(1,WIDTH -20)
				self.rect.y = (random.randint(0, HEIGHT-30))*(-1)
		elif action == "gotToTop":
			self.rect.x = random.randint(1,WIDTH -20)
			self.rect.y = (random.randint(0, HEIGHT-30))*(-1)
		# for t in spaghettiArray:
		# 	if self.rect.colliderect(t):
		# 		self.rect.x = random.randint(1,WIDTH -20)
		# 		self.rect.y = (random.randint(0, HEIGHT-30))*(-1)
		# for g in meatballArray:
		# 	if self.rect.colliderect(g):
		# 		self.rect.x = random.randint(1,WIDTH -20)
		# 		self.rect.y = (random.randint(0, HEIGHT-30))*(-1)
		if self.rect.colliderect(bowl1):
			self.rect.x = random.randint(1,WIDTH -20)
			self.rect.y = (random.randint(0, HEIGHT-30))*(-1)
			score = score + spaghettiScore
			# this is for playing sound
			# play(file name here ex: 'getPoint.wav')
	def gotToTop(self):
		self.rect.x = random.randint(1,WIDTH -20)
		self.rect.y = (random.randint(0, HEIGHT-30))*(-1)

class Bowl(Sprite):
	def __init__(self):
		Sprite.__init__(self)
		self.image = image.load("bowl.bmp").convert()
		self.rect = self.image.get_rect()
		self.rect.y = 450

	def update(self):
		self.rect.x = x_pos
		self.rect.y = 450
		if self.rect.x < 0:
			self.rect.x = 0
		elif self.rect.x > (WIDTH - self.rect.width):
			self.rect.x = (WIDTH - self.rect.width)

class Background(Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load("background2.bmp")
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


init()

gameDisplay = display.set_mode((WIDTH, HEIGHT)) #initialize with a tuple
#lets add a title, aka "caption"
display.set_caption("Cloudy with a Chance of Meatballs: Catch them if you can")

scoreFont = font.Font(None, 25)

BackGround = Background("background2.bmp", [0,0])

# meatball = Meatball()
# meatballSprite = RenderPlain(meatball)
meatballArray = []
for i in range(0, maxmeatballs-1):
	meatballArray.append(Meatball())
meatballSprites = []
for x in  range(0, (len(meatballArray)-1)):
	meatballSprites.append(RenderPlain(meatballArray[x]))
spaghettiArray = []
for i in range(0, maxspaghettis-1):
	spaghettiArray.append(Spaghetti())
spaghettiSprites = []
for x in range(0, (len(spaghettiArray)-1)):
	spaghettiSprites.append(RenderPlain(spaghettiArray[x]))

bowl1 = Bowl()
bowlthing=RenderPlain(bowl1)

gameDisplay.fill(white)
gameExit = False

while not gameExit:

	# if score == maxscore:
	# 	gameExit = True
	# This sometimes works, and is used to stop the game when you get a max score

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True
	if event.type == pygame.KEYDOWN:
		y_pos= 450;
		if event.key == pygame.K_LEFT or event.key == pygame.K_a: # left key or a key pressed
			# if you want to be able to pause uncomment the if statement with the other code in it
			# if not paused:
			x_pos -= speed
			# bowlthing.move(-10)
		if event.key == pygame.K_RIGHT or event.key == pygame.K_d: # right key or d key pressed
			# if you want to be able to pause uncomment the if statement with the other code in it
			# if not paused:
			x_pos += speed
		# uncomment this code if you want muting. key m toggles mute
		# if event.key == pygame.K_m:
		# 	muted = not muted
		# un comment the code below this comment to allow pauses. space or p key toggles mute
		# if event.key == pygame.K_SPACE or event.key == pygame.K_p:
		# 	paused = not paused
	# suround all code in this if statement in the while loop under this comment if you want to be able to pause the game but keep display.update() out of the if statement
	# if not paused:
	gameDisplay.fill(white)
	gameDisplay.blit(BackGround.image, BackGround.rect)
	scoreText = scoreFont.render("Score: "+str(score), False, (0,0,0))
	gameDisplay.blit(scoreText, (320, 0))
	# pygame.display.update()
	# meatballSprite.update('move down')
	# meatballSprite.draw(gameDisplay)
	for i in range(0,len(meatballSprites) -1):
		meatballSprites[i].update("move down")
		meatballSprites[i].draw(gameDisplay)
	for i in range(0,len(spaghettiSprites) -1):
		spaghettiSprites[i].update("move down")
		spaghettiSprites[i].draw(gameDisplay)
	bowlthing.update()
	bowlthing.draw(gameDisplay)
	display.update()

pygame.quit()
quit()				#exits python

