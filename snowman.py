import pygame
import spriteloader

# Define some colors as global constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


def draw_snowman(screen, x, y):
    # Circle for the head
    pygame.draw.ellipse(screen, WHITE, [35+x, 0+y, 25, 25])
    # Draw the middle circle
    pygame.draw.ellipse(screen, WHITE, [23+x, 20+y, 50, 50])
    # Draw the bottom circle
    pygame.draw.ellipse(screen, WHITE, [0+x, 65+y, 100, 100])


def draw_stick_figure(screen, x, y):
    # Head
    pygame.draw.ellipse(screen, WHITE, [1+x, y, 10, 10], 0)

    # Legs
    pygame.draw.line(screen, WHITE, [5+x, 17+y], [10+x, 27+y], 2)
    pygame.draw.line(screen, WHITE, [5+x, 17+y], [x, 27+y], 2)

    # Body
    pygame.draw.line(screen, WHITE, [5+x, 17+y], [5+x, 7+y], 2)

    # Arms
    pygame.draw.line(screen, WHITE, [5+x, 7+y], [9+x, 17+y], 2)
    pygame.draw.line(screen, WHITE, [5+x, 7+y], [1+x, 17+y], 2)


def main():
    """ Main function for the game. """
    pygame.init()
    pygame.mouse.set_visible(False)
    # Set the width and height of the screen [width,height]
    size = [1024, 768]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("My Game")

    #Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    tickrate = 20

    # Speed (pixels per frame)
    x_speed = 0
    y_speed = 0

    # Initial position
    x_coord = 10
    y_coord = 10

    # Player washing?
    player_washing = False


    # Images
    background_image = pygame.image.load("images/bg.png").convert()
    player_idle_sprites = spriteloader.sprite_sheet((15, 26), "images/player_idle.png")
    player_walk_sprites = spriteloader.sprite_sheet((15, 26), "images/player_walk.png")
    player_wash_sprites = spriteloader.sprite_sheet((15, 26), "images/player_wash-off.png")
    player_idle1 = pygame.image.load("images/player_idle1.png").convert()
    player_idle2 = pygame.image.load("images/player_idle2.png").convert()
    player_idle1.set_colorkey(BLACK)
    player_idle2.set_colorkey(BLACK)
    frame_loop = 0
    wash_loop = 0

    # -------- Main Program Loop -----------
    while not done:
        # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop

            # Key presses
            if event.type == pygame.KEYDOWN:
                # Figure out if it was a relevant key
                if event.key == pygame.K_LEFT:
                    x_speed = -3
                if event.key == pygame.K_RIGHT:
                    x_speed = 3
                if event.key == pygame.K_UP:
                    y_speed = -3
                if event.key == pygame.K_DOWN:
                    y_speed = 3
                if event.key == pygame.K_SPACE:
                    player_washing = True

            # Key releases
            if event.type == pygame.KEYUP:
                # Figure out if it was a relevant key
                if event.key == pygame.K_LEFT:
                    x_speed = 0
                if event.key == pygame.K_RIGHT:
                    x_speed = 0
                if event.key == pygame.K_UP:
                    y_speed = 0
                if event.key == pygame.K_DOWN:
                    y_speed = 0
                if event.key == pygame.K_SPACE:
                    player_washing = False

        # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT
      
      
        # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT
        pos = pygame.mouse.get_pos()
        x_coord += x_speed
        y_coord += y_speed
        if x_coord > 1024:
            x_coord = 1024
        if x_coord < 0:
            x_coord = 0
        if y_coord > 768:
            y_coord = 768
        if y_coord < 0:
            y_coord = 0

        if not player_washing:
            if frame_loop > tickrate / 2:
                if x_speed == 0 and y_speed == 0:
                    player_image = player_idle_sprites[1]
                else:
                    player_image = player_walk_sprites[1]
            else:
                if x_speed == 0 and y_speed == 0:
                    player_image = player_idle_sprites[0]
                else:
                    player_image = player_walk_sprites[0]
            if frame_loop > tickrate:
                frame_loop = 0
            frame_loop += 1
            wash_loop = 0
        else:
            if wash_loop < len(player_wash_sprites):
                player_image = player_wash_sprites[wash_loop]
                wash_loop += 1
            else:
                player_image = player_wash_sprites[len(player_wash_sprites) - 1]

        # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        # First, clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
        screen.fill(BLACK)
        screen.blit(background_image, [0, 0])
        screen.blit(player_image, [x_coord, y_coord])
        #draw_stick_figure(screen, x_coord, y_coord)
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
         
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
 
        # Limit to 20 frames per second
        clock.tick(tickrate)

if __name__ == "__main__":
    main()


