import time
import pygame
from os import system

try:
    size = input('size(width height):  ')
    plus = input('bordersize:  ')
    bs = input('squaresize:  ')
    offall = input('augmented construction(true or false):  ')
    if offall == 'true':
        offall = True
    else:
        offall = False
    bs = int(bs)
    plus = int(plus)
    size = size.split()
    mw = int(size[0])
    mh = int(size[1])
except:
    print('Error: making another size')
    mw = 3
    mh = 3
    bs = 222
    plus = 10
    offall = False
system('cls||clear')
print('buttons:\n'
      'z,x,c - undo: lines, starts, blocks & dots\n'
      'v,b,n - linemake: coordinate 1, coordinate 2, line between 2 coordinats\n'
      'w,a,s,d - dot move: up, left, down, right\n'
      'up,left,down,right arrows - square move: up, left, down, right\n'
      '1,2,3,4,6,7 - create: dot, block, anti, triangle, double triangle, figure, anti-figure\n'
      't,g - change color: up, down\n'
      'q - viewing mode toggle\n'
      'e,r - starts: clear start, fill start\n'
      'f - clear all\n'
      'backspace - exit game\n'
      'space - half mode\n')

x = 0
y = 0
zx = 0
zy = 0
ssx = 0
ssy = 0
run = True
white = [255, 255, 255]
grey = [100, 100, 100]
blue = [100, 100, 255]
red = [255, 0, 0]
black = [0, 0, 0]
orange = [219, 159, 18]
sx = plus
sy = plus
step = bs + plus
vis = True
linemode = True
d1, d2 = [0, 0], [0, 0]
colorchange = 2
colors = [
    white,
    black,
    red,
    orange,
    blue,
    [0, 255, 0],
    [0, 0, 255],
    [255, 255, 0],
    [0, 255, 255],
    [255, 0, 255],
    grey
]

inx = 0
iny = 0
lines = []
starts = []
blocks = []
plus2 = plus // 2


def o(num):
    if num % 2 == 0:
        return 1
    else:
        return 0


def fill(scx, scy):
    dx = 0
    dy = 0
    ox = plus
    oy = plus
    for _ in range(scy):
        for _ in range(scx):
            sizex = bs * dx + ox
            sizey = bs * dy + oy
            pygame.draw.rect(window, grey, (sizex, sizey, bs, bs))
            ox += plus
            dx += 1
        oy += plus
        ox = plus
        dy += 1
        dx = 0


def sprite(x: int, y: int, sprite: list, window: pygame.display, bluec: bool, w: int, h: int):
    xp = 0
    yp = 0
    ow = bs / w - plus
    oh = bs / h - plus
    m = min(ow, oh) - plus
    save = (bs - (m * w + plus2 * w)) / 4
    ox = plus2
    oy = plus2
    for list in sprite:
        for all in list:
            bx = xp * plus + ox - (plus2 / 2) + save
            by = yp * plus + oy - (plus2 / 2) + save
            if all != '0':
                if bluec:
                    pygame.draw.rect(window, blue, [bx + x, by + y, m, m], plus2)
                else:
                    pygame.draw.rect(window, orange, [bx + x, by + y, m, m])
            ox += m
            xp += 1
        xp = 0
        yp += 1
        oy += m
        ox = plus2


mow = mw * (bs + plus)
moh = mh * (bs + plus)

pygame.init()
window = pygame.display.set_mode([mow + plus, moh + plus])
pygame.display.set_caption('witness drawer')

