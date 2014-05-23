import pygame
import spriteloader
import player

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

    # Create instance of player
    the_player = player.Player()
    # Set initial position
    the_player.x_coord = 10
    the_player.y_coord = 10
    the_player.idle_sprites = spriteloader.sprite_sheet((15, 26), "images/player_idle.png")
    the_player.walk_sprites = spriteloader.sprite_sheet((15, 26), "images/player_walk.png")
    the_player.wash_sprites = spriteloader.sprite_sheet((15, 26), "images/player_wash-off.png")
    the_player.image = the_player.idle_sprites[0]

    # Images
    background_image = pygame.image.load("images/bg.png").convert()
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
                    the_player.x_speed = -3
                if event.key == pygame.K_RIGHT:
                    the_player.x_speed = 3
                if event.key == pygame.K_UP:
                    the_player.y_speed = -3
                if event.key == pygame.K_DOWN:
                    the_player.y_speed = 3
                if event.key == pygame.K_SPACE:
                    the_player.washing = True

            # Key releases
            if event.type == pygame.KEYUP:
                # Figure out if it was a relevant key
                if event.key == pygame.K_LEFT:
                    the_player.x_speed = 0
                if event.key == pygame.K_RIGHT:
                    the_player.x_speed = 0
                if event.key == pygame.K_UP:
                    the_player.y_speed = 0
                if event.key == pygame.K_DOWN:
                    the_player.y_speed = 0
                if event.key == pygame.K_SPACE:
                    the_player.washing = False

        # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT
      
      
        # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT
        pos = pygame.mouse.get_pos()
        the_player = player.do_updates(the_player, tickrate)
        # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        # First, clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
        screen.fill(BLACK)
        screen.blit(background_image, [0, 0])
        screen.blit(the_player.image, [the_player.x_coord, the_player.y_coord])
        #draw_stick_figure(screen, x_coord, y_coord)
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
         
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
 
        # Limit to 20 frames per second
        clock.tick(tickrate)

if __name__ == "__main__":
    main()


