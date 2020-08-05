import pygame,sys,time
pygame.init()
screen=pygame.display.set_mode([700,700])
pygame.display.set_caption("Scrolling platformer")
level=1
player=pygame.image.load("C:/Users/Rainbow/Documents/GitHub/scrolling-platformer/player.png")
player.set_colorkey((255,255,255))
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
areamask=None
playermask=pygame.mask.Mask((50,50),True)
screenposx=-300
screenposy=3100
velx=0
vely=0
def loadlevel():
  global levelpic,groundmask,lavamask,jumpymask,fastleftmask,fastrightmask,watermask,shrinkmask,normalmask,winmask,areamask
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
  areamask=pygame.mask.from_threshold(levelpic,(255,100,255),(1,1,1))
while True:
  loadlevel()
  while True:
    ground=bool(groundmask.overlap_area(playermask,(screenposx+300,screenposy+301)))
    screen.fill((255,255,255))
    for event in pygame.event.get():
      if event.type==pygame.QUIT:
        pygame.quit()
        sys.exit()
    screen.blit(levelpic,(-screenposx,-screenposy))
    keys=pygame.key.get_pressed()
    if velx>=2:
      velx-=2
    elif velx<=-2:
      velx+=2
    else:
      velx=0
    if not ground:
      vely-=2
    else:
      vely=0
    if keys[pygame.K_UP] and ground:
      vely+=30
    if keys[pygame.K_LEFT]:
      velx-=3
    if keys[pygame.K_RIGHT]:
      velx+=3
    if screenposx<-300:
      screenposx=-300
      velx=0
    if screenposx>3150:
      screenposx=3150
      velx=0
    screenposx+=velx
    screenposy-=vely
    screen.blit(player,(300,300))
    pygame.display.flip()
    time.sleep(0.02)
