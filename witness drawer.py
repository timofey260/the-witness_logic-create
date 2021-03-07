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
    mw = 20
    mh = 20
    bs = 35
    plus = 5
    offall = False
system('cls||clear')
print('buttons:\n'
      'z,x,c - undo: lines, starts, blocks & dots\n'
      'v,b,n,m - linemake: coordinate 1, coordinate 2, line between 2 coordinats, clear line between 2 coordinats\n'
      'w,a,s,d - dot move: up, left, down, right\n'
      'up,left,down,right arrows - square move: up, left, down, right\n'
      '1,2,3,4,5 - create: dot, block, anti, triangle, double triangle\n'
      't,g - change color: up, down\n'
      'q - viewing mode toggle\n'
      'e,r - starts: clear start, fill start\n'
      'f - clear all\n'
      'y,h - rotation: right, left\n'
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
rotation = 0
colors = [
    white,
    black,
    red,
    orange,
    [0, 255, 0],
    [0, 0, 255],
    [255, 255, 0],
    [0, 255, 255],
    [255, 0, 255]
]

inx = 0
iny = 0
lines = []
starts = []
blocks = []
steps = 0
plus2 = plus // 2


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


mow = mw * (bs + plus)
moh = mh * (bs + plus)

pygame.init()
window = pygame.display.set_mode([mow + plus, moh + plus])
pygame.display.set_caption('witness drawer')

while run:
    window.fill(white)
    fill(mw, mh)

    for all in starts:
        if len(all) == 2:
            pygame.draw.line(window, white, all[0], all[1], plus)
        elif len(all) == 1:
            pygame.draw.circle(window, white, [all[0][0], all[0][1]], plus * 2)
    for all in lines:
        if len(all) == 2:
            pygame.draw.line(window, blue, all[0], all[1], plus)
        elif len(all) == 1:
            pygame.draw.circle(window, blue, [all[0][0], all[0][1]], plus * 2 + 1)
    for all in blocks:
        if all[-1] == 'dot':
            pygame.draw.circle(window, black, [all[0] + plus2, all[1] + plus2], plus / 2)
        elif all[-1] == 'sqr':
            pygame.draw.rect(window, all[2], [all[0], all[1], bs / 2, bs / 2])
        elif all[-1] == 'anti':
            anti = [[all[0] + (bs / 20 * 9), all[1] + bs / 5], [all[0] + (bs / 20 * 11), all[1] + bs / 5],
                    [all[0] + (bs / 2 + 1), all[1] + bs / 2], [all[0] + (bs / 4 * 3), all[1] + bs / 10 * 7],
                    [all[0] + (bs / 6 * 4), all[1] + bs / 10 * 7.5], [all[0] + (bs / 2), all[1] + bs / 10 * 6],
                    [all[0] + (bs / 6 * 2), all[1] + bs / 10 * 7.5], [all[0] + (bs / 4 * 1), all[1] + bs / 10 * 7],
                    [all[0] + (bs / 2 - 1), all[1] + bs / 2]]

            pygame.draw.polygon(window, white, anti)
        elif all[-1] == 'tri':
            if all[2] == 0:
                tri = [[all[0] + (bs / 2), all[1] + bs / 5],
                       [all[0] + (bs / 10 * 2), all[1] + (bs / 10 * 8)],
                       [all[0] + (bs / 10 * 8), all[1] + (bs / 10 * 8)]]
            elif all[2] == 1:
                tri = [[all[0] + (bs / 10 * 2), all[1] + (bs / 10 * 2)],
                       [all[0] + (bs / 10 * 8), all[1] + (bs / 10 * 5)],
                       [all[0] + (bs / 10 * 2), all[1] + (bs / 10 * 8)]]
            elif all[2] == 2:
                tri = [[all[0] + (bs / 2), all[1] + bs / 10 * 8],
                       [all[0] + (bs / 10 * 2), all[1] + (bs / 10 * 2)],
                       [all[0] + (bs / 10 * 8), all[1] + (bs / 10 * 2)]]
            elif all[2] == 3:
                tri = [[all[0] + (bs / 10 * 8), all[1] + (bs / 10 * 2)],
                       [all[0] + (bs / 10 * 2), all[1] + (bs / 10 * 5)],
                       [all[0] + (bs / 10 * 8), all[1] + (bs / 10 * 8)]]
            pygame.draw.polygon(window, orange, tri)
        elif all[-1] == 'trid':
            if all[2] == 0:
                tri = [[all[0] + (bs / 2), all[1] + (bs / 10 * 8)],
                       [all[0] + (bs / 6 * 2), all[1] + (bs / 10 * 5)],
                       [all[0] + (bs / 10 * 2), all[1] + (bs / 10 * 8)],
                       [all[0] + (bs / 10 * 8), all[1] + (bs / 10 * 8)],
                       [all[0] + (bs / 6 * 4), all[1] + (bs / 10 * 5)]]
            elif all[2] == 1:
                tri = [[all[0] + (bs / 10 * 2), all[1] + (bs / 10 * 2)],
                       [all[0] + (bs / 10 * 5), all[1] + (bs / 6 * 2)],
                       [all[0] + (bs / 10 * 2), all[1] + (bs / 10 * 5)],
                       [all[0] + (bs / 10 * 5), all[1] + (bs / 6 * 4)],
                       [all[0] + (bs / 10 * 2), all[1] + (bs / 10 * 8)]]
            elif all[2] == 2:
                tri = [[all[0] + (bs / 2), all[1] + (bs / 10 * 2)],
                       [all[0] + (bs / 6 * 2), all[1] + (bs / 10 * 5)],
                       [all[0] + (bs / 10 * 2), all[1] + (bs / 10 * 2)],
                       [all[0] + (bs / 10 * 8), all[1] + (bs / 10 * 2)],
                       [all[0] + (bs / 6 * 4), all[1] + (bs / 10 * 5)]]
            elif all[2] == 3:
                tri = [[all[0] + (bs / 10 * 8), all[1] + (bs / 10 * 2)],
                       [all[0] + (bs / 10 * 5), all[1] + (bs / 6 * 2)],
                       [all[0] + (bs / 10 * 8), all[1] + (bs / 10 * 5)],
                       [all[0] + (bs / 10 * 5), all[1] + (bs / 6 * 4)],
                       [all[0] + (bs / 10 * 8), all[1] + (bs / 10 * 8)]]
            pygame.draw.polygon(window, orange, tri)
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
                    if not [[x + (plus2 - 1), y + (plus2 - 1)]] in lines:
                        lines.append([[x + (plus2 - 1), y + (plus2 - 1)]])

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
                    d1 = [x + plus2 - 1, y + plus2 - 1]
            elif event.key == pygame.K_b:
                if (zy % 10 != 5 or zx % 10 != 5) or offall:
                    d2 = [x + plus2 - 1, y + plus2 - 1]
            elif event.key == pygame.K_n:
                if d1 == d2:
                    pass
                elif (d1[0] == d2[0] or d1[1] == d2[1]) or offall:
                    if not [d1, d2] in lines or not [d2, d1] in lines:
                        lines.append([d1, d2])

            elif event.key == pygame.K_m:
                if d1 == d2:
                    pass
                elif (d1[0] == d2[0] or d1[1] == d2[1]) or offall:
                    if not [d1, d2] in lines or not [d2, d1] in lines:
                        starts.append([d1, d2])
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

            elif event.key == pygame.K_y:
                rotation -= 1
                if rotation == -1:
                    rotation = 3
            elif event.key == pygame.K_h:
                rotation += 1
                if rotation == 4:
                    rotation = 0
            elif event.key == pygame.K_1:
                if zy % 10 != 5 or zx % 10 != 5:
                    if not [x, y, 'dot'] in blocks:
                        blocks.append([x, y, 'dot'])
            elif event.key == pygame.K_2:
                if not [sx + bs / 4 + 1, sy + bs / 4 + 1, 'sqr'] in blocks:
                    blocks.append([sx + bs / 4 + 1, sy + bs / 4 + 1, colors[colorchange], 'sqr'])
            elif event.key == pygame.K_3:
                if not [sx, sy, 'anti'] in blocks:
                    blocks.append([sx, sy, 'anti'])
            elif event.key == pygame.K_4:
                if not [sx, sy, rotation, 'tri'] in blocks:
                    blocks.append([sx, sy, rotation, 'tri'])
            elif event.key == pygame.K_5:
                if not [sx, sy, rotation, 'trid'] in blocks:
                    blocks.append([sx, sy, rotation, 'trid'])

    if vis:
        pygame.draw.rect(window, red, (x, y, plus, plus))
        pygame.draw.rect(window, colors[colorchange], (sx, sy, bs, bs), plus)
        if rotation == 0:
            pygame.draw.rect(window, colors[colorchange], (sx + (bs / 2) - plus2, sy + plus - plus2, plus, plus), plus)
        elif rotation == 1:
            pygame.draw.rect(window, colors[colorchange], (sx + bs - plus, sy + bs / 2 - plus2, plus, plus), plus)
        elif rotation == 2:
            pygame.draw.rect(window, colors[colorchange], (sx + (bs / 2) - plus2, sy + bs - plus - plus2, plus, plus),
                             plus)
        elif rotation == 3:
            pygame.draw.rect(window, colors[colorchange], (sx + plus - plus, sy + bs / 2 - plus2, plus, plus), plus)

    pygame.display.flip()
    pygame.display.update()
pygame.quit()
