import pygame
import math
from Bullet import Bullet
class Player(pygame.sprite.Sprite):
    direction = 1
    caminho_imagem = pygame.image.load('.venv/assets/idle.png')
    def __init__(self):
        global caminho_imagem 
        caminho_imagem = pygame.image.load('.venv/assets/idle.png')
        pygame.sprite.Sprite.__init__(self)
        self.image = caminho_imagem.convert()
        self.image.fill((0, 0, 255))  # cor verde
        self.rect = self.image.get_rect()
        self.rect.center = (100, 100)  # posição inicial
    def update_pos(self, x, y):
        self.rect.center=(x,y)
     
    def rotate(self, xm, ym, xp, yp):
        global direction
        new_x = xm - xp
        new_y = ym - yp
        angle = math.degrees(math.atan2(-new_y,new_x))
        #self.image = pygame.transform.rotate(caminho_imagem, -angle )
        
        #flipar se passar dos eixos:3
        #ta dando errado essa porra, deixa um top down mesmo
        if 180 > angle > 90 or -180 < angle < -90:
          
            self.image = pygame.transform.rotate(caminho_imagem, -angle )
            self.image = pygame.transform.flip(self.image, False, True) 
            self.rect = self.image.get_rect(center=self.rect.center)
        
        else:
            
            self.image = pygame.transform.rotate(caminho_imagem, angle )
            self.image = pygame.transform.flip(self.image, False, False) 
            self.rect = self.image.get_rect(center=self.rect.center)

    
