import pygame


def recolor(col):
    if col == 0:
        return 1
    elif col == 1:
        return 2
    return 0


color = 2
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
m = 2
circles = []
n, k = list(map(int, input().split()))
for i in range(k):
    m = recolor(m)
    circles.append(colors[m])
pygame.init()
size = width, height = k * n, k * n
screen = pygame.display.set_mode(size)
screen.fill((0, 0, 0))
otstup = 0
for i in list(reversed(circles)):
    pygame.draw.ellipse(screen, i, (otstup // 2, otstup // 2, width - otstup, height - otstup))
    otstup += n
pygame.display.flip()
# ожидание закрытия окна:
while pygame.event.wait().type != pygame.QUIT:
    pass
# завершение работы:
pygame.quit()