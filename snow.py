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
class Snow:
    def __init__(self, x_position, y_position, sway_counter, sway_direction):
        self.x_pos = x_position
        self.y_pos = y_position
        self.sway_counter = sway_counter
        self.sway_direction = sway_direction


# Loop 50 times and add a snowflake in each random position
snowflakes = [Snow(random.randrange(-50, 550), random.randrange(-50, 550), 0, 1) for i in range(200)]

clock = pygame.time.Clock()
sway_amount = 1
# Loop the animation until the user clicks close
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Set screen background
    screen.fill(BLACK)

    # Process each snowflake
    for snowflake in snowflakes:
        # Draw the snowflake
        pygame.draw.circle(screen, WHITE, (snowflake.x_pos, snowflake.y_pos), 2)

        # Move the snowflake down one pixel
        snowflake.y_pos += 1

        # Let's add a sway
        if (random.randrange(0, 2) == 1 and snowflake.sway_counter == 0) or snowflake.sway_counter > 25:
            snowflake.sway_direction *= -1
            snowflake.sway_counter = 0

        sway_amount = random.randrange(0, 3)
        snowflake.x_pos += sway_amount * snowflake.sway_direction
        snowflake.sway_counter += 1

        # If the snowflake falls off the screen we should reset it just above the top
        if snowflake.y_pos > 500 or snowflake.x_pos > 500 or snowflake.x_pos < 0:
            y = random.randrange(-50, -10)
            snowflake.y_pos = y
            # Give it a new x position too
            snowflake.x_pos = random.randrange(0, 500)

        #Draw changes to screen
    pygame.display.flip()
    clock.tick(30)