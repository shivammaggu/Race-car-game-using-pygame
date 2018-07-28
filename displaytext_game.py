import pygame
import time

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

car_width = 73

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()
carImg = pygame.image.load('racecar.png')

def car(x,y):
    gameDisplay.blit(carImg,(x,y))

def crash():
    display_message("You Crashed :(")
    time.sleep(3)
    game_loop()

def display_message(text):
    large_text = pygame.font.Font('freesansbold.ttf',115)
    text_surf , text_rect = text_objects(text , large_text)
    text_rect.center = (((display_width/2) , (display_height/2)))
    gameDisplay.blit(text_surf,text_rect)
    pygame.display.update()

def text_objects(text , font1):
    textsurface = font1.render(text , True , black)
    return textsurface , textsurface.get_rect()

def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change

        gameDisplay.fill(white)
        car(x,y)

        if x > display_width - car_width or x < 0:
            crash()
            
        
        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()
