from operator import truediv
import pygame as pg
from pygame.locals import *
import random

pg.init()

# Génération de la fenetre
icon = pg.image.load('NSI\PyGame\MyGame\Assets\gameboy_icon.png')

pg.display.set_icon(icon)
pg.display.set_caption("Game")             # Définir le titre de la fenetre 
height = 720
width = 1080
screen = pg.display.set_mode((width,height))   #Dimensions de la fenetre
screenBackground = (255,255,255)


pg.mixer.music.load('NSI\PyGame\MyGame\Assets\Musiques\chill.mp3')
pg.mixer.music.play(loops = -1)



player = pg.image.load('NSI\PyGame\MyGame\Assets\gameboy_icon.png')
playerRect = player.get_rect()
playerWidth = player.get_width()
playerHeight = player.get_height()
playerVelocity = 10

battery = pg.image.load('NSI\PyGame\MyGame\Assets\energy-lila.png')
batteryRect = battery.get_rect()

maxEnergy = 150
playerEnergy = 0
batteryEnergy = 10
energyBar = [width-180,20,150,30]



run = True 
while run: #Tant que run = true le jeu marche
    screen.fill(screenBackground)
    pg.draw.rect(screen, (0,0,0),(width-180,20,150,30), 5)


# Energy Spawn
    if batteryRect.colliderect(playerRect):
        batteryRect.x = random.randint(10,200)
        batteryRect.y = random.randint(10,200)
        playerEnergy += batteryEnergy

    if playerEnergy < 150:
        energyBar[2] = playerEnergy
        pg.draw.rect(screen, (255,0,0),energyBar)
    else:
        print("Game Win")


# Player Movement
    userKeyInput = pg.key.get_pressed()
    if userKeyInput[pg.K_LEFT]:
        if playerRect.x > 0:
            playerRect.x -= playerVelocity
    if userKeyInput[pg.K_RIGHT]:
        if playerRect.x < width - playerWidth:
            playerRect.x += playerVelocity
    if userKeyInput[pg.K_UP]:
        if playerRect.y > 0:
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
