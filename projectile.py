import pygame


class Projectile(pygame.sprite.Sprite):
    x_speed = 15

    def __init__(self, color, width, height, x_pos, y_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        #self.image.fill(color)
        #self.image.set_colorkey(color)
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos
        pygame.draw.circle(self.image, color, [self.rect.x, self.rect.y], height)


    def update(self):
        self.rect.x += self.x_speed
        return self