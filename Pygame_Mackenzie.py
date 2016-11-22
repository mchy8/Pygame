#required 
from pygame import *
from pygame.sprite import *
import pygame
pygame.init();

white = (255,255,255)
black = (0,0,0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

x_pos = 0
y_pos = 0
x_delta = 0
y_delta = 0
clock = pygame.time.Clock()

#create a surface
gameDisplay = pygame.display.set_mode((800,600)) #initialize with a tuple

#lets add a title, aka "caption"
pygame.display.set_caption("Cloudy with a Chance of Meatballs")

#pygame.display.flip() 		#similar to a flip book, updates entire surface
pygame.display.update()		#only updates portion specified

class Meatball(Sprite):
	def __init__(self):
		Sprite.__init__(self)
		self.image = image.load("meatball.bmp").convert()
		self.rect = self.image.get_rect()


	def move(self):
		randX= randint(0, 300)
		randY = randint(450, 0)
		self.rect.center = (randX, randY)

class Spaghetti(Sprite):
	def __init__(self):
		Sprite.__init__(self)
		self.image = image.load("Spaghetti.jpg").convert()
		self.rect= self.image.get_rect()

	def move(self):
		randiX= randint(600, 500)
		randiY = randint(0,500)
		self.rect.center = (randiX, randiY)

		

init()

meatballs = Meatball()
sprites = RenderPlain(meatballs)
# def hit(self,target):
# 	return self.rect.colliderect(target)
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
		if event.key == pygame.K_UP:
			y_delta -= 10
		if event.key == pygame.K_DOWN:
			y_delta += 10
		# if event.key == pygame.K_LCTRL:

	
	x_pos +=x_delta
	y_pos +=y_delta
	# gameDisplay.fill(black)
	# pygame.display.update()		
	# clock.tick(30)

	sprites.update()
	sprites.draw(gameDisplay)
	display.update()
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