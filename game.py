import pygame
from random import randint

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode([500, 500])

class GameObject(pygame.sprite.Sprite):
  def __init__(self, x, y, image):
    super(GameObject, self).__init__()
    self.surf = pygame.image.load(image)
    self.x = x
    self.y = y
  
  def render(self, screen):
    screen.blit(self.surf, (self.x, self.y))

class Apple(GameObject):
  def __init__(self):
    super(Apple, self).__init__(0, 0, 'apple.png')
    self.dx = 0
    self.dy = (randint(0, 200) / 100) + 1
    self.reset()

  def move(self):
    self.x += self.dx
    self.y += self.dy
    if self.y > 500: 
      self.reset()

  def reset(self):
    self.x = randint(50, 400)
    self.y = -64

class Strawberry(GameObject):
  def __init__(self):
    super(Strawberry, self).__init__(0, 0, 'strawberry.png')
    self.dx = (randint(0, 200) / 100) + 1
    self.dy = 0
    self.reset()

  def move(self):
    self.x += self.dx
    self.y += self.dy
    if self.x > 500: 
      self.reset()

  def reset(self):
    self.x = -64
    self.y = randint(50, 400)

class Player(GameObject):
  def __init__(self):
    super(Player, self).__init__(0, 0, 'player.png')
    # player is 32 x 32
    self.dx = 250 - 32
    self.dy = 250 - 32
    self.reset()

  def left(self):
    if self.dx >= 32:
      self.dx -= 32
    else:
      pass

  def right(self):
    if self.dx <= 408:
      self.dx += 32
    else:
      pass

  def up(self):
    if self.dy >= 32:
      self.dy -= 32
    else:
      pass

  def down(self):
    if self.dy <= 408:
      self.dy += 32
    else:
      pass

  def move(self):
    self.x -= (self.x - self.dx) * 0.25
    self.y -= (self.y - self.dy) * 0.25
    # if self.x < 32 or self.x > 532s:
    #   self.reset()
    # if self.y < 32 or self.y > 532:
    #   self.reset()

  def reset(self):
    self.x = 250 - 32
    self.y = 250 - 32

apple1 = Apple()
apple2 = Apple()
apple3 = Apple()

strawberry1 = Strawberry()
strawberry2 = Strawberry()
strawberry3 = Strawberry()

player = Player()

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        running = False
      elif event.key == pygame.K_LEFT:
        player.left()
      elif event.key == pygame.K_RIGHT:
        player.right()
      elif event.key == pygame.K_UP:
        player.up()
      elif event.key == pygame.K_DOWN:
        player.down()
  screen.fill((255, 255, 255))

  player.move()
  apple1.move()
  apple2.move()
  apple1.move()
  strawberry1.move()
  strawberry2.move()
  strawberry3.move()

  player.render(screen)
  apple1.render(screen)
  apple2.render(screen)
  apple3.render(screen)
  strawberry1.render(screen)
  strawberry2.render(screen)
  strawberry3.render(screen)

  pygame.display.flip()
  clock.tick(60)