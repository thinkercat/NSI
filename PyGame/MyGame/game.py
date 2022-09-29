from operator import truediv
import pygame as pg
from pygame.locals import *
import random

pg.init()

# Génération de la fenetre
icon = pg.image.load('PyGame/MyGame/Assets/gameboy_icon.png')

pg.display.set_icon(icon)
pg.display.set_caption("Game")             # Définir le titre de la fenetre 
height = 1000
width = 900
screen = pg.display.set_mode((width,height))   #Dimensions de la fenetre
screenBackground = (200,160,160)


#pg.mixer.music.load('NSI\PyGame\MyGame\Assets\Musiques\chill.mp3')
#pg.mixer.music.play(loops = -1)

#Dimensions jouables
playScreenHeight = 900
playScreenWidht = 900

## Player variables
player = pg.image.load('PyGame/MyGame/Assets/gameboy_icon.png')
playerRect = player.get_rect()
playerWidth = player.get_width()
playerHeight = player.get_height()
playerVelocity = 10
#Player pos on start
playerRect.x = playScreenWidht/2    
playerRect.y = playScreenHeight/2

## Battery variables
battery = pg.image.load('PyGame/MyGame/Assets/energy-lila.png')
batteryRect = battery.get_rect()
#Battery pos on start
batteryRect.x = 300
batteryRect.y = 300

## Energy(health) variables
maxEnergy = 150
playerEnergy = 0
batteryEnergy = 10
energyBar = [width-180,20,150,30]



run = True 
while run: #Tant que run = true le jeu marche
    screen.fill(screenBackground)


# Energy Spawn
    if batteryRect.colliderect(playerRect):
        batteryRect.x = random.randint(0,playScreenWidht)
        batteryRect.y = random.randint(height-playScreenHeight, playScreenHeight)
        playerEnergy += batteryEnergy
        playerVelocity += 2

# Verify if player win and state the energy bar 
    if playerEnergy < maxEnergy:
        energyBar[2] = playerEnergy
        pg.draw.rect(screen, (0,255,100),energyBar)
    else:
        print("Game Win")
        run = False
        pg.quit
    pg.draw.rect(screen, (0,0,0),(width-180,20,150,30), 5)

# Player Movement
    userKeyInput = pg.key.get_pressed()
    if userKeyInput[pg.K_LEFT]:
        if playerRect.x > 0:
            playerRect.x -= playerVelocity
    if userKeyInput[pg.K_RIGHT]:
        if playerRect.x < playScreenWidht - playerWidth:
            playerRect.x += playerVelocity
    if userKeyInput[pg.K_UP]:
        if playerRect.y > height-playScreenHeight:
            playerRect.y -= playerVelocity
    if userKeyInput[pg.K_DOWN]:
        if playerRect.y < height - playerHeight:
            playerRect.y += playerVelocity    





    for event in pg.event.get():   # dans la liste des evenements .get
        if event.type == pg.QUIT:   # si l'evenement pg.QUIT est activé
            run = False             # on arrete le jeu
            pg.quit                 # et on quitte pygame
    
    pg.time.delay(30)               # "fps"
    screen.blit(battery,batteryRect)
    screen.blit(player,playerRect)
    pg.display.flip()
