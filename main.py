import pygame
import random
#initialize the pygame
pygame.init()
#create the screen
screen = pygame.display.set_mode((800, 600))
# Title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('001-space-invaders.png')
pygame.display.set_icon(icon)

#Player
playerImg = pygame.image.load('SpaceShip.png')
playerX = 370
playerY = 480
playerX_change = 0
#Enemy
enemyImg = pygame.image.load('Enemy.png')
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_change = 3
enemyY_change = 40

def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


# Game Loop
running = True
while running:
# RGB - Red,Green,Blue
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#If keystroke is proessed check whether its right or left
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerX_change = -3
        if event.key == pygame.K_RIGHT:
            playerX_change = 3
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            playerX_change = 0

#changeing  the  x coordinate when left or right key pressed
    playerX += playerX_change

#boundaries so the player does not move pass the window
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

#enemy boundary

    enemyX += enemyX_change


    if enemyX <=0:
        enemyX_change = 3
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -3
        enemyY += enemyY_change



#update each frame
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
