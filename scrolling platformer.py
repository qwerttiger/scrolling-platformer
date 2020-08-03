import pygame,random
pygame.init()
pygame.display.set_mode([700,700])
pygame.display.set_caption("Scrolling platformer")
level=1
player=pygame.image.load("C:/Users/Rainbow/Documents/GitHub/scrolling-platformer/player.png")
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
