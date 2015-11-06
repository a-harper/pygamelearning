import pygame
import projectile


pygame.init()


class Player(pygame.sprite.Sprite):
    x_speed = 0
    y_speed = 0
    washing = False
    idle_sprites = ""
    walk_sprites = ""
    wash_sprites = ""
    image = ""
    wash_loop = 0
    frame_loop = 0
    direction_r = True

    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()

    def fire_projectile(self):
        # size = pygame.Surface(self.image.get_size())
        proj = projectile.Projectile((0, 0, 0), 2, 2, self.rect.x, (self.rect.y + 13))
        if self.direction_r:
            proj.x_speed = 15
        else:
            proj.x_speed = -15
        return proj

    def update(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
        if self.rect.x > 1024:
            self.rect.x = 1024
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.y > 768:
            self.rect.y = 768
        if self.rect.y < 0:
            self.rect.y = 0

        if not self.washing:
            if self.frame_loop > 5:
                if self.x_speed == 0 and self.y_speed == 0:
                    self.image = self.idle_sprites[1]
                else:
                    self.image = self.walk_sprites[1]
            else:
                if self.x_speed == 0 and self.y_speed == 0:
                    self.image = self.idle_sprites[0]
                else:
                    self.image = self.walk_sprites[0]
            if not self.direction_r:
                self.image = pygame.transform.flip(self.image, True, False)
            if self.frame_loop > 10:
                self.frame_loop = 0
            self.wash_loop = 0
            self.frame_loop += 1
        else:
            if self.wash_loop < len(self.wash_sprites):
                self.image = self.wash_sprites[self.wash_loop]
                self.wash_loop += 1
            else:
                self.image = self.wash_sprites[len(self.wash_sprites) - 1]
        return self