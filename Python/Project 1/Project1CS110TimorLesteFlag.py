#---------------------------------------------------------------------------------------------------------------------------------
#Project #1
#Adam Clements
#Summary: Create the flag of Timor-Leste
# -fill the background red
# -create a yellow triangle half width of flag
# -create a black triangle 1/4 of the width of the flag
# -draw a white star in the middle of the black triangle that is 1/6 the width of the flag (rotated toward the top left corner)
#----------------------------------------------------------------------------------------------------------------------------------
#add the necessary imports (pygame)
import pygame, sys
from pygame.locals import *
leave = 0
#make a loop, so that if an invalid number is entered, it prompts again
while leave != 1:
    #ask for the horizontal size of the flag
    w = input("Input the horizontal size of the flag (min:100, max:1000): ")

    #check to make sure the flag is not too big or too small
    if int(w)>=100 and int(w)<=1000:
        #begin pygame
        pygame.init()
        #set the dimension variables for the flag (aspect ratio 1:2)
        hSize = int(w)
        vSize = int(w)//2

        #make the window
        window = pygame.display.set_mode( (hSize,vSize),0,24 )
        #create colors necessary for the flag
        RED = (218, 41, 28)
        YELLOW = (255, 199, 44)
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)
        #choose the background color (red previously created)
        window.fill(RED)
        #make the first yellow triangle (half the width)
        pygame.draw.polygon(window,YELLOW,((0,0),(0,vSize),(hSize//2,vSize//2)))
        #make the second black triangle (1/4 width of whole flag)
        pygame.draw.polygon(window,BLACK,((0,0),(0,vSize),(hSize//4,vSize//2)))
        #make the star (1/6 width of the flag)

        #pygame.draw.circle(window,WHITE,(40, 108),36,1)
        #pygame.draw.line(window,WHITE,(40, 108),(0,0))
        #pygame.draw.line(window,WHITE,(80, 215),(0,0))
        #pygame.draw.line(window,WHITE,(0,160),(300,0))
        #pygame.draw.line(window,WHITE,(40, 108),(0,108))
        pygame.draw.polygon(window,WHITE,((hSize//(430/28), vSize//(215/76)),(hSize//(430/28), vSize//(215/102)),(hSize//(430/6), vSize//(215/112)),(hSize//(430/29), vSize//(215/120)),(hSize//(430/32), vSize//(215/142)),(hSize//(430/45), vSize//(215/122)),(hSize//(430/72), vSize//(215/126)),(hSize//(430/56), vSize//(215/107)),(hSize//(430/65), vSize//(215/85)),(hSize//(430/45), vSize//(215/94))))
        #begin the loop to keep the window open

        while True:
            #check for events (specifically in order to close the window, and end the code and while loop)
            (x,y) = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == KEYDOWN and event.key == K_SPACE:
                    print((x,y))
                if event.type == QUIT:
                    leave = 1
                    pygame.quit()
                    sys.exit()
            #if there is no exit event, update the screen
            pygame.display.update()
    #if an invalid input is given, print an error message, and prompt them again
    else:
        print("Please enter a value between 100 and 1000")
