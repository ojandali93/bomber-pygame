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

apple1 = Apple()
apple2 = Apple()
apple3 = Apple()

strawberry1 = Strawberry()
strawberry2 = Strawberry()
strawberry3 = Strawberry()

running = True
while running:
  # Looks at events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  screen.fill((255, 255, 255))

  apple1.move()
  apple2.move()
  apple1.move()
  strawberry1.move()
  strawberry2.move()
  strawberry3.move()

  apple1.render(screen)
  apple2.render(screen)
  apple3.render(screen)
  strawberry1.render(screen)
  strawberry2.render(screen)
  strawberry3.render(screen)

  pygame.display.flip()
  clock.tick(60)