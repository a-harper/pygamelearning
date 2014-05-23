import pygame
import spriteloader
import player

# Define some colors as global constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


def main():
    """ Main function for the game. """
    pygame.init()
    pygame.mouse.set_visible(False)
    # Set the width and height of the screen [width,height]
    size = [1024, 768]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Dark Flare's Wookie Game")

    #Loop until the user clicks the close button.
    done = False

    projectile_list = pygame.sprite.Group()
    all_sprites_list = pygame.sprite.Group()

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    tickrate = 20

    # Create instance of player
    default_sprite_image = spriteloader.sprite_sheet((15, 26), "images/player_idle.png")
    the_player = player.Player(default_sprite_image[0])
    # Set initial position
    the_player.rect.x = 10
    the_player.rect.y = 10
    the_player.idle_sprites = spriteloader.sprite_sheet((15, 26), "images/player_idle.png")
    the_player.walk_sprites = spriteloader.sprite_sheet((15, 26), "images/player_walk.png")
    the_player.wash_sprites = spriteloader.sprite_sheet((15, 26), "images/player_wash-off.png")
    the_player.image = the_player.idle_sprites[0]
    all_sprites_list.add(the_player)
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
                    the_player.direction_r = False
                if event.key == pygame.K_RIGHT:
                    the_player.x_speed = 3
                    the_player.direction_r = True
                if event.key == pygame.K_UP:
                    the_player.y_speed = -3
                if event.key == pygame.K_DOWN:
                    the_player.y_speed = 3
                if event.key == pygame.K_SPACE:
                    the_player.washing = True
                if event.key == pygame.K_LCTRL:
                    proj = the_player.fire_projectile()
                    projectile_list.add(proj)
                    all_sprites_list.add(proj)

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
        #the_player.update(tickrate)

        # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        # First, clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
        screen.fill(BLACK)
        screen.blit(background_image, [0, 0])
        #screen.blit(the_player.image, [the_player.rect.x, the_player.rect.y])
        all_sprites_list.update()
        all_sprites_list.draw(screen)
        #draw_stick_figure(screen, x_coord, y_coord)
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
         
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
 
        # Limit to 20 frames per second
        clock.tick(tickrate)

if __name__ == "__main__":
    main()


