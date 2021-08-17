import pygame
import time
my_dict = {1: (3, 150), 2: (78, 150), 3: (150, 150), 4: (3, 78), 5: (78, 78),
           6: (150, 78), 7: (3, 3), 8: (78, 3), 9: (150, 3)}
my_dict_x = []
my_dict_o = []
winer = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [7, 4, 1], [8, 5, 2], [9, 6, 3], [7, 5, 3, ], [9, 5, 1]]
pygame.init()
win = pygame.display.set_mode((225, 225))
pygame.display.set_caption("Game")
run = True
background = pygame.image.load("img/black.jpg")
x = pygame.image.load("img/x.jpg")
o = pygame.image.load("img/o.jpg")
x_color = pygame.image.load("img/x_color.jpg")
o_color = pygame.image.load("img/o_color.jpg")
clock = pygame.time.Clock()
while run:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.blit(background, (0, 0))

    for i in my_dict_x:
        win.blit(x, my_dict[i])
    for i in my_dict_o:
        win.blit(o, my_dict[i])
    pygame.display.update()

    while True:
        try:
            c = input('input x')
            assert len(c) == 1
            c = int(c)
            if c in my_dict_o or c in my_dict_x:
                assert 1 == 2
            my_dict_x.append(c)
            win.blit(x, my_dict[c])
            break
        except Exception:
            pass

    pygame.display.update()

    for i in winer:
        t = True
        for w in i:
            if w not in my_dict_x:
                t = False
                break
        if t is True:
            p = {'x': i}
            print('x win')
            break
    if t is True:
        break
    if len(my_dict_x) + len(my_dict_o) == 9:
        p = False
        break

    while True:
        try:
            c = input('input o')
            assert len(c) == 1
            c = int(c)
            if c in my_dict_o or c in my_dict_x:
                assert 1 == 2
            my_dict_o.append(c)
            win.blit(o, my_dict[c])
            break
        except Exception:
            pass
    pygame.display.update()

    for i in winer:
        t = True
        for w in i:
            if w not in my_dict_o:
                t = False
                break
        if t is True:
            p = {'o': i}
            print('o win')
            break
    if t is True:
        break

if p is not False:
    for i in range(4):
        for b in list(p.values())[0]:
            if list(p.keys())[0] == 'x':
                win.blit(x_color, my_dict[b])
            else:
                win.blit(o_color, my_dict[b])
        pygame.display.update()

        time.sleep(0.5)

        for h in list(p.values())[0]:
            if list(p.keys())[0] == 'x':
                win.blit(x, my_dict[h])
            else:
                win.blit(o, my_dict[h])
        pygame.display.update()

        time.sleep(0.5)
else:
    print("vvv")


pygame.quit()
