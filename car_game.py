import math

import pygame, sys
from pygame.locals import *


pygame.init()
pi = math.pi
FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()


# set up the window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
screen_size = [WINDOW_WIDTH, WINDOW_HEIGHT]
screen = pygame.display.set_mode(screen_size)
screen_rect = screen.get_rect()
pygame.display.set_caption('Animation')
DISPLAYSURF = pygame.display.set_mode((screen_size[0], screen_size[1]), 0, 32)


#colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (102, 102, 102)
DGREY = (62, 62, 62)
GREEN = (96, 128, 56)
NAVY = (0,0,128)
RED = (128, 0, 0)


alpha = 0


image_orig = pygame.image.load('carbis.png')#.convert()
scaling_factor = 0.2
image_orig = pygame.transform.scale(image_orig, ( int(scaling_factor * 641), int(scaling_factor * 258)))
image = image_orig.copy()
image_rect = image_orig.get_rect(center=screen_rect.center)

while True: # the main game loop
	DISPLAYSURF.fill(GREEN)

	alpha += 1


	image = pygame.transform.rotate(image_orig, alpha)
	image_rect = image.get_rect(center=image_rect.center)
	DISPLAYSURF.blit(image, image_rect)
	
	pygame.display.flip() # what is it?


	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	pygame.display.update()
	fpsClock.tick(FPS)