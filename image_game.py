import pygame
pygame.init()
g_height = 600
g_width = 800
game_display = pygame.display.set_mode((g_width , g_height))
pygame.display.set_caption('a bit racey!')
clock = pygame.time.Clock()
white = (255,255,255)
black = (0,0,0)
carimg = pygame.image.load('racecar.png')
crashed = False
x = g_width * 0.45
y = g_height * 0.8
def car(x , y):
	game_display.blit(carimg , (x,y))

while not crashed:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			crashed = True
	game_display.fill(white)
	car(x,y)
	pygame.display.update()
	clock.tick(60)
pygame.quit()
quit()