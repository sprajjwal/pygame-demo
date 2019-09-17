import pygame
pygame.init()

win=pygame.display.set_mode((500,500))
pygame.display.set_caption("First game")

x = 50
y = 440
width = 40
height = 60
vel = 5
run = True
isJump = False
jumpCount = 10

while run:
    pygame.time.delay(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 0:
        x -= vel

    if keys[pygame.K_RIGHT] and x < 500-width:
        x += vel
    if not isJump:
        if keys[pygame.K_UP] and y > 0:
            y-=vel
        if keys[pygame.K_DOWN] and y < 500-height:
            y+=vel
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount  >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount **2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10
    
    win.fill((0,0,0))
    pygame.draw.rect(win, (255, 222, 0), (x, y, width, height))
    pygame.display.update()

pygame.quit()