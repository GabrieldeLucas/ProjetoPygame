import pygame
from pygame.locals import *
from sys import exit
import random
import time


contador = 0
coin_width = 500
coin_heigth = 350
width = 1000
heigth = 700
SPEED = 10
GROUND_WIDTH = 2 * width
GROUND_HEIGTH = 50
GAME_SPEED = 10









class Moeda(pygame.sprite.Sprite):
    def __init__(self, xpos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("sprites/coin.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(30, 30))
        self.rect = self.image.get_rect()
        self.rect[0] = xpos
        self.rect[1] = heigth - coin_heigth

    def update(self, *args):
        self.rect[0] -= GAME_SPEED * 3




def foradatela(sprite):
    return sprite.rect[0] < -(sprite.rect[2])

class inimigo_terrestre(pygame.sprite.Sprite):
    def __init__(self,  xpos):
      pygame.sprite.Sprite.__init__(self)


      self.image_inimigo1 = pygame.image.load("sprites/inimigo_terrestre1.png")
      self.image_inimigo1 = pygame.transform.scale(self.image_inimigo1,(100,100))
      self.image_run_inimigo1 = [pygame.image.load("sprites/inimigo_terrestre1.png").convert_alpha(),
                                 pygame.image.load("sprites/inimigo_terrestre1.png").convert_alpha(),
                                 pygame.image.load("sprites/inimigo_terrestre2.png").convert_alpha(),
                                 pygame.image.load("sprites/inimigo_terrestre2.png").convert_alpha(),
                                 pygame.image.load("sprites/inimigo_terrestre3.png").convert_alpha(),
                                 pygame.image.load("sprites/inimigo_terrestre3.png").convert_alpha(),
                                 pygame.image.load("sprites/inimigo_terrestre4.png").convert_alpha(),
                                 pygame.image.load("sprites/inimigo_terrestre4.png").convert_alpha(),
                                 pygame.image.load("sprites/inimigo_terrestre5.png").convert_alpha(),
                                 pygame.image.load("sprites/inimigo_terrestre5.png").convert_alpha(),
                                 pygame.image.load("sprites/inimigo_terrestre4.png").convert_alpha(),
                                 pygame.image.load("sprites/inimigo_terrestre4.png").convert_alpha(),
                                 pygame.image.load("sprites/inimigo_terrestre6.png").convert_alpha(),
                                 pygame.image.load("sprites/inimigo_terrestre6.png").convert_alpha(),
                                 pygame.image.load("sprites/inimigo_terrestre7.png").convert_alpha(),
                                 pygame.image.load("sprites/inimigo_terrestre7.png").convert_alpha(),
                                 pygame.image.load("sprites/inimigo_terrestre8.png").convert_alpha(),
                                 pygame.image.load("sprites/inimigo_terrestre9.png").convert_alpha(),
                                 pygame.image.load("sprites/inimigo_terrestre9.png").convert_alpha(),
                                 pygame.image.load("sprites/inimigo_terrestre10.png").convert_alpha(),
                                 pygame.image.load("sprites/inimigo_terrestre10.png").convert_alpha()
                                 ]

      self.image = pygame.image.load("sprites/inimigo_terrestre1.png")
      self.rect = pygame.Rect(900, 580, 100, 100)
      self.current_image = 0
      self.rect[0] = xpos + 950
      self.rect[1] = 580
    def update(self, *args):

       self.current_image = (self.current_image + 1) % 20
       self.image = self.image_run_inimigo1[self.current_image]
       self.image = pygame.transform.scale(self.image, (100, 100))
       self.rect[0] -= GAME_SPEED * 2

def inimigo_fora_tela(sprite):
    return sprite.rect[0] < 0

class slime_ball(pygame.sprite.Sprite):
 def __init__(self, xpos):
  pygame.sprite.Sprite.__init__(self)

  self.image = pygame.image.load("sprites/slime_ball.png")
  self.image = pygame.transform.scale(self.image, (10, 10))
  self.rect = pygame.Rect(10, 560, 10, 10)
  self.rect[0] = xpos + 950
  self.rect[1] = 560

 def update(self, *args):
  self.image = pygame.transform.scale(self.image, (30, 30))
  self.rect[0] -= GAME_SPEED * 2
def slime_fugiu(sprite):
    return sprite.rect[0] < -(sprite.rect[2])















class Player(pygame.sprite.Sprite):
    def __init__(self):
      pygame.sprite.Sprite.__init__(self)
      self.image_fall = pygame.image.load("sprites/Fall.png").convert_alpha()
      self.image_fall = pygame.transform.scale(self.image_fall, (100, 100))
      self.image_run = [pygame.image.load("sprites/Run__000.png").convert_alpha(),
                        pygame.image.load("sprites/Run__001.png").convert_alpha(),
                        pygame.image.load("sprites/Run__002.png").convert_alpha(),
                        pygame.image.load("sprites/Run__003.png").convert_alpha(),
                        pygame.image.load("sprites/Run__004.png").convert_alpha(),
                        pygame.image.load("sprites/Run__005.png").convert_alpha(),
                        pygame.image.load("sprites/Run__006.png").convert_alpha(),
                        pygame.image.load("sprites/Run__007.png").convert_alpha(),
                        pygame.image.load("sprites/Run__008.png").convert_alpha(),
                        pygame.image.load("sprites/Run__009.png").convert_alpha()
                        ]
      self.image = pygame.image.load("sprites/Run__000.png")
      self.rect = pygame.Rect(100,100,100,100)
      self.current_image = 0
    def update(self, *args):
      def move_player(self):
       key = pygame.key.get_pressed()
       if key[pygame.K_d] and self.rect[0]<905:
           self.rect[0] += GAME_SPEED
       elif key[pygame.K_a] and self.rect[0]>0:
           self.rect[0] -=GAME_SPEED
       if key[pygame.K_RIGHT] and self.rect[0]<905:
           self.rect[0] += GAME_SPEED
       elif key[pygame.K_LEFT]  and self.rect[0]>0:
           self.rect[0] -= GAME_SPEED
       self.current_image = (self.current_image + 1) % 10
       self.image = self.image_run[self.current_image]
       self.image = pygame.transform.scale(self.image,(100,100))
      move_player(self)
      self.rect[1] += SPEED

      def fly(self):
          key = pygame.key.get_pressed()
          if key[pygame.K_w] or key[pygame.K_UP] or key[pygame.K_SPACE]:
              self.image = pygame.image.load('sprites/Fly.png').convert_alpha()
              self.image = pygame.transform.scale(self.image, (100, 100))
              if self.rect[1]>0:
               self.rect[1] -= 30

      fly(self)

      def fall(self):
          key = pygame.key.get_pressed()
          if not pygame.sprite.groupcollide(playerGroup,groundGroup,False,False) and not key[pygame.K_w] and not key[pygame.K_UP] and not key[pygame.K_SPACE]:
              self.image = self.image_fall
      fall(self)

class Ground(pygame.sprite.Sprite):
    def __init__(self, xpos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("sprites/ground2.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(GROUND_WIDTH, GROUND_HEIGTH))
        self.rect = self.image.get_rect()
        self.rect[0] =xpos
        self.rect[1] = heigth - GROUND_HEIGTH

    def update(self, *args):
        self.rect[0] -= GAME_SPEED


def is_off_screen(sprite):
    return sprite.rect[0] < -(sprite.rect[2])


pygame.init()
#pygame.mixer.init()

#musica = pygame.mixer.music.load("musica.mp3")
#pygame.mixer.music.play(-1)

game_window = pygame.display.set_mode((width,heigth))
pygame.display.set_caption("joguinho legal dms")

groundGroup = pygame.sprite.Group()
for i in range(3):

 ground = Ground(width * i)
 groundGroup.add(ground)


BACKGROUND = pygame.image.load("sprites/background3.gif")
BACKGROUND = pygame.transform.scale(BACKGROUND,(width,heigth))


playerGroup = pygame.sprite.Group()
player = Player()
playerGroup.add(player)



inimigo_terrestreGroup = pygame.sprite.Group()
for i in range(1):
 inimigo1 = inimigo_terrestre(width * i)
 inimigo_terrestreGroup.add(inimigo1)


slime_ballGroup = pygame.sprite.Group()
for i in range(1):
  slime_ball
  tiro_slime = slime_ball(width * i)
  slime_ballGroup.add(tiro_slime)


coinGroup = pygame.sprite.Group()
for i in range(4):
 coin = Moeda(width * i)
 coinGroup.add(coin)






gameloop = True

def draw():
 coinGroup.draw(game_window)
 playerGroup.draw(game_window)
 groundGroup.draw(game_window)
 inimigo_terrestreGroup.draw(game_window)
 slime_ballGroup.draw(game_window)


def update():
 coinGroup.update()
 playerGroup.update()
 groundGroup.update()
 inimigo_terrestreGroup.update()
 slime_ballGroup.update()

clock = pygame.time.Clock()

while gameloop == True:
 clock.tick(10)
 game_window.blit(BACKGROUND,(0,0))
 for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

 if slime_fugiu(slime_ballGroup.sprites()[0]):
     slime_ballGroup.remove(slime_ballGroup.sprites()[0])
     nova_ball_slime = slime_ball(width - 20  )
     slime_ballGroup.add(nova_ball_slime)



 if is_off_screen(groundGroup.sprites()[0]):
     groundGroup.remove(groundGroup.sprites()[0])
     newGround = Ground(width - 20)
     groundGroup.add(newGround)
 if pygame.sprite.groupcollide(playerGroup,groundGroup,False,False):
     SPEED = 0
 else:
    SPEED = 10

 if inimigo_fora_tela(inimigo_terrestreGroup.sprites()[0]):
     inimigo_terrestreGroup.remove(inimigo_terrestreGroup.sprites()[0])
     newinimigoterrestre = inimigo_terrestre(width - 100 )
     inimigo_terrestreGroup.add(newinimigoterrestre)

 elif pygame.sprite.groupcollide(playerGroup, inimigo_terrestreGroup, False, False):
  #playerGroup.remove(playerGroup.sprites()[0])

  SPEED = 0
  GAME_SPEED = 0


 if foradatela(coinGroup.sprites()[0]):
     clock.tick(5)
     coin_width = random.randint(0, width - 50)
     coin_heigth = random.randint(0, heigth)
     coinGroup.remove(coinGroup.sprites()[0])
     newMoeda = Moeda(width * i)
     coinGroup.add(newMoeda)

 elif pygame.sprite.groupcollide(playerGroup, coinGroup, False, False):
     clock.tick(5)
     coin_width = random.randint(0, width - 50)
     coin_heigth = random.randint(0, heigth)
     coinGroup.remove(coinGroup.sprites()[0])
     newMoeda = Moeda(width * i)
     coinGroup.add(newMoeda)
     contador += 1

 update()
 draw()

 pygame.display.update()
