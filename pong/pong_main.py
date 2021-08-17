import random
import time
import math
import pygame

def speed_chenging():
    global change_time
    if change_time + 0.015 < time.process_time():
        change_time = time.process_time()
        if math.fabs(ball['x_speed']) < 20:
            ball['x_speed'] += 2 * random.random() * ball['x_speed'] / math.fabs(ball['x_speed'])
        if math.fabs(ball['y_speed']) < 20:
            ball['y_speed'] += random.random() * ball['y_speed'] / math.fabs(ball['y_speed'])


def all_blit():
    win.fill((250, 250, 250))
    win.blit(player, (player_1['x'], player_1['y']))
    win.blit(player, (player_2['x'], player_2['y']))
    win.blit(ball_img, (ball['x'], ball['y']))
    pygame.display.update()


def ball_go():
    global run
    if 680 > ball['y'] > 20:
        ball['y'] += ball['y_speed']
    else:
        ball['y_speed'] *= -gortakic
        if ball['y'] < 400:
            ball['y'] = 25
            ball['y'] += ball['y_speed']
        else:
            ball['y'] = 675
            ball['y'] += ball['y_speed']

    if ball['x'] < 0:
        print('player 2 won')
        run = False
    elif 20 > ball['x']:
        if player_1['y'] + 150 > ball['y'] > player_1['y'] - 20:
            ball['x_speed'] *= -0.7
            ball['x'] = 25
        else:
            ball['x'] += ball['x_speed']
    elif 20 <= ball['x'] < 665:
        ball['x'] += ball['x_speed']
    elif 600 < ball['x'] < 680:
        if player_2['y']+150 > ball['y'] > player_2['y'] - 20:
            c = player_2['y'] - 20
            v = player_2['y']+150
            d = 170
            # x_to_y =

            ball['x_speed'] *= -0.7
            ball['x'] = 660
        else:
            ball['x'] += ball['x_speed']
    else:
        print('plyer 1 win')
        run = False


pygame.init()
win = pygame.display.set_mode((700, 700))
pygame.display.set_caption("Game")
player = pygame.image.load("img/player.jpg")
ball_img = pygame.image.load("img/ball.png")
run = True
clock = pygame.time.Clock()

player_1 = {'x': 5, 'y': 0}
player_2 = {'x': 685, 'y': 550}
ball = {'x': 350, 'y': 350, 'x_speed': 3 + 5 * random.random(), 'y_speed': 3 + 5 * random.random()}
gortakic = 0.5
gortakic_time = 0
change_time = 0
while run:
    if gortakic_time + 0.01 < time.process_time():
        gortakic_time = time.process_time()
        gortakic += (1 - gortakic) * gortakic / 200
    print(ball['x_speed'], '    ', ball['y_speed'], '             ', gortakic, '   ', gortakic_time, '   ', time.process_time())
    speed_chenging()
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        if player_2['y'] > 13:
            player_2['y'] -= 13
        else:
            player_2['y'] = 0
    if keys[pygame.K_DOWN]:
        if player_2['y'] < 537:
            player_2['y'] += 13
        else:
            player_2['y'] = 550
    if keys[pygame.K_w]:
        if player_1['y'] > 13:
            player_1['y'] -= 13
        else:
            player_1['y'] = 0
    if keys[pygame.K_s]:
        if player_1['y'] < 537:
            player_1['y'] += 13
        else:
            player_1['y'] = 550

    all_blit()
    ball_go()
