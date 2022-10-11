from operator import truediv
import string
import pygame as pg
from pygame.locals import *
import random
from settings import *

pg.init()

## CLASSES
class Player():
    """ 
    Définit les parametres du joueur
    """
    def __init__(self,spriteFile:string=ASSET+'gameboy.png',energy:int=10,velocity:int=10):
        self.sprite = pg.image.load(spriteFile)
        self.rect = self.sprite.get_rect()
        self.width = self.sprite.get_width()
        self.height = self.sprite.get_height()
        self.energy = energy
        self.velocity = velocity

    def Movements(self):

        userKeyInput = pg.key.get_pressed()

        if userKeyInput[pg.K_LEFT]: 
            self.rect.x -= self.velocity

        if userKeyInput[pg.K_RIGHT]:    
            self.rect.x += self.velocity

        if userKeyInput[pg.K_UP]:   
            self.rect.y -= self.velocity

        if userKeyInput[pg.K_DOWN]:
            self.rect.y += self.velocity    

        if self.rect.x < 0:
            self.rect.x = 0

        if self.rect.x >= WIDTH - self.width:
            self.rect.x = WIDTH - self.width

        if self.rect.y < 100:
            self.rect.y = 100
        if self.rect.y >= HEIGHT - self.height:
            self.rect.y = HEIGHT - self.height

















player1 = Player()


#################################################################################### 
# Génération de la fenetre
icon = pg.image.load(ASSET+'gameboy.png')

pg.display.set_icon(icon)
pg.display.set_caption("Game")             # Définir le titre de la fenetre 

screen = pg.display.set_mode((WIDTH,HEIGHT))   #Dimensions de la fenetre
screenBackground = (200,160,160)


#pg.mixer.music.load('NSI/PyGame/MyGame\Assets\Musiques\chill.mp3')
#pg.mixer.music.play(loops = -1)

#Dimensions jouables
playScreenHeight = 900
playScreenWidht = 900
## Player variables
player1.rect.x = playScreenWidht/2    
player1.rect.y = playScreenHeight/2

## Battery variables
battery = pg.image.load(ASSET+'pile-verte.png')
batteryRect = battery.get_rect()
batteryRect.x = 300
batteryRect.y = 300


## BadBattery variable
badBattery = []
badBatteryRect = [] 
badBatterySpawn = 2

def badBatteryGeneration(nombreDeBadBattery:int):      
    for nbOfBadBattery in range(nombreDeBadBattery):
        badBattery.append(pg.image.load(ASSET+'pile-rouge.png'))
        badBatteryRect.append(badBattery[nbOfBadBattery].get_rect()) 
def badBatteryRandomSpawn():
    for nbOfBadBattery in range(len(badBatteryRect)):
        badBatteryRect[nbOfBadBattery].x = random.randint(0, playScreenWidht)
        badBatteryRect[nbOfBadBattery].y = random.randint(HEIGHT-playScreenHeight, playScreenHeight)
        while badBatteryRect[nbOfBadBattery].colliderect(player1.rect) or badBatteryRect[nbOfBadBattery].colliderect(batteryRect):
            badBatteryRect[nbOfBadBattery].x = random.randint(0, playScreenWidht)
            badBatteryRect[nbOfBadBattery].y = random.randint(HEIGHT-playScreenHeight, playScreenHeight)           
## Energy(health) variables
maxEnergy = 150
playerEnergy = 10
batteryEnergy = 10
badBatteryEnergy = 10
energyBar = [WIDTH-180,20,150,30]
energyBarColor = [255,0,0]

def InitialisationDesVariables(): # Variables on start
    #Player

    player1.rect.x = playScreenWidht/2    
    player1.rect.y = playScreenHeight/2

    #Battery
    batteryRect.x = 300
    batteryRect.y = 300

    #BadBattery
    badBattery = []
    badBatteryRect = [] 
    badBatterySpawn = 2

    #Energy
    maxEnergy = 150
    playerEnergy = 10
    batteryEnergy = 10
    badBatteryEnergy = 10
    energyBar = [WIDTH-180,20,150,30]
    energyBarColor = [255,0,0]



GamePlay = False
run = True 
while run: #Tant que run = true le jeu marche
    playerEnergy = 10
    screen.fill(screenBackground)
    playButton = pg.draw.circle(screen,(200,0,0),(WIDTH/2,HEIGHT/2),200)
    MousePress = pg.mouse.get_pressed()
    MousePos = pg.mouse.get_pos()

    if MousePress[0] & playButton.collidepoint(MousePos):
        GamePlay = True
        InitialisationDesVariables()


    while GamePlay :

        for event in pg.event.get(): 
            if event.type == pg.QUIT:
                GamePlay = False  
                run = False            
                pg.quit






        screen.fill(screenBackground)
    # When player collide
        if player1.rect.colliderect(batteryRect): 
            batteryRect.x = random.randint(0,playScreenWidht)
            batteryRect.y = random.randint(HEIGHT-playScreenHeight, playScreenHeight)
            badBatteryGeneration(badBatterySpawn)
            badBatteryRandomSpawn()
            playerEnergy += batteryEnergy
            player1.velocity += 5

        for nbOfBadBattery in range(len(badBatteryRect)):   
            if player1.rect.colliderect(badBatteryRect[nbOfBadBattery]):
                badBatteryRandomSpawn()
                playerEnergy -= badBatteryEnergy
                player1.velocity -= 5







    # Verify player energy and state the energy bar 

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
            GamePlay = False
        if playerEnergy >= maxEnergy:   
            print("Game Win")
            GamePlay = False
        





        player1.Movements()


        pg.time.delay(60)               # "fps"
        screen.blit(battery,batteryRect)
        for nbOfBadBattery in range(len(badBatteryRect)):
            screen.blit(badBattery[nbOfBadBattery],badBatteryRect[nbOfBadBattery])
        screen.blit(player1.sprite,player1.rect)
        pg.draw.rect(screen,(0,0,0),(0,100,playScreenWidht,playScreenHeight),10)
        pg.draw.rect(screen, (0,0,0),(WIDTH-180,20,150,30), 5)

                 
        pg.display.flip()



    for event in pg.event.get():   # dans la liste des evenements .get
        if event.type == pg.QUIT:   # si l'evenement pg.QUIT est activé
            run = False             # on arrete le jeu
            pg.quit                 # et on quitte pygame
    pg.display.flip()
