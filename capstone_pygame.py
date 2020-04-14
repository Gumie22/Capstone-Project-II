#This is a python game
import pygame
import time
import random
#import all the necessary modules to run the game
pygame.init()
#initiate pygame
#configure the size of our screen
display_width = 800
display_height = 600
#configure some colours we will need for our game
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
#defining the colour of the blocks we will be dodging
block_color = (53,115,255)
#The width of the player
player_width = 100

#Displaying our screen and caption
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Tackling Blocks")
clock = pygame.time.Clock()

#loading the player image
playerImg = pygame.image.load("monster.copy.png")

#Defining the events and displays for our screen
def things_dodged(count):
    font = pygame.font.SysFont(None,25)
    text = font.render("Dodged: "+str(count),True,black)
    gameDisplay.blit(text,(0,0))
    

def things(thingx,thingy,thingw,thingh,color):
    pygame.draw.rect(gameDisplay,color,[thingx,thingy,thingw,thingh])

def player(x,y):
    gameDisplay.blit(playerImg,(x,y))

def text_objects(text,font):
    textSurface = font.render(text,True, red)
    return textSurface,textSurface.get_rect()

def message_display(text):
    largeTEXT = pygame.font.Font("freesansbold.ttf",115)
    TextSurf,TextRect = text_objects(text,largeTEXT)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf,TextRect)

#show updated events on the screen
    pygame.display.update()

    time.sleep(2)

    game_loop()
#message to be printed out if the player crashes
def crash():
    message_display("You Lose")

def game_loop():    
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0
    y_change = 0

#defining the start point of our blocks

    thing_startx = random.randrange(0,display_width)
    thing_starty = -600
    thing_speed = 7
    thing_width = 100
    thing_height = 100

#setting a counter to determine our score
    dodged = 0
        
    gameExit = False
#game loop
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
    
 #checking event keys and what happens when they are pressed   
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                elif event.key == pygame.K_UP:
                    y_change = -5
                elif event.key == pygame.K_DOWN:
                    y_change = 5

            if event.type == pygame.KEYUP:
               if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
               elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                     y_change = 0

                    

        x += x_change
        y += y_change
                    
            
        gameDisplay.fill(white)

        things(thing_startx,thing_starty,thing_width,thing_height,block_color)
        thing_starty += thing_speed
        player(x,y)
        things_dodged(dodged)
        

        if x > display_width - player_width or x < 0:
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width)
            dodged += 1
            thing_speed += 1

        if y < thing_starty + thing_height:
            print("y crossover")

            if x > thing_startx and x < thing_startx + thing_width or x+player_width > thing_startx and x + player_width < thing_startx+thing_width:
                print("x crossover")
                crash()

            
#update the screen for the events in the game        
        pygame.display.update()
        
        clock.tick(60)
        
game_loop()
pygame.quit()
quit()
