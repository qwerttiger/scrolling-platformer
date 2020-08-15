import sys,time,os #import sys for exiting, time for waiting, os for hiding support prompt.

os.environ['PYGAME_HIDE_SUPPORT_PROMPT']="hide" #hide support prompt

import pygame #import pygame

pygame.init() #initiate pygame
screen=pygame.display.set_mode([700,700]) #set pygame display
pygame.display.set_caption("Scrolling platformer") #set caption

playerr=pygame.image.load("C:/Users/Rainbow/Documents/GitHub/scrolling-platformer/player.png") #load file
playerr.set_colorkey((255,255,255)) #set colourkey
playerl=pygame.transform.flip(playerr,True,False) #make player left
playersr=pygame.transform.scale(playerr,(25,25)) #small player right
playersl=pygame.transform.scale(playerl,(25,25)) #small player left
playergl=pygame.transform.flip(playerl,False,True) #make player upside down left
playergr=pygame.transform.flip(playerr,False,True) #make player upside down right
playergsl=pygame.transform.flip(playersl,False,True) #make player upside down small left
playergsr=pygame.transform.flip(playersr,False,True) #make player upside down small right

bottomb=pygame.mask.from_threshold(pygame.image.load("C:/Users/Rainbow/Documents/GitHub/scrolling-platformer/bottom.png"),(0,0,0),(1,1,1)) #bottom mask
sideb=pygame.mask.from_threshold(pygame.image.load("C:/Users/Rainbow/Documents/GitHub/scrolling-platformer/side.png"),(0,0,0),(1,1,1)) #side mask
topb=pygame.mask.from_threshold(pygame.image.load("C:/Users/Rainbow/Documents/GitHub/scrolling-platformer/top.png"),(0,0,0),(1,1,1)) #top mask
bottoms=pygame.mask.from_threshold(pygame.image.load("C:/Users/Rainbow/Documents/GitHub/scrolling-platformer/bottomsmall.png"),(0,0,0),(1,1,1)) #bottom small mask
sides=pygame.mask.from_threshold(pygame.image.load("C:/Users/Rainbow/Documents/GitHub/scrolling-platformer/sidesmall.png"),(0,0,0),(1,1,1)) #side small mask
tops=pygame.mask.from_threshold(pygame.image.load("C:/Users/Rainbow/Documents/GitHub/scrolling-platformer/topsmall.png"),(0,0,0),(1,1,1)) #top small mask

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
gravitymask=None #gravity mask

playermaskb=pygame.mask.Mask((50,50),True) #player mask big
playermasks=pygame.mask.Mask((25,25),True) #player mask small

velx=0 #x speed
vely=0 #y speed
lorr=True #left or right
level=1 #level
big=True #small or big
top=None #top mask
side=None #side mask
bottom=None #bottom mask
deaths=0 #how many times you died
playermask=None #the playermask
gravity=1 #is gravity up or down?
cang=True #can switch gravity
skips=0 #number of skips

def setmask(): #define setmask
  global top,side,bottom,playermask #make these things global
  if big: #if big
    top=topb #set top mask
    side=sideb #set side mask
    bottom=bottomb #set bottom mask
    playermask=playermaskb #set playermask
  else: #if small
    top=tops #set top mask
    side=sides #set side mask
    bottom=bottoms #set bottom mask
    playermask=playermasks #set playermask
def loadlevel(): #load the level
  try: #try to
    global levelpic,groundmask,lavamask,jumpymask,fastleftmask,fastrightmask,watermask,shrinkmask,normalmask,winmask,gravitymask #make all of these global
    
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
    gravitymask=pygame.mask.from_threshold(levelpic,(255,128,0),(1,1,1))
  except: #if the file does not exist, which means you won
    pygame.quit() #quit pygame
    
    input("YOU WIN") #print you win
    
    sys.exit() #exit

def reset(): #reset position and speed
  global screenposx,screenposy,velx,vely,gravity,big #global variables
  
  screenposx=-300 #set position to be -300
  screenposy=3100 #and 3100
  
  velx=0 #x speed=0
  vely=0 #y speed=0
  big=True #make you big
  gravity=1 #set gravity to normal

