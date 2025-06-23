import pygame
class Bullet(pygame.sprite.Sprite):
   

    def __init__(self):
        img = pygame.image.load('assets/bullet.png')
        pygame.sprite.Sprite.__init__(self)
        self.image = img.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (100, 100)  # posição inicial
        
