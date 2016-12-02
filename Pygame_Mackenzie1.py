from pygame import *
from pygame.sprite import *
import pygame
import random


WIDTH = 800
HEIGHT = 544
#sets the dimensions of the screen


white = (255,255,255)
black = (0,0,0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

x_pos = 0
y_pos = 0
#setting them to use later 


meatballspeed = 8
maxmeatballs = 5
meatballScore = 5

spaghettispeed = 10
maxspaghettis = 5
spaghettiScore = 3

#for both meatball and spaghetti: their speeds, max amounts and score per object
speed = 10
#speed of the bowl
score = 0
maxscore = 100
#sets the global scores and maxscores

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
		#this entire def is to make sure they dont overlap with each other when they are falling. ocassionally they may overlap because the meatballs and spaghetti fall at different speeds

class Meatball(Sprite):
	def __init__(self):
		Sprite.__init__(self)
		self.image = image.load("meatball_v2.bmp").convert_alpha()
		self.rect = self.image.get_rect()
		#gets the photo of a meatball- with transperant background 

	def update(self, action):
		global score
		global meatballScore
		if action == "move down":
			self.rect.y += meatballspeed
			if self.rect.y > HEIGHT- self.rect.height:
				self.rect.x = random.randint(1,WIDTH -20)
				self.rect.y = (random.randint(0, HEIGHT-30))*(-1)
				overlap(self)
				#when y value is greater than the height it resets
				# makes sure it doesnt overlap
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
			#makes sure it doesnt overlap

class Spaghetti(Sprite):
	def __init__(self):
		Sprite.__init__(self)
		self.image = image.load("spaghetti_v2.bmp").convert_alpha()
		self.rect = self.image.get_rect()
		#loads the spaghetti sprites 

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
			#this does the same things as the meatball sprites do 

class Bowl(Sprite):
	def __init__(self):
		Sprite.__init__(self)
		self.image = image.load("bowl_v2.bmp").convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.y = HEIGHT - self.rect.height
		#loads the bowl sprite

	def update(self):
		self.rect.x = x_pos
		self.rect.y = HEIGHT - self.rect.height
		if self.rect.x < 0:
			self.rect.x = 0
		elif self.rect.x > (WIDTH - self.rect.width):
			self.rect.x = (WIDTH - self.rect.width)
			#makes sure it doesnt go off the screen 

class Background(Sprite):
    def __init__(self, image_file, location):
        Sprite.__init__(self)
        self.image = pygame.image.load("background2.bmp")
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        #loads the background photo 
        #this background photo is from Cloudy with a Chance of Meatballs the movie- owned by Sony Pictures Animation, Sony Pictures Imageworks - it does not belong to me


init()
#initiates the pygame lib
mixer.music.load("The_XX.wav")
mixer.music.play(-1)
#plays the music in the background

gameDisplay = display.set_mode((WIDTH, HEIGHT)) #initialize with a tuple
#lets add a title, aka "caption"
display.set_caption("Cloudy with a Chance of Meatballs")
#caption

scoreFont = font.Font(None, 30)
#the score font and size

BackGround = Background("background2.bmp", [0,0])

meatballArray = []
for i in range(0, maxmeatballs-1):
	#the reason its -1 is because I start counting at 0
	meatballArray.append(Meatball())
	#appending it 
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
#all the same things I do to the meatballs 
bowl1 = Bowl()
bowlthing=RenderPlain(bowl1)
#rendering the bowl- only 
gameDisplay.fill(white)
#creating it 
gameExit = False

while not gameExit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True
	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_LEFT or event.key == pygame.K_a: # left key or a key pressed to move the bowl to the left
			x_pos -= speed
		if event.key == pygame.K_RIGHT or event.key == pygame.K_d: # right key or d key pressed to move the bowl to the right
			x_pos += speed
	gameDisplay.fill(white)
	gameDisplay.blit(BackGround.image, BackGround.rect)
	#putting the background photo in
	scoreText = scoreFont.render("Score: "+str(score), False, (0,0,0))
	gameDisplay.blit(scoreText, (320, 0))
	#the updates for the score- how it keeps adding and what color and location
	for i in range(0,len(meatballSprites) -1):
		meatballSprites[i].update("move down")
		meatballSprites[i].draw(gameDisplay)
		#how there are multiple meatballs falling at all times 
	for i in range(0,len(spaghettiSprites) -1):
		spaghettiSprites[i].update("move down")
		spaghettiSprites[i].draw(gameDisplay)
		#how there are multiple spaghettis falling at all times 
	bowlthing.update()
	bowlthing.draw(gameDisplay)
	display.update()
	#updates the screen continuously 

pygame.quit() #when it ends 
quit()			

