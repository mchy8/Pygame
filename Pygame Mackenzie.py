#required 
import pygame
pygame.init();

white = (255,255,255)
black = (0,0,0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)


#create a surface
gameDisplay = pygame.display.set_mode((800,600)) #initialize with a tuple

#lets add a title, aka "caption"
pygame.display.set_caption("CLoudy with a Chance of Meatballs")

#pygame.display.flip() 		#similar to a flip book, updates entire surface
pygame.display.update()		#only updates portion specified


gameExit = False
while not gameExit:
	gameDisplay.fill(black)

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
	
	x_pos +=x_delta
	y_pos +=y_delta
	gameDisplay.fill(red, rect=[x_pos,y_pos, 40,40])
	pygame.display.update()		
	clock.tick(30)


gameDisplay.fill(white)
pygame.display.update()	

# gameExit = False
# while not gameExit:
# 	for event in pygame.event.get():
# 		if event.type == pygame.QUIT:
# 			gameExit = True


#required
pygame.quit()
quit()				#exits python