def up(): #go up
  global screenposy #global y position
  
  while bool(groundmask.overlap_area(bottom,(screenposx+300,screenposy+299))): #while touching ground
    screenposy-=1 #go up

def down(): #go down
  global screenposy #global y position
  
  while bool(groundmask.overlap_area(top,(screenposx+300,screenposy+299))): #while touching ground
    screenposy+=1 #go down

def drawtext(text,colour,size=30,pos=(350,100)): #draws a single piece of text
  screen.blit(pygame.font.SysFont("arial",size).render(text,True,colour),(pos[0]-round(pygame.font.SysFont("arial",size).render(text,True,colour).get_width()/2),pos[1]-pygame.font.SysFont("arial",size).render(text,True,colour).get_height()/2)) #draw it

def startthing(): #the thing at the start
  global playerr,playerl,playersr,playersl #set everything to be global
  
  screen.fill((255,255,255)) #fill screen
  drawtext("scrolling platformer",(0,0,0),50) #draw text
  
  #drawing play button
  pygame.draw.rect(screen,(0,0,0),pygame.Rect((300,300),(100,100)),1)
  pygame.draw.line(screen,(0,0,0),(336,325),(336,375))
  pygame.draw.line(screen,(0,0,0),(336,325),(379,350))
  pygame.draw.line(screen,(0,0,0),(336,375),(379,350))
  pygame.draw.rect(screen,(0,0,0),pygame.Rect((100,300),(100,100)),1)
  screen.blit(playerr,(125,325)) #draw player
  
  pygame.display.flip() #flip screen
  keep_going=True #set keep_going
  
  while keep_going: #while you keep going
    for event in pygame.event.get(): #for every event
      if event.type==pygame.QUIT: #if quit
        pygame.quit() #quit
        sys.exit() #exit
      
      if event.type==pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0]>=300 and pygame.mouse.get_pos()[0]<=400 and pygame.mouse.get_pos()[1]>=300 and pygame.mouse.get_pos()[1]<=400: #if you press play
        keep_going=False #go to the main game
      
      if event.type==pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0]>=100 and pygame.mouse.get_pos()[0]<=300 and pygame.mouse.get_pos()[1]>=300 and pygame.mouse.get_pos()[1]<=400:
        #draw the screen
        screen.fill((255,255,255))
        pygame.draw.rect(screen,(0,0,0),pygame.Rect((175,325),(50,50)))
        pygame.draw.rect(screen,(255,0,0),pygame.Rect((225,325),(50,50)))
        pygame.draw.rect(screen,(0,255,0),pygame.Rect((275,325),(50,50)))
        pygame.draw.rect(screen,(0,0,255),pygame.Rect((325,325),(50,50)))
        pygame.draw.rect(screen,(255,255,0),pygame.Rect((375,325),(50,50)))
        pygame.draw.rect(screen,(255,0,255),pygame.Rect((425,325),(50,50)))
        pygame.draw.rect(screen,(0,255,255),pygame.Rect((475,325),(50,50)))
        
        pygame.display.flip() #flip display
        
        kep_going=True #lol keep_going but... yeah
        while kep_going: #while keep going
          for event in pygame.event.get(): #for every event
            if event.type==pygame.QUIT: #if you quit
              pygame.quit() #quit
              sys.exit() #exit
            if event.type==pygame.MOUSEBUTTONDOWN: #if you click
              pos=pygame.mouse.get_pos() #you find the position of the mouse
              
              if pos[1]>=325 and pos[1]<=375: #if you click in the region horizontal region where it works
                if pos[0]>=175 and pos[0]<225: #if you click on black
                  for posx in range(50): #for every column
                    for posy in range(50): #for every pixel in that column
                      if playerr.get_at((posx,posy)) not in [(255,255,255),(254,254,254)]: #if it is not blank
                        playerr.set_at((posx,posy),(0,0,0)) #set that pixel to black
                
                #the same for the other ones but with different colours
                if pos[0]>=225 and pos[0]<275:
                  for posx in range(50):
                    for posy in range(50):
                      if playerr.get_at((posx,posy)) not in [(255,255,255),(254,254,254)]:
                        playerr.set_at((posx,posy),(255,0,0))
                
                if pos[0]>=275 and pos[0]<325:
                  for posx in range(50):
                    for posy in range(50):
                      if playerr.get_at((posx,posy)) not in [(255,255,255),(254,254,254)]:
                        playerr.set_at((posx,posy),(0,255,0))
                
                if pos[0]>=325 and pos[0]<375:
                  for posx in range(50):
                    for posy in range(50):
                      if playerr.get_at((posx,posy)) not in [(255,255,255),(254,254,254)]:
                        playerr.set_at((posx,posy),(0,0,255))
                
                if pos[0]>=375 and pos[0]<425:
                  for posx in range(50):
                    for posy in range(50):
                      if playerr.get_at((posx,posy)) not in [(255,255,255),(254,254,254)]:
                        playerr.set_at((posx,posy),(255,255,0))
                
                if pos[0]>=425 and pos[0]<475:
                  for posx in range(50):
                    for posy in range(50):
                      if playerr.get_at((posx,posy)) not in [(255,255,255),(254,254,254)]:
                        playerr.set_at((posx,posy),(255,0,255))
                
                if pos[0]>=475 and pos[0]<525:
                  for posx in range(50):
                    for posy in range(50):
                      if playerr.get_at((posx,posy)) not in [(255,255,255),(254,254,254)]:
                        playerr.set_at((posx,posy),(0,255,255))
                
                playerl=pygame.transform.flip(playerr,True,False) #set the new playerl
                playersr=pygame.transform.scale(playerr,(25,25))
                playersl=pygame.transform.scale(playerl,(25,25))
                playergl=pygame.transform.flip(playerl,False,True) #make player upside down left
                playergr=pygame.transform.flip(playerr,False,True) #make player upside down right
                playergsl=pygame.transform.flip(playersl,False,True) #make player upside down small left
                playergsr=pygame.transform.flip(playersr,False,True) #make player upside down small right
              #draw the things
              screen.fill((255,255,255))
              drawtext("scrolling platformer",(0,0,0),50)
              pygame.draw.rect(screen,(0,0,0),pygame.Rect((300,300),(100,100)),1)
              pygame.draw.line(screen,(0,0,0),(336,325),(336,375))
              pygame.draw.line(screen,(0,0,0),(336,325),(379,350))
              pygame.draw.line(screen,(0,0,0),(336,375),(379,350))
              pygame.draw.rect(screen,(0,0,0),pygame.Rect((100,300),(100,100)),1)
              screen.blit(playerr,(125,325))
              
              kep_going=False #exit this loop
              pygame.display.flip() #flip screen

