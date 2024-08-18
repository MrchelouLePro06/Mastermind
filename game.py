import pygame

pygame.init()

size_screen=(1280,720)
screen=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
fullscreen=True
clock=pygame.time.Clock()
running=True

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    screen.fill("white")

    keys=pygame.key.get_pressed()
    if keys[pygame.K_h]:
        if fullscreen:
            screen=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
            fullscreen=False
        else:
            screen=pygame.display.set_mode(size_screen)
            fullscreen=True

    pygame.display.flip()
    clock.tick(60)
pygame.quit()