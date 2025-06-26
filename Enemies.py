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

    def update_pos(self):
        pass