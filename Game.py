import pygame
from random import randint
from time import sleep
pygame.init()
window = pygame.display.set_mode((1366,768))
T1 = pygame.Rect(300, 350, 150, 250)
T2 = pygame.Rect(500, 350, 150, 250)
T3 = pygame.Rect(700, 350, 150, 250)
T4 = pygame.Rect(900, 350, 150, 250)
cards = [T1,T2,T3,T4]
clicktext = pygame.font.SysFont("Verdana", 45).render("Click", True, (15, 15, 15))
x = [320,520,720,920]
scorecount = 0
score = pygame.font.SysFont("Verdana", 45).render(f"Points: {scorecount}", True, (15, 15, 15))
losecount = 0
lose = pygame.font.SysFont("Verdana", 26).render(f"Loses: {losecount}", True, (173, 0, 0))
clickcard = randint(0,3)
while 1:
    pygame.time.Clock().tick(3)
    window.fill((3, 219, 252))
    for card in cards:
        pygame.draw.rect(window,(227, 151, 0),card)
        pygame.draw.rect(window,(10, 10, 10),card, 10)
    window.blit(score, (20, 20))
    for i in pygame.event.get():
        if i.type == pygame.MOUSEBUTTONDOWN:
            xcard = pygame.mouse.get_pos()[0]
            if xcard >= x[clickcard] and xcard <= x[clickcard]+150:
                scorecount+=1
                pygame.draw.rect(window,(59, 255,75),cards[clickcard])
            else:
                losecount+=1
                pygame.draw.rect(window, (237, 12, 12), cards[clickcard])
        if i.type == pygame.QUIT:
            exit()
    window.blit(clicktext, (x[clickcard], 430))
    clickcard = randint (0, 3)
    score = pygame.font.SysFont("Verdana", 45).render(f"Points: {scorecount}", True, (15, 15, 15))
    lose = pygame.font.SysFont("Verdana", 26).render(f"Loses: {losecount}", True, (173, 0, 0))
    window.blit(lose, (1230,20))

    pygame.display.flip()