__author__ = 'harpera'

"""
    Animating multiple objects using a list
"""

import pygame
import random

pygame.init()

BLACK = [0, 0, 0]
WHITE = [255, 255, 255]

# screensize
SIZE = [500, 500]

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Snow Animation")

# Create array to hold snow
snow_list = []

# Loop 50 times and add a snowflake in each random position
for i in range(50):
    x = random.randrange(0, 500)
    y = random.randrange(0, 500)
    snow_list.append([x, y])

clock = pygame.time.Clock()

# Loop the animation until the user clicks close
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Set screen background
    screen.fill(BLACK)

    # Process each snowflake
    for i in range(len(snow_list)):
        # Draw the snowflake
        pygame.draw.circle(screen, WHITE, snow_list[i], 2)

        # Move the snowflake down one pixel
        snow_list[i][1] += 1

        # If the snowflake falls off the screen we should reset it just above the top
        if snow_list[i][1] > 400:
            y = random.randrange(-50, -10)
            snow_list[i][1] = y
            # Give it a new x position too
            snow_list[i][0] = random.randrange(0, 500)

        #Draw changes to screen
    pygame.display.flip()
    clock.tick(20)