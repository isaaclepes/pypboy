1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
import pygame
import os

os.environ['SDL_VIDEODRIVER'] = 'kmsdrm'

pygame.init()
screen = pygame.display.set_mode((720, 720), pygame.DOUBLEBUF | pygame.HWSURFACE)
screen = pygame.display.get_surface()
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 18)
 
 
def update_fps():
	fps = str(int(clock.get_fps()))
	fps_text = font.render(fps, 1, pygame.Color("coral"))
	return fps_text
 
 
loop = 1
while loop:
	screen.fill((0, 0, 0))
	screen.blit(update_fps(), (10,0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			loop = 0
	clock.tick(60)
	pygame.display.update()
 
pygame.quit()