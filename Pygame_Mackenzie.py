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
y_pos = 0
# x_delta = 0
# y_delta = 0
clock = pygame.time.Clock()

meatballspeed = 10
maxmeatballs = 5
spaghettispeed = 10
maxspaghettis = 5
score = 0
maxscore = 500 
meatballScore = 5
spaghettiScore = 3
#create a surface
gameDisplay = display.set_mode((WIDTH, HEIGHT)) #initialize with a tuple

#lets add a title, aka "caption"
display.set_caption("Cloudy with a Chance of Meatballs")

#pygame.display.flip() 		#similar to a flip book, updates entire surface
# pygame.display.update()		#only updates portion specified

class Meatball(Sprite):
	def __init__(self):
		Sprite.__init__(self)
		self.image = image.load("meatball.bmp").convert()
		self.rect = self.image.get_rect()

	def update(self, action):
		if action == "move down":
			self.rect.y += meatballspeed
			if self.rect.y > screen_height:
				self.rect.x = random.randint(1,WIDTH -20)
				self.rect.y = (random.randint(0, HEIGHT-30))*(-1)
		elif action == "gotToTop":
			self.rect.x = random.randint(1,WIDTH -20)
			self.rect.y = (random.randint(0, HEIGHT-30))*(-1)
		# for g in meatballArray:
		# 	if self.rect.colliderect(g):
		# 		self.rect.x = random.randint(1,WIDTH -20)
		# 		self.rect.y = (random.randint(0, HEIGHT-30))*(-1)
		# for t in spaghettiArray:
		# 	if self.rect.colliderect(t):
		# 		self.rect.x = random.randint(1,WIDTH -20)
		# 		self.rect.y = (random.randint(0, HEIGHT-30))*(-1)
		# if self.rect.colliderect(bowl1):
		# 	self.rect.x = random.randint(1,WIDTH -20)
		# 	self.rect.y = (random.randint(0, HEIGHT-30))*(-1)
		# 	global score += meatballScore


	def gotToTop(self):
		self.rect.x = random.randint(1,WIDTH -20)
		self.rect.y = (random.randint(0, HEIGHT-30))*(-1)

class Spaghetti(Sprite):
	def __init__(self):
		Sprite.__init__(self)
		self.image = image.load("spaghetti.bmp").convert()
		self.rect = self.image.get_rect()
		

	def update(self, action):
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
		# if self.rect.colliderect(bowl1):
		# 	self.rect.x = random.randint(1,WIDTH -20)
		# 	self.rect.y = (random.randint(0, HEIGHT-30))*(-1)
		# 	global score += spaghettiScore


	def gotToTop(self):
		self.rect.x = random.randint(1,WIDTH -20)
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
for x in range(0, (len(spaghettiArray)-1)):
	spaghettiSprites.append(RenderPlain(spaghettiArray[x]))

class Bowl(Sprite):
	def __init__(self):
		Sprite.__init__(self)
		self.image = image.load("bowl.bmp").convert()
		self.rect = self.image.get_rect()
		self.rect.y = 450

	def update(self):
		self.rect.x = x_pos
		self.rect.y = 450

# bowlthing=RenderPlain(Bowl)
bowl1 = Bowl()

bowlthing= RenderPlain(bowl1)

init()

gameDisplay.fill(white)
gameExit = False
while not gameExit:
	# bowlthing()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True
	if event.type == pygame.KEYDOWN:
		# x_pos=;
		y_pos= 450;
		if event.key == pygame.K_LEFT:
			x_pos -= 10
			# bowlthing.move(-10)
		if event.key == pygame.K_RIGHT:
			x_pos += 10
			# bowlthing.move(10)
		# if event.key == pygame.K_UP:
		# 	y_delta -= 10
		# if event.key == pygame.K_DOWN:
		# 	y_delta += 10
		# if event.key == pygame.K_LCTRL:
	gameDisplay.fill(white)
	scoreFont = font.Font(None, 25)
	scoreText = scoreFont.render("Score: "+str(score), False, (0,0,0))
	gameDisplay.blit(scoreText, (320, 0))
	# pygame.display.update()	
	for i in range(0,len(meatballSprites) -1):
		meatballSprites[i].update("move down")
		meatballSprites[i].draw(gameDisplay)
		display.update()
	for i in range(0,len(spaghettiSprites) -1):
		# meatballArray[i].update()
		# meatballArray[i].draw(gameDisplay)
		spaghettiSprites[i].update("move down")
		spaghettiSprites[i].draw(gameDisplay)
		display.update()
	bowlthing.update()
	bowlthing.draw(gameDisplay)
	display.update()
	for i in range(0, len(meatballSprites)-1):
		if pygame.sprite.collide_rect(bowl1, meatballArray[i]):
			score+=meatballScore
			meatballSprites[i].update("gotToTop")
	for i in range(0, len(spaghettiSprites)-1):
		if pygame.sprite.collide_rect(bowl1, spaghettiArray[i]):
			score+=spaghettiScore
			spaghettiSprites[i].update("gotToTop")

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


# gameDisplay.fill(black)
# pygame.display.update()	

#sounds--- edit this 
# elif e.type == MOUSEBOTTONDOWN:
# 	if shovel.hit(gold):
# 		mixer.sound("yada").play()
# 		gold.move()
# 		hits += 1


		

#required
pygame.quit()
quit()				#exits python
 