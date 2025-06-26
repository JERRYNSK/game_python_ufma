import pygame
from Player import Player
from Bullet import Bullet
from Enemies import Enemies
pygame.init()
#  variables
width=800
height=480
screen = pygame.display.set_mode((width,height))
red =(255,0,0)
x_pos_player = width/2
y_pos_player = height/2


#tem que criar uma classe pra usar o sprite... merda
pl_group = pygame.sprite.Group()

#player
jogador = Player()
pl_group.add(jogador)

#bala
balas = []
#inimigos
minhoco = Enemies(300, 400)
pl_group.add(minhoco)

#functions
def update_game():
    global x_pos_player
    global y_pos_player
    minhoco.update_pos(x_pos_player, y_pos_player)
    rotate_player()
    jogador.update_pos(x_pos_player, y_pos_player)
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
        if ev.type == pygame.MOUSEBUTTONDOWN:
            bullet = Bullet()
            bullet.shoot(x_pos_player, y_pos_player)
            balas.append(bullet)
            pl_group.add(bullet)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        x_pos_player -= 1
    if keys[pygame.K_w]:
        y_pos_player-=1
    if keys[pygame.K_s]:
        y_pos_player+=1
    if keys[pygame.K_d]:
        x_pos_player+=1
    
    shoot()
    pl_group.update(screen)

def shoot():
    if len(balas) != 0:
        for i in balas:
            i.update_pos(x_pos_player, y_pos_player)

        
def rotate_player():
    xm,ym = pygame.mouse.get_pos()
    jogador.rotate(xm, ym, x_pos_player, y_pos_player)



def draw_game():
    pl_group.draw(screen)
    pygame.display.update()
while True:
    screen.fill((100,0,0))
    update_game()
    draw_game()