import pygame
pygame.init()
game_display = pygame.display.set_mode((800,600))
pygame.display.set_caption('a bit racey!')
clock = pygame.time.Clock()
crashed = False
while not crashed:
	for event in pygame.event.get():
		print(event)
		if event.type == pygame.QUIT:
			crashed = True	
		print(event)
	pygame.display.update()
	clock.tick(60)
pygame.quit()
quit()