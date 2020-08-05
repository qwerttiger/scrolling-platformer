import pygame,sys
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
screenposx=-300
screenposy=3100
velx=0
vely=0
def loadlevel():
  global levelpic,groundmask,lavamask,jumpymask,fastleftmask,fastrightmask,watermask,shrinkmask,normalmask,winmask,areamask
  levelpic=pygame.image.load(f"C:/Users/Rainbow/Documents/GitHub/scrolling-platformer/levels/{level}.png")
  groundmask=pygame.mask.from_threshold(levelpic,(0,0,0))
  lavamask=pygame.mask.from_threshold(levelpic,(255,0,0))
  jumpymask=pygame.mask.from_threshold(levelpic,(255,255,100))
  fastleftmask=pygame.mask.from_threshold(levelpic,(0,255,0))
  fastrightmask=pygame.mask.from_threshold(levelpic,(255,0,255))
  watermask=pygame.mask.from_threshold(levelpic,(0,255,255))
  shrinkmask=pygame.mask.from_threshold(levelpic,(0,100,0))
  normalmask=pygame.mask.from_threshold(levelpic,(0,0,100))
  winmask=pygame.mask.from_threshold(levelpic,(255,255,0))
  areamask=pygame.mask.from_threshold(levelpic,(255,100,255))
while True:
  loadlevel()
  while True:
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
    if keys[pygame.K_UP]:
      vely+=0.1
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
    print(velx)
    screenposx+=velx
    screenposy-=vely
    screen.blit(player,(300,300))
    pygame.display.flip()
