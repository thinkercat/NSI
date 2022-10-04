from operator import truediv
import pygame as pg
from pygame.locals import *
import random

pg.init()

# Génération de la fenetre
icon = pg.image.load('PyGame/MyGame/Assets/gameboy.png')

pg.display.set_icon(icon)
pg.display.set_caption("Game")             # Définir le titre de la fenetre 
height = 1000
width = 900
screen = pg.display.set_mode((width,height))   #Dimensions de la fenetre
screenBackground = (200,160,160)


#pg.mixer.music.load('MyGame\Assets\Musiques\chill.mp3')
#pg.mixer.music.play(loops = -1)

#Dimensions jouables
playScreenHeight = 900
playScreenWidht = 900
## Player variables
player = pg.image.load('PyGame/MyGame/Assets/gameboy.png')
playerRect = player.get_rect()
playerWidth = player.get_width()
playerHeight = player.get_height()
playerVelocity = 10
#Player pos on start
playerRect.x = playScreenWidht/2    
playerRect.y = playScreenHeight/2

## Battery variables
battery = pg.image.load('PyGame/MyGame/Assets/pile-verte.png')
batteryRect = battery.get_rect()
#Battery pos on start
batteryRect.x = 300
batteryRect.y = 300

## BadBattery variable
badBattery = []
badBatteryRect = [] 
badBatterySpawn = 2
def badBatteryGeneration(nombreDeBadBattery:int):      
    for nbOfBadBattery in range(nombreDeBadBattery):
        badBattery.append(pg.image.load('PyGame/MyGame/Assets/pile-rouge.png'))
        badBatteryRect.append(badBattery[nbOfBadBattery].get_rect()) 
def badBatteryRandomSpawn():
    for nbOfBadBattery in range(len(badBatteryRect)):
        badBatteryRect[nbOfBadBattery].x = random.randint(0, playScreenWidht)
        badBatteryRect[nbOfBadBattery].y = random.randint(height-playScreenHeight, playScreenHeight)
        while badBatteryRect[nbOfBadBattery].colliderect(playerRect) or badBatteryRect[nbOfBadBattery].colliderect(batteryRect):
            badBatteryRect[nbOfBadBattery].x = random.randint(0, playScreenWidht)
            badBatteryRect[nbOfBadBattery].y = random.randint(height-playScreenHeight, playScreenHeight)           
## Energy(health) variables
maxEnergy = 150
playerEnergy = 10
batteryEnergy = 10
badBatteryEnergy = 5
energyBar = [width-180,20,150,30]
energyBarColor = [255,0,0]






run = True 
while run: #Tant que run = true le jeu marche
    screen.fill(screenBackground)
    playableScreen = pg.draw.rect(screen,(0,0,0),(0,100,playScreenWidht,playScreenHeight),10)

# When player collide
    if playerRect.colliderect(batteryRect):
        batteryRect.x = random.randint(0,playScreenWidht)
        batteryRect.y = random.randint(height-playScreenHeight, playScreenHeight)
        badBatteryGeneration(badBatterySpawn)
        badBatteryRandomSpawn()
        playerEnergy += batteryEnergy
        playerVelocity += 5






# Verify player energy and state the energy bar 
    if playerEnergy < maxEnergy:

        if playerEnergy < maxEnergy//3:
            energyBarColor = [255,0,0]
        elif playerEnergy < (maxEnergy//3)*2:
            energyBarColor = [255,255,0]
        elif playerEnergy < (maxEnergy//3)*3:
            energyBarColor = [0,255,0]

        energyBar[2] = playerEnergy
        pg.draw.rect(screen, (energyBarColor),energyBar)
    if playerEnergy <= 0:
        print("Game Over")
        run = False
        pg.quit
    if playerEnergy >= maxEnergy:
        print("Game Win")
        run = False
        pg.quit
    pg.draw.rect(screen, (0,0,0),(width-180,20,150,30), 5)

# Player Movement
#    userKeyInput = pg.key.get_pressed()
#    if userKeyInput[pg.K_LEFT]:
#        if not playerRect.y.colliderect(playableScreenRect):
#            playerRect.x -= playerVelocity
#    if userKeyInput[pg.K_RIGHT]:
#        if playerRect.x - playerVelocity < playScreenWidht - playerWidth:
#            playerRect.x += playerVelocity
#    if userKeyInput[pg.K_UP]:
#       if playerRect.y + playerVelocity > height-playScreenHeight:
#            playerRect.y -= playerVelocity
#    if userKeyInput[pg.K_DOWN]:
#        if playerRect.y - playerVelocity < height - playerHeight:
#            playerRect.y += playerVelocity    

    MousePos = pg.mouse.get_pos()
    playerRect = MousePos


    for event in pg.event.get():   # dans la liste des evenements .get
        if event.type == pg.QUIT:   # si l'evenement pg.QUIT est activé
            run = False             # on arrete le jeu
            pg.quit                 # et on quitte pygame
    
    pg.time.delay(60)               # "fps"
    screen.blit(battery,batteryRect)
    for nbOfBadBattery in range(len(badBatteryRect)):
        screen.blit(badBattery[nbOfBadBattery],badBatteryRect[nbOfBadBattery])
    screen.blit(player,playerRect)

    
    pg.display.flip()
