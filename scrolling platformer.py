import pygame,sys,time
pygame.init()
screen=pygame.display.set_mode([700,700])
pygame.display.set_caption("Scrolling platformer")
level=1
playerr=pygame.image.load("C:/Users/Rainbow/Documents/GitHub/scrolling-platformer/player.png")
playerr.set_colorkey((255,255,255))
playerl=pygame.transform.flip(playerr,True,False)
bottom=pygame.mask.from_threshold(pygame.image.load("C:/Users/Rainbow/Documents/GitHub/scrolling-platformer/bottom.png"),(0,0,0),(1,1,1))
side=pygame.mask.from_threshold(pygame.image.load("C:/Users/Rainbow/Documents/GitHub/scrolling-platformer/side.png"),(0,0,0),(1,1,1))
top=pygame.mask.from_threshold(pygame.image.load("C:/Users/Rainbow/Documents/GitHub/scrolling-platformer/top.png"),(0,0,0),(1,1,1))
levelpic=None
groundmask=None
lavamask=None
jumpymask=None
fastleftmask=None
fastrightmask=None
watermask=None
shrinkmask=None
normalmask=None
winmask=None
playermask=pygame.mask.Mask((50,50),True)
velx=0
vely=0
lorr=True
def loadlevel():
  try:
    global levelpic,groundmask,lavamask,jumpymask,fastleftmask,fastrightmask,watermask,shrinkmask,normalmask,winmask
    levelpic=pygame.image.load(f"C:/Users/Rainbow/Documents/GitHub/scrolling-platformer/levels/{level}.png")
    groundmask=pygame.mask.from_threshold(levelpic,(0,0,0),(1,1,1))
    lavamask=pygame.mask.from_threshold(levelpic,(255,0,0),(1,1,1))
    jumpymask=pygame.mask.from_threshold(levelpic,(255,255,100),(1,1,1))
    fastleftmask=pygame.mask.from_threshold(levelpic,(0,255,0),(1,1,1))
    fastrightmask=pygame.mask.from_threshold(levelpic,(255,0,255),(1,1,1))
    watermask=pygame.mask.from_threshold(levelpic,(0,255,255),(1,1,1))
    shrinkmask=pygame.mask.from_threshold(levelpic,(0,100,0),(1,1,1))
    normalmask=pygame.mask.from_threshold(levelpic,(0,0,100),(1,1,1))
    winmask=pygame.mask.from_threshold(levelpic,(255,255,0),(1,1,1))
  except:
    pygame.quit()
    input("YOU WIN")
    sys.exit()
def reset():
  global screenposx,screenposy,velx,vely
  screenposx=-300
  screenposy=3100
  velx=0
  vely=0
while True:
  loadlevel()
  reset()
  while True:
    tbottom=bool(groundmask.overlap_area(bottom,(screenposx+300,screenposy+300)))
    tside=bool(groundmask.overlap_area(side,(screenposx+299,screenposy+300)))
    ttop=bool(groundmask.overlap_area(top,(screenposx+300,screenposy+299)))
    win=bool(winmask.overlap_area(playermask,(screenposx+300,screenposy+300)))
    lava=bool(lavamask.overlap_area(playermask,(screenposx+300,screenposy+300)))
    screen.fill((255,255,255))
    for event in pygame.event.get():
      if event.type==pygame.QUIT:
        pygame.quit()
        sys.exit()
    if screenposx<-300:
      screenposx=-300
      velx=0
    if screenposx>3150:
      screenposx=3150
      velx=0
    screen.blit(levelpic,(-screenposx,-round(screenposy)))
    keys=pygame.key.get_pressed()
    if velx>=2:
      velx-=2
    elif velx<=-2:
      velx+=2
    else:
      velx=0
    if not tbottom:
      vely-=2
    else:
      vely=0
    if keys[pygame.K_UP] and tbottom:
      vely+=30
    if keys[pygame.K_LEFT]:
      velx-=3
      lorr=False
    if keys[pygame.K_RIGHT]:
      velx+=3
      lorr=True
    screenposx+=velx
    screenposy-=vely
    if lorr:
      screen.blit(playerr,(300,300))
    else:
      screen.blit(playerl,(300,300))
    if win:
      break
    if lava:
      reset()
    pygame.display.flip()
    time.sleep(0.02)
  level+=1
