__author__ = 'harpera'
import pygame
import math
pygame.init()

#Defining colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

PI = math.pi

size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Dark Flare's Cool Game")


# Let's set up the main program loop
# Loop until the user hits the X
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#--------------MAIN PROGRAM LOOP--------------
while not done:
    # ALL EVENT PROCESSING UNDER THIS COMMENT
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # User clicked the X
            done = True  # We should exit
    # ALL EVENT PROCESSING ABOVE THIS COMMENT

    # ALL GAME LOGIC BELOW THIS COMMENT

    # ALL GAME LOGIC ABOVE THIS COMMENT

    # ALL CODE TO DRAW BELOW THIS COMMENT
    # Erase the screen contents - Don't do anything before this or it'll get removed!
    screen.fill(WHITE)

    #Draw text to the screen
    #Select font size
    font = pygame.font.Font(None, 25)

    # Render the text, "True" means anti-aliased
    # Black is the colour
    # This line creates an image of the letters,
    # But does not put it on the screen yet
    text = font.render("Test text", True, BLACK)

    # This line stamps the text onto the screen at the given co-ords
    screen.blit(text, [250, 250])

    # Draw changes to screen - Do all changes before this or they won't display
    pygame.display.flip()


    # ALL CODE TO DRAW ABOVE THIS COMMENT

    # Max 20fps
    clock.tick(20)