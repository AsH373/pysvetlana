import random
import pygame
import time
shirina = 800
dlina = 600
pygame.init()
zarzdka = pygame.display.set_mode((shirina, dlina))
pygame.display.set_caption("Светлама")
speed = pygame.time.Clock()
five = 5
def game():
    snake = []
    x1 = shirina / 2
    y1 = dlina / 2
    razmer = 30
    shag = 30
    leng = 1
    x1_change = 0
    y1_change = 0
    zarzdka.fill("white")
    golovka = [x1, y1]
    snake.append(golovka)
    for i in snake:
        pygame.draw.rect(zarzdka, "red", [i[0], i[1], razmer, razmer])
    pygame.display.update()
    pygame.display.flip()
    while True:
        while True:
            zarzdka.fill('purple')
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        break
                        break
                    if event.key == pygame.K_c:
                         game()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change -= shag
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change += shag
                    y1_change = 0
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change += shag
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change -= shag
        x1 += x1_change
        y1 += y1_change
        for i in snake:
            pygame.draw.rect(zarzdka, "red", [i[0], i[1], razmer, razmer])
        pygame.display.flip()
        snake.append(golovka)
        if len(snake) > leng:
            del snake[0]
    pygame.display.update()
    time.sleep(3)
    pygame.quit()
    quit()
game()













