import sys,time,os #import sys for exiting, time for waiting, os for hiding support prompt.

os.environ['PYGAME_HIDE_SUPPORT_PROMPT']="hide" #hide support prompt

import pygame #import pygame

pygame.init() #initiate pygame
screen=pygame.display.set_mode([700,700]) #set pygame display
pygame.display.set_caption("Scrolling platformer") #set caption

playerr=pygame.image.load("C:/Users/Rainbow/Documents/GitHub/scrolling-platformer/player.png") #load file
playerr.set_colorkey((255,255,255)) #set colourkey
playerl=pygame.transform.flip(playerr,True,False) #make player left

bottom=pygame.mask.from_threshold(pygame.image.load("C:/Users/Rainbow/Documents/GitHub/scrolling-platformer/bottom.png"),(0,0,0),(1,1,1)) #bottom mask
side=pygame.mask.from_threshold(pygame.image.load("C:/Users/Rainbow/Documents/GitHub/scrolling-platformer/side.png"),(0,0,0),(1,1,1)) #side mask
top=pygame.mask.from_threshold(pygame.image.load("C:/Users/Rainbow/Documents/GitHub/scrolling-platformer/top.png"),(0,0,0),(1,1,1)) #top mask

levelpic=None #set the level picture

groundmask=None #the ground mask
lavamask=None #lava mask
jumpymask=None #jumpy mask
fastleftmask=None #<- mask
fastrightmask=None #-> mask
watermask=None #water mask
shrinkmask=None #small mask
normalmask=None #big mask
winmask=None #win mask

playermask=pygame.mask.Mask((50,50),True) #player mask

velx=0 #x speed
vely=0 #y speed
lorr=True #left or right
level=1 #level

def loadlevel(): #load the level
  try: #try to
    global levelpic,groundmask,lavamask,jumpymask,fastleftmask,fastrightmask,watermask,shrinkmask,normalmask,winmask #make all of these global
    
    levelpic=pygame.image.load(f"C:/Users/Rainbow/Documents/GitHub/scrolling-platformer/levels/{level}.png") #level picture
    
    #all of the next ones are making the level masks
    groundmask=pygame.mask.from_threshold(levelpic,(0,0,0),(1,1,1))
    lavamask=pygame.mask.from_threshold(levelpic,(255,0,0),(1,1,1))
    jumpymask=pygame.mask.from_threshold(levelpic,(255,255,100),(1,1,1))
    fastleftmask=pygame.mask.from_threshold(levelpic,(0,255,0),(1,1,1))
    fastrightmask=pygame.mask.from_threshold(levelpic,(255,0,255),(1,1,1))
    watermask=pygame.mask.from_threshold(levelpic,(0,255,255),(1,1,1))
    shrinkmask=pygame.mask.from_threshold(levelpic,(0,100,0),(1,1,1))
    normalmask=pygame.mask.from_threshold(levelpic,(0,0,100),(1,1,1))
    winmask=pygame.mask.from_threshold(levelpic,(255,255,0),(1,1,1))
  except: #if the file does not exist, which means you won
    pygame.quit() #quit pygame
    
    input("YOU WIN") #print you win
    
    sys.exit() #exit
def reset(): #reset position and speed
  global screenposx,screenposy,velx,vely #global variables
  
  screenposx=-300 #set position to be -300
  screenposy=3100 #and 3100
  
  velx=0 #x speed=0
  vely=0 #y speed=0
def up(): #go up
  global screenposy #global y position
  
  while bool(groundmask.overlap_area(bottom,(screenposx+300,screenposy+299))): #while touching ground
    screenposy-=1 #go up

while True: #level loop
  loadlevel() #load the level
  reset() #reset position
  
  while True:
    #bottom, side, top touching ground
    tbottom=bool(groundmask.overlap_area(bottom,(screenposx+300,screenposy+300)))
    tside=bool(groundmask.overlap_area(side,(screenposx+299,screenposy+300)))
    ttop=bool(groundmask.overlap_area(top,(screenposx+300,screenposy+299)))
    
    win=bool(winmask.overlap_area(playermask,(screenposx+300,screenposy+300))) #touching win
    lava=bool(lavamask.overlap_area(playermask,(screenposx+300,screenposy+300))) #touching lava
    jumpy=bool(jumpymask.overlap_area(playermask,(screenposx+300,screenposy+300))) #touching jumpy
    
    screen.fill((255,255,255)) #fill screen
    
    for event in pygame.event.get(): #for every event
      if event.type==pygame.QUIT: #if you quit
        pygame.quit() #quit pygame
        sys.exit() #exit
    
    if screenposx<-300: #if you go past boundary
      screenposx=-300 #go back to boundary
      velx=0 #set speed=0
    if screenposx>3150: #other boundary
      screenposx=3150 #go back
      velx=0 #freeze speed
    
    screen.blit(levelpic,(-screenposx,-round(screenposy))) #draw the background

    #friction
    if velx>=2: #going right
      velx-=2 #slow down
    elif velx<=-2: #going left
      velx+=2 #slow down
    else: #going slow
      velx=0 #stop
    
    if not tbottom: #if bottom not touching ground
      vely-=2 #go down    
    else: #if bottom touching ground
      vely=0 #stop
      up() #go up
    
    if ttop and not tbottom: #if up touching but not down touching
      vely=-vely #reverse

    keys=pygame.key.get_pressed() #the pressed keys
    if keys[pygame.K_UP] and tbottom: #if pressing up and touching bottom
      vely+=30 #go up
    if keys[pygame.K_LEFT] and velx>=-30: #if going left and less than max speed
      velx-=3 #go left
      lorr=False #face left
    if keys[pygame.K_RIGHT] and velx<=30: #if going right and less than max speed
      velx+=3 #go right
      lorr=True #face right
    
    if jumpy: #if touching jumpy
      vely+=20 #jump
    
    screenposx+=velx #change by x velocity
    screenposy-=vely #change by y velocity
    
    if lorr: #if going right
      screen.blit(playerr,(300,300)) #draw character
    else: #if left
      screen.blit(playerl,(300,300)) #draw character
    
    if win: #if win level
      break #break
    
    if lava: #if touch lava
      reset() #reset level
    
    pygame.display.flip() #flip screen
    
    time.sleep(0.02) #slow down game
  level+=1 #go to next level
