import pygame

class Enemies(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('assets/minhoca.jpg')
        self.x = x
        self.y = y
        self.image = pygame.transform.scale(img.convert_alpha(), (50, 50))
        self.rect = self.image.get_rect()
        self.center = (self.x, self.y)
        self.vec_dir = pygame.Vector2(self.x, self.y)

    def update_pos(self, xplayer, yplayer):
        offsetx = xplayer - self.vec_dir.x
        offsety = yplayer - self.vec_dir.y
        direction = pygame.Vector2(offsetx, offsety)
        self.vec_dir += direction.normalize() / 10
        self.rect = self.image.get_rect(center=self.vec_dir)

        print(direction.length())


        