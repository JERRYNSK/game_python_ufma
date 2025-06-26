import pygame
from pygame.locals import *
class Bullet(pygame.sprite.Sprite):
    
    def __init__(self):
        img = pygame.image.load('assets/bullet.png')
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(img.convert_alpha(), (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (400, 280)  # posição inicial
        self.can_move = False
        self.vec_dir = pygame.Vector2(0)
        self.x = 0
        self.y = 0
        self.xm, self.ym = 0,0



    def shoot(self, x, y):
        self.rect.center = (x, y)
        self.vec_dir = pygame.Vector2(x, y)
        self.can_move = True
        self.x, self.y = pygame.mouse.get_pos()
        self.xm, self.ym = x,y
        print('shooted', x, y)
    def update_pos(self,x,y):
    
        if self.can_move:
            new_x = self.x - self.xm
            new_y = self.y - self.ym
            self.vec_dir += pygame.Vector2(new_x, new_y).normalize() * 5
            self.rect.center = self.vec_dir
            #print(self.vec_dir)
        
            
            
        


