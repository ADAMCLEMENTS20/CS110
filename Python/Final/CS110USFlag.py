#--------------------------------------------
#Adam Clements
#US Flag-
#   -Draw the US flag algorithmically
#   -Use some source for accuracy. Mine are the following:
#       -https://www.inchcalculator.com/american-flag-size-proportions-calculator/
#       -#https://www.legion.org/flag/questions-answers/91472/what-are-exact-shades-colors-blue-and-red
#   -ONLY USE 3 DRAW STATEMENTS
#   -use a sprite for the stars
#-------------------------------------------
#import the necessary inputs
import pygame, sys
from pygame.locals import *


#make a class for the 50 stars
class Star(pygame.sprite.Sprite):
    #overload with x and y coordinates
    def __init__(self,x,y):
        super().__init__()
        #set the size of the stars
        size = int(vSize*0.0616)
        #set the image and image size for the star
        self.image = pygame.transform.scale(starIMG,(size,size))
        #make a rectangle using the sprite
        self.rect = self.image.get_rect(center = (x,y))
sz = ""
while sz != "l" and sz != "m" and sz != "s":
    sz = input("What size for the flag? (s,m,l) ")
    if sz == "l":
        a = 650
    elif sz == "m":
        a = 390
    elif sz == "s":
        a = 130

starsList = pygame.sprite.Group()

def drawStars():

    y = int(vSize*.054)
    for a in range(5):
        x = int(vSize*0.063)
        for b in range(6):
            star = Star(x,y)
            starsList.add(star)
            x += int(vSize*.126)
        y += int(vSize*.108)
    y = int(vSize*.108)
    for a in range(4):
        x = int(vSize*.126)
        for b in range(5):
            star = Star(x,y)
            starsList.add(star)
            x += int(vSize*.126)
        y += int(vSize*.108)
    #--------THIRD DRAW STATEMENT----------
    starsList.draw(window)

# Tell pygame to initialize
pygame.init()

# Make a window
vSize = a
hSize = vSize*1.9

# Pretty much the same no matter which code we're writing
window = pygame.display.set_mode( (int(hSize), int(vSize)), 0, 32)
#Create colors (based on colors link in top comment)
RED = (191,10,48)
BLUE = (0,40,104)
WHITE = (255, 255, 255)

window.fill(WHITE)

pygame.display.update()
yloc = 0
xloc = 0
starIMG = pygame.image.load('Star.png').convert_alpha()

while True: # Main game loop
    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit() # Quits pygame nicely
            sys.exit()  # This actually closes the window
    #make a loop which runs 13 times (for the 13 stripes)
    for i in range(13):
        #mod operator to switch back and forth from red to white
        if (i%2) == 1:
            color = WHITE
        else:
            color = RED
        #---------FIRST DRAW STATEMENT--------
        pygame.draw.rect(window,color,(xloc,yloc,int(hSize),(vSize/13)))
        yloc += (vSize//13)
    #--------SECOND DRAW STATEMENT------------
    pygame.draw.rect(window,BLUE,(0,0,(vSize*.76),(vSize*.54)))
    #call the draw stars function
    drawStars()
    pygame.display.update()