#real game

startthing()

while True: #level loop
  loadlevel() #load the level
  reset() #reset position
  
  while True:
    setmask()
    #bottom, side, top touching ground
    tbottom=bool(groundmask.overlap_area(bottom,(screenposx+300,screenposy+300)))
    tside=bool(groundmask.overlap_area(side,(screenposx+299,screenposy+300)))
    ttop=bool(groundmask.overlap_area(top,(screenposx+300,screenposy+299)))
    
    win=bool(winmask.overlap_area(playermask,(screenposx+300,screenposy+300))) #touching win
    lava=bool(lavamask.overlap_area(playermask,(screenposx+300,screenposy+300))) #touching lava
    jumpy=bool(jumpymask.overlap_area(playermask,(screenposx+300,screenposy+300))) #touching jumpy
    fastleft=bool(fastleftmask.overlap_area(playermask,(screenposx+300,screenposy+300))) #touching <-
    fastright=bool(fastrightmask.overlap_area(playermask,(screenposx+300,screenposy+300))) #touching ->
    water=bool(watermask.overlap_area(playermask,(screenposx+300,screenposy+300))) #touching water
    shrink=bool(shrinkmask.overlap_area(playermask,(screenposx+300,screenposy+300))) #touching shrink
    normal=bool(normalmask.overlap_area(playermask,(screenposx+300,screenposy+300))) #touching normal
    grâvity=bool(gravitymask.overlap_area(playermask,(screenposx+300,screenposy+300))) #touching normal
    
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
    
    screen.blit(levelpic,(-screenposx,-screenposy)) #draw the background
    
    #friction
    if velx>=2: #going right
      velx-=2 #slow down
    elif velx<=-2: #going left
      velx+=2 #slow down
    else: #going slow
      velx=0 #stop
    
    if tbottom and not ttop: #if bottom touching ground
      vely=0 #stop
      up() #go up
    
    if ttop and not tbottom: #if up touching but not down touching
      vely=0 #stop
      down()

    if ((not tbottom and gravity==1) or (not ttop and gravity==-1)) and not water: #if bottom not touching ground and not touching water
      vely-=2*gravity #accelerate down
    if ((not tbottom and gravity==1) or (not ttop and gravity==-1)) and water: #if bottom not touching ground and touching water
      vely=-2*gravity #go down
    
    if tside:
      velx=-velx
    
    if fastleft:
      velx-=30
    if fastright:
      velx+=30

    if grâvity and cang: #if you are touching gravity and you can switch gravity
      gravity=-gravity #reverse gravity
    cang=not grâvity #set cang to not grâvity

    if shrink: #if you are touching shrink
      big=False #become small
    if normal: #if you are touching normal
      big=True #become big
    
    keys=pygame.key.get_pressed() #the pressed keys
    if keys[pygame.K_UP] and ((tbottom and gravity==1) or (ttop and gravity==-1)) and not water and not ((tbottom and gravity==-1) or (ttop and gravity==1)): #if pressing up and touching bottom and not touching top and not in water
      vely+=30*gravity #jump
    if keys[pygame.K_UP] and water: #if going up in water
      vely=4*gravity
    if keys[pygame.K_LEFT]: #if going left
      velx-=3 #go left
      lorr=False #face left
    if keys[pygame.K_RIGHT]: #if going right
      velx+=3 #go right
      lorr=True #face right
    
    if jumpy: #if touching jumpy
      vely+=20*gravity #jump
    
    screenposx+=velx #change by x velocity
    screenposy-=vely #change by y velocity
    if gravity==1: #if going normal
      if big: #if you are big
        if lorr: #if going right
          screen.blit(playerr,(300,300)) #draw character
        else: #if left
          screen.blit(playerl,(300,300)) #draw character
      else: #if you are small
        if lorr: #if going right
          screen.blit(playersr,(300,300)) #draw character
        else: #if left
          screen.blit(playersl,(300,300)) #draw character
    else: #if flipped gravity
      if big: #if you are big
        if lorr: #if going right
          screen.blit(playergr,(300,300)) #draw character
        else: #if left
          screen.blit(playergl,(300,300)) #draw character
      else: #if you are small
        if lorr: #if going right
          screen.blit(playergsr,(300,300)) #draw character
        else: #if left
          screen.blit(playergsl,(300,300)) #draw character
    
    if win: #if win level
      break #break
    
    if lava or keys[pygame.K_r] or (screenposy>=3700 and gravity==1) or (screenposy<=0 and gravity==-1): #if touch lava
      reset() #reset level
      if not keys[pygame.K_r]: #if you either fall of the screen or touch lava
        deaths+=1 #add 1 to deaths
    
    if keys[pygame.K_p]: #if you press pause
      startthing() #do the start thing
    
    screen.blit(pygame.font.SysFont("arial",30).render("level: "+str(level)+" deaths: "+str(deaths)+" skips: "+str(skips),True,(128,128,128)),(0,0)) #draw level
    
    pygame.display.flip() #flip screen
    
    if keys[pygame.K_n]: #if you skip and can skip
      skips+=1
      break #go to next level
    
    time.sleep(0.02) #slow down game
  level+=1 #go to next level