while run:
    window.fill(white)
    fill(mw, mh)

    for all in starts:
        pygame.draw.circle(window, white, [all[0][0], all[0][1]], plus * 2)
    for all in lines:
        if len(all) == 2:
            pygame.draw.line(window, all[1], all[0][0], all[0][1], plus)
        elif len(all) == 1:
            pygame.draw.circle(window, all[0][2], [all[0][0], all[0][1]], plus * 2 + 1)
    for all in blocks:
        if all[-1] == 'dot':
            pygame.draw.circle(window, all[2], [all[0] + plus2, all[1] + plus2], plus / 2)
        elif all[-1] == 'sqr':
            pygame.draw.rect(window, all[2], [all[0], all[1], bs / 2, bs / 2])
        elif all[-1] == 'anti':
            anti = [[all[0] + (bs / 20 * 9), all[1] + bs / 5], [all[0] + (bs / 20 * 11), all[1] + bs / 5],
                    [all[0] + (bs / 20 * 11), all[1] + bs / 2], [all[0] + (bs / 4 * 3), all[1] + bs / 10 * 7],
                    [all[0] + (bs / 6 * 4), all[1] + bs / 10 * 7.5], [all[0] + (bs / 2), all[1] + bs / 10 * 6],
                    [all[0] + (bs / 6 * 2), all[1] + bs / 10 * 7.5], [all[0] + (bs / 4 * 1), all[1] + bs / 10 * 7],
                    [all[0] + (bs / 20 * 9), all[1] + bs / 2]]

            pygame.draw.polygon(window, white, anti)
        elif all[-1] == 'tri':
            tri = [[all[0] + (bs / 2), all[1] + bs / 5],
                    [all[0] + (bs / 10 * 2), all[1] + (bs / 10 * 8)],
                    [all[0] + (bs / 10 * 8), all[1] + (bs / 10 * 8)]]
            pygame.draw.polygon(window, orange, tri)
        elif all[-1] == 'trid':
            tri = [[all[0] + (bs / 2), all[1] + (bs / 10 * 8)],
                    [all[0] + (bs / 6 * 2), all[1] + (bs / 10 * 5)],
                    [all[0] + (bs / 10 * 2), all[1] + (bs / 10 * 8)],
                    [all[0] + (bs / 10 * 8), all[1] + (bs / 10 * 8)],
                    [all[0] + (bs / 6 * 4), all[1] + (bs / 10 * 5)]]
            pygame.draw.polygon(window, orange, tri)
        elif all[-1] == 'fig':
            sprite(all[0], all[1], all[2], window, False, all[3], all[4])
        elif all[-1] == 'figb':
            sprite(all[0], all[1], all[2], window, True, all[3], all[4])
        elif all[-1] == 'cl':
            pygame.draw.rect(window, grey, (all[0], all[1], plus, plus))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if vis:
                if event.key == pygame.K_LEFT:
                    if x != 0:
                        if linemode:
                            zx -= 10
                            x -= step
                        elif not linemode:
                            zx -= 5
                            x -= step / 2
                elif event.key == pygame.K_RIGHT:
                    if x != mow:
                        if linemode:
                            zx += 10
                            x += step
                        elif not linemode:
                            zx += 5
                            x += step / 2
                elif event.key == pygame.K_DOWN:
                    if y != moh:
                        if linemode:
                            zy += 10
                            y += step
                        elif not linemode:
                            zy += 5
                            y += step / 2
                elif event.key == pygame.K_UP:
                    if y != 0:
                        if linemode:
                            zy -= 10
                            y -= step
                        elif not linemode:
                            zy -= 5
                            y -= step / 2

                if event.key == pygame.K_a:
                    if sx != plus:
                        sx -= step
                elif event.key == pygame.K_d:
                    if sx != mow - step + plus:
                        sx += step
                elif event.key == pygame.K_s:
                    if sy != moh - step + plus:
                        sy += step
                elif event.key == pygame.K_w:
                    if sy != plus:
                        sy -= step

            if event.key == pygame.K_e:
                if (zy % 10 != 5 or zx % 10 != 5) or offall:
                    if not [[x + (plus2 - 1), y + (plus2 - 1)]] in starts:
                        starts.append([[x + (plus2 - 1), y + (plus2 - 1)]])

            elif event.key == pygame.K_r:
                if [[x + plus2 - 1, y + plus2 - 1]] in starts:
                    if not [[x + (plus2 - 1), y + (plus2 - 1), colors[colorchange]]] in lines:
                        lines.append([[x + (plus2 - 1), y + (plus2 - 1), colors[colorchange]]])

            if event.key == pygame.K_q:
                if vis:
                    vis = False
                elif not vis:
                    vis = True

            elif event.key == pygame.K_BACKSPACE:
                run = False
            elif event.key == pygame.K_SPACE:
                if linemode:
                    linemode = False
                elif not linemode:
                    if zx % 10 != plus and zx % 10 != -plus:
                        if zy % 10 != plus and zy % 10 != -plus:
                            linemode = True

            elif event.key == pygame.K_z:
                if len(lines) != 0:
                    del lines[-1]
            elif event.key == pygame.K_x:
                if len(starts) != 0:
                    del starts[-1]
            elif event.key == pygame.K_c:
                if len(blocks) != 0:
                    del blocks[-1]

            elif event.key == pygame.K_v:
                if (zy % 10 != 5 or zx % 10 != 5) or offall:
                    d1 = [x + plus2 - o(plus), y + plus2 - o(plus)]
            elif event.key == pygame.K_b:
                if (zy % 10 != 5 or zx % 10 != 5) or offall:
                    d2 = [x + plus2 - o(plus), y + plus2 - o(plus)]
            elif event.key == pygame.K_n:
                if d1 == d2:
                    pass
                elif (d1[0] == d2[0] or d1[1] == d2[1]) or offall:
                    if not [[d1, d2], colors[colorchange]] in lines or not [[d2, d1], colors[colorchange]] in lines:
                        lines.append([[d1, d2], colors[colorchange]])
            if event.key == pygame.K_f:
                lines = []
                starts = []
                blocks = []
            elif event.key == pygame.K_g:
                if colorchange != 0:
                    colorchange -= 1
            elif event.key == pygame.K_t:
                if colorchange != len(colors) - 1:
                    colorchange += 1
            elif event.key == pygame.K_1:
                if zy % 10 != 5 or zx % 10 != 5 or offall:
                    if not [x, y, colors[colorchange], 'dot'] in blocks:
                        blocks.append([x, y, colors[colorchange], 'dot'])
            elif event.key == pygame.K_2:
                if not [sx + bs / 4 + 1, sy + bs / 4 + 1, 'sqr'] in blocks:
                    blocks.append([sx + bs / 4 + 1, sy + bs / 4 + 1, colors[colorchange], 'sqr'])
            elif event.key == pygame.K_3:
                if not [sx, sy, 'anti'] in blocks:
                    blocks.append([sx, sy, 'anti'])
            elif event.key == pygame.K_4:
                if not [sx, sy,  'tri'] in blocks:
                    blocks.append([sx, sy, 'tri'])
            elif event.key == pygame.K_5:
                if not [sx, sy, 'trid'] in blocks:
                    blocks.append([sx, sy, 'trid'])
            elif event.key == pygame.K_6 or event.key == pygame.K_7:
                d = True
                if event.key == pygame.K_7:
                    b = 'figb'
                elif event.key == pygame.K_6:
                    b = 'fig'
                try:
                    sizew = int(input('width(in blocks):  '))
                    sizeh = int(input('height(in blocks):  '))
                except:
                    print('Error')
                    d = False
                    break
                ad = []
                for f in range(sizeh):
                    d = input('%d: blocks(0 is clear, 1 is fill):  ' % (f + 1)).split()
                    if len(d) != sizew:
                        print('Error')
                        d = False
                        break
                    else:
                        ad.append(d)
                if d:
                    if not [sx, sy, ad, sizew, sizew, b] in blocks:
                        blocks.append([sx, sy, ad, sizew, sizeh, b])
            elif event.key == pygame.K_i:
                if zy % 10 != 5 or zx % 10 != 5:
                    if not [x, y, 'cl'] in blocks:
                        blocks.append([x, y, 'cl'])

    if vis:
        pygame.draw.rect(window, colors[colorchange], (x, y, plus, plus))
        pygame.draw.rect(window, colors[colorchange], (sx, sy, bs, bs), plus)
    pygame.display.flip()
    pygame.display.update()
pygame.quit()
