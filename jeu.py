import pygame
from pygame.locals import *

pygame.init()

fenetre = pygame.display.set_mode((640,480))
fond = pygame.image.load("background.jpg").convert()
fenetre.blit(fond,(0,0))

perso = pygame.image.load("husky.jpg").convert_alpha()
position_perso = perso.get_rect()
fenetre.blit(perso,position_perso)


pygame.display.flip()
pygame.key.set_repeat(400,90)
d = 1
while d:
    for event in pygame.event.get():
        if event.type == QUIT:
            d =  0
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                position_perso = position_perso.move(0,3)
            if event.key == K_UP:
                position_perso = position_perso.move(0,-3)
            if event.key == K_RIGHT:
                position_perso = position_perso.move(3,0)
            if event.key == K_LEFT:
                position_perso = position_perso.move(-3,0)

    fenetre.blit(fond,(0,0))
    fenetre.blit(perso,position_perso)

    pygame.display.flip()
