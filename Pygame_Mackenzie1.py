from pygame import *
from pygame.sprite import *
import pygame
import random

WIDTH = 800
HEIGHT = 544


white = (255,255,255)
black = (0,0,0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

x_pos = 0
y_pos = 0
clock = pygame.time.Clock()

meatballspeed = 8
maxmeatballs = 5
meatballScore = 5

spaghettispeed = 10
maxspaghettis = 5
spaghettiScore = 3

speed = 10

score = 0
maxscore = 100


def overlap(Sprite):
	for x in meatballArray:
		if x != Sprite and Sprite.rect.colliderect(x.rect):
			Sprite.rect.x = random.randint(1,WIDTH -20)
			Sprite.rect.y = (random.randint(0, HEIGHT-30))*(-1)
			overlap(Sprite)
	for x in spaghettiArray:
		if x != Sprite and Sprite.rect.colliderect(x.rect):
			Sprite.rect.x = random.randint(1,WIDTH -20)
			Sprite.rect.y = (random.randint(0, HEIGHT-30))*(-1)
			overlap(Sprite)

class Meatball(Sprite):
	def __init__(self):
		Sprite.__init__(self)
		self.image = image.load("meatball_v2.bmp").convert_alpha()
		self.rect = self.image.get_rect()

	def update(self, action):
		global score
		global meatballScore
		if action == "move down":
			self.rect.y += meatballspeed
			if self.rect.y > HEIGHT- self.rect.height:
				self.rect.x = random.randint(1,WIDTH -20)
				self.rect.y = (random.randint(0, HEIGHT-30))*(-1)
				overlap(self)
				#y value is greater than the height it resets
		elif action == "gotToTop":
			self.rect.x = random.randint(1,WIDTH -20)
			self.rect.y = (random.randint(0, HEIGHT-30))*(-1)
			overlap(self)
		if self.rect.colliderect(bowl1):
			self.rect.x = random.randint(1,WIDTH -20)
			self.rect.y = (random.randint(0, HEIGHT-30))*(-1)
			score = score + meatballScore
			#changes the score and goes back to top
			overlap(self)

class Spaghetti(Sprite):
	def __init__(self):
		Sprite.__init__(self)
		self.image = image.load("spaghetti_v2.bmp").convert_alpha()
		self.rect = self.image.get_rect()


	def update(self, action):
		global score
		global spaghettiScore
		if action == "move down":
			self.rect.y += spaghettispeed
			if self.rect.y > HEIGHT - self.rect.height:
				self.rect.x = random.randint(1,WIDTH -20)
				self.rect.y = (random.randint(0, HEIGHT-30))*(-1)
				overlap(self)
		elif action == "gotToTop":
			self.rect.x = random.randint(1,WIDTH -20)
			self.rect.y = (random.randint(0, HEIGHT-30))*(-1)
			overlap(self)
		if self.rect.colliderect(bowl1):
			self.rect.x = random.randint(1,WIDTH -20)
			self.rect.y = (random.randint(0, HEIGHT-30))*(-1)
			score = score + spaghettiScore
			overlap(self)

class Bowl(Sprite):
	def __init__(self):
		Sprite.__init__(self)
		self.image = image.load("bowl_v2.bmp").convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.y = HEIGHT - self.rect.height

	def update(self):
		self.rect.x = x_pos
		self.rect.y = HEIGHT - self.rect.height
		if self.rect.x < 0:
			self.rect.x = 0
		elif self.rect.x > (WIDTH - self.rect.width):
			self.rect.x = (WIDTH - self.rect.width)

class Background(Sprite):
    def __init__(self, image_file, location):
        Sprite.__init__(self)
        self.image = pygame.image.load("background2.bmp")
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


init()
#initiates the pygame lib
mixer.music.load("The_XX.wav")
mixer.music.play(-1)
#plays the music in the background

gameDisplay = display.set_mode((WIDTH, HEIGHT)) #initialize with a tuple
#lets add a title, aka "caption"
display.set_caption("Cloudy with a Chance of Meatballs")

scoreFont = font.Font(None, 30)

BackGround = Background("background2.bmp", [0,0])

meatballArray = []
for i in range(0, maxmeatballs-1):
	meatballArray.append(Meatball())
meatballSprites = []
for x in  range(0, (len(meatballArray)-1)):
	#zero to the length of the array
	meatballSprites.append(RenderPlain(meatballArray[x]))
	#add the rendered meatball sprite x- adding it to meatball sprites
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
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True
	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_LEFT or event.key == pygame.K_a: # left key or a key pressed
			x_pos -= speed
		if event.key == pygame.K_RIGHT or event.key == pygame.K_d: # right key or d key pressed
			x_pos += speed
	gameDisplay.fill(white)
	gameDisplay.blit(BackGround.image, BackGround.rect)
	scoreText = scoreFont.render("Score: "+str(score), False, (0,0,0))
	gameDisplay.blit(scoreText, (320, 0))
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
quit()			

