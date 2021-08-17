import pygame
import time
import random


def karucel_git(a, b):
    git.append([])
    r = random.randint(1, 4)
    print(type(a))
    s = random.randint(0, 5)
    for i in range(r):
        del a[s]
    for i in a:
        git[-1].append({})
        git[-1][-1]['kordinat'] = i
        git[-1][-1]['uxxutyun'] = b
        git[-1].append(time.process_time())


git = []
pygame.init()
win = pygame.display.set_mode((410, 410))
pygame.display.set_caption("Game")
background = pygame.image.load("img/background.jpg")
white = pygame.image.load("img/white.jpg")
red = pygame.image.load("img/red.jpg")
run = True
clock = pygame.time.Clock()
cubs_time = -1
cubs = []

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    clock.tick(30)
    win.blit(background, (0, 0))
    for x in range(0, 400, 50):
        for y in range(0, 400, 50):
            win.blit(white, (x+10, y+10))
    for a in git:
        for x in a:
            win.blit(red, x['kordinat'])
    if cubs_time + 1 < time.process_time():
        cubs_time = time.process_time()
        uxxadziq_horizonakan = random.randint(1, 2)
        if uxxadziq_horizonakan == 1:
            verev_nerqev = random.randint(1, 2)
            if verev_nerqev == 1:
                karucel_git([[10, 10], [10, 60], [10, 110], [10, 160], [10, 210], [10, 260], [10, 310], [10, 360]], 'verev')
            else:
                karucel_git([[360, 10], [360, 60], [360, 110], [360, 160], [360, 210], [360, 260], [360, 310], [360, 360]], 'nerqev')
        else:
            aj_dzax = random.randint(1, 2)
            if aj_dzax == 1:
                karucel_git([[10, 10], [10, 60], [10, 110], [10, 160], [10, 210], [10, 260], [10, 310], [10, 360]], 'aj')
            else:
                karucel_git([[360, 10], [360, 60], [360, 110], [360, 160], [360, 210], [360, 260], [360, 310], [360, 360]], 'dzax')
    time.sleep(0.1)














    pygame.display.update()


