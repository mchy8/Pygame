#required 
from pygame import *
from pygame.sprite import *
import pygame
import random
pygame.init();

WIDTH = 800
HEIGHT = 600

screen_height = 800 

white = (255,255,255)
black = (0,0,0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

x_pos = 0
y_pos = 200
bg_x = 0
bg_y = -200
poop_x = random.randrange(0, WIDTH) 
poop_y = random.randrange(200, HEIGHT) 

x_pos = 0
y_pos = 0
x_delta = 0
y_delta = 0
clock = pygame.time.Clock()

meatballspeed = 10
maxmeatballs = 5
spaghettispeed = 10
maxspaghettis = 5
#create a surface
gameDisplay = display.set_mode((WIDTH, HEIGHT)) #initialize with a tuple

#lets add a title, aka "caption"
display.set_caption("Cloudy with a Chance of Meatballs")

#pygame.display.flip() 		#similar to a flip book, updates entire surface
pygame.display.update()		#only updates portion specified

class Meatball(Sprite):
	def __init__(self):
		Sprite.__init__(self)
		self.image = image.load("meatball.bmp").convert()
		self.rect = self.image.get_rect()

	def update(self):
		self.rect.y += meatballspeed
		if self.rect.y > screen_height:
			self.rect.x = random.randint(1,WIDTH -20)
			self.rect.y = 100
			self.rect.y = (random.randint(0, HEIGHT-30))*(-1)

class Spaghetti(Sprite):
	def __init__(self):
		Sprite.__init__(self)
		self.image = image.load("spaghetti.bmp").convert()
		self.rect = self.image.get_rect()

	def update(self):
		self.rect.y += spaghettispeed
		if self.rect.y > screen_height:
			self.rect.x = random.randint(1,WIDTH -20)
			self.rect.y = 100
			self.rect.y = (random.randint(0, HEIGHT-30))*(-1)

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
for x in  range(0, (len(spaghettiArray)-1)):
	spaghettiSprites.append(RenderPlain(spaghettiArray[x]))

class Bowl(Sprite):
    def __init__(self):
    	Sprite.__init__(self)
    	self.image = image.load("bowl.bmp").convert()
		self.rect = self.image.get_rect()

	def move(ammount):
		self.x += ammount
		self.y 

        
# block = Meatball([20, 20])

# meatballs1 = image.load("meatball.bmp").convert()
	# def move(self):
	# 	randX = randint(0, 600)

	# 	randY = randint(0, 400)
	# 	self.rect.center = (randX,randY)

# class Spaghetti(Sprite):
# 	def __init__(self):
# 		Sprite.__init__(self)
# 		self.image = image.load("Spaghetti.bmp").convert()
# 		self.rect= self.image.get_rect()

# 	def move(self):
# 		randiX= randint(600, 500)
# 		randiY = randint(0,500)
# 		self.rect.center = (randiX, randiY)

# pygame.display.update()		#only updates portion specified
		

init()



# spaghetti1 = Spaghetti()
# meatballs1 = Meatball([20,20])
# sprites = RenderPlain(meatballs1)
def hit(self,target):
	return self.rect.colliderect(target)
#this is when it collides

gameExit = False
while not gameExit:
	gameDisplay.fill(white)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True


	if event.type == pygame.KEYDOWN:
		x_delta=0;
		y_delta=0;
		if event.key == pygame.K_LEFT:
			x_delta -= 10
		if event.key == pygame.K_RIGHT:
			x_delta += 10
		# if event.key == pygame.K_UP:
		# 	y_delta -= 10
		# if event.key == pygame.K_DOWN:
		# 	y_delta += 10
		# if event.key == pygame.K_LCTRL:


	
	x_pos +=x_delta
	y_pos +=y_delta
	if x_pos>=WIDTH:
		poop_x = random.randrange(0, WIDTH) 
		poop_y = random.randrange(200, HEIGHT) 
		x_pos = 0
		if bg_x == 0:
			bg_x -=200
		else:
			bg_x = 0
	pygame.display.update()	

	for i in range(0,len(meatballSprites) -1):
		# meatballArray[i].update()
		# meatballArray[i].draw(gameDisplay)
		meatballSprites[i].update()
		meatballSprites[i].draw(gameDisplay)
		display.update()
	for i in range(0,len(spaghettiSprites) -1):
		# meatballArray[i].update()
		# meatballArray[i].draw(gameDisplay)
		spaghettiSprites[i].update()
		spaghettiSprites[i].draw(gameDisplay)
		display.update()
	# gameDisplay.blit(meatballs1,(x_pos,y_pos))
	# gameDisplay.fill(black)
	# pygame.display.update()		
	# clock.tick(30)

	# sprites.update()
	# sprites.draw(gameDisplay)
	# display.update()
	# # block.update()
	# # block.draw(gameDisplay)
	# meatballs1.draw(gameDisplay)
	# meatballs1.update()
#render is for words
# class meatballs(pygame.sprite.Sprite):
# 	def _init_(self, x, y)

# gameDisplay.fill(black)
# pygame.display.update()	

#sounds
# elif e.type == MOUSEBOTTONDOWN:
# 	if shovel.hit(gold):
# 		mixer.sound("yada").play()
# 		gold.move()
# 		hits += 1


		

#required
pygame.quit()
quit()				#exits python

#CURRENT ISSUES
#1) HOW TO NOT GO OFF SCREEN
#2) HOW TO ONLY HAVE ONE MEATBALL 