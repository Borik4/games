import pygame
import time
import random


def stugum():
    global run
    for po in range(len(ball)):
        if ball[po]['y'] < you['y'] < ball[po]['y'] + 50 and ball[po]['x'] < 150 < ball[po]['x'] + 50:
            run = False
    if 700 < you['y'] or you['y'] < 0:
        run = False


def all_blit():
    win.fill((250, 250, 250))
    win.blit(green_ball, (150, you['y']))
    for asd in range(len(ball)):
        win.blit(black_ball, (ball[asd]['x'], ball[asd]['y']))
    pygame.display.update()


def create_black_ball():
    ball.append({})
    ball[-1]['x'] = 650
    ball[-1]['y'] = random.randint(1, 650)


def up():
    global up_time
    if up_time + 0.005 < time.process_time():
        up_time = time.process_time()
        you['speed'] = 10


pygame.init()
win = pygame.display.set_mode((700, 700))
pygame.display.set_caption("Game")
black_ball = pygame.image.load("img/black_ball.png")
green_ball = pygame.image.load("img/green_ball.png")
run = True
clock = pygame.time.Clock()

you = {'speed': 0, 'y': 350}
ball = [{'x': 650, 'y': 650}]
last_time = 0
up_time = -1
last_ball = -1
while run:
    for i in range(len(ball)):
        ball[i]['x'] -= 5
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        up()
    if last_time + 0.001 < time.process_time():
        last_time = time.process_time()
        you['speed'] -= 1.5
    stugum()
    you['y'] -= you['speed']
    all_blit()
    if last_ball + 0.05 < time.process_time():
        create_black_ball()
        last_ball = time.process_time()
