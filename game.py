import pygame
from random import randint, choice

lanes = [93, 218, 343]

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
    self.x = choice(lanes)
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
    self.y = choice(lanes)

class Player(GameObject):
  def __init__(self):
    super(Player, self).__init__(0, 0, 'player.png')
    # player is 32 x 32
    self.dx = 0
    self.dy = 0
    self.pos_x = 1
    self.pos_y = 1
    self.reset()

  def update_dx_dy(self):
    self.dx = lanes[self.pos_x]
    self.dy = lanes[self.pos_y]

  def left(self):
    if self.pos_x > 0:
      self.pos_x -= 1
      self.update_dx_dy()

  def right(self):
    if self.pos_x < len(lanes) - 1:
      self.pos_x += 1
      self.update_dx_dy()

  def up(self):
    if self.pos_y > 0:
      self.pos_y -= 1
      self.update_dx_dy()

  def down(self):
    if self.pos_y < len(lanes) - 1:
      self.pos_y += 1
      self.update_dx_dy()

  def move(self):
    self.x -= (self.x - self.dx) * 0.25
    self.y -= (self.y - self.dy) * 0.25

  def reset(self):
    self.x = lanes[self.pos_x]
    self.y = lanes[self.pos_y]
    self.dx = self.x
    self.dy = self.y

player = Player()
apple1 = Apple()
apple2 = Apple()
strawberry1 = Strawberry()
strawberry2 = Strawberry()

all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(apple1)
# all_sprites.add(apple2)
all_sprites.add(strawberry1)
# all_sprites.add(strawberry2)

# apple = Apple()
# apple2 = Apple()
# apple3 = Apple()

# strawberry = Strawberry()
# strawberry2 = Strawberry()
# strawberry3 = Strawberry()

# player = Player()

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
  for entity in all_sprites:
    entity.move()
    entity.render(screen)

  # player.move()
  # apple1.move()
  # apple2.move()
  # apple1.move()
  # strawberry1.move()
  # strawberry2.move()
  # strawberry3.move()

  # player.render(screen)
  # apple1.render(screen)
  # apple2.render(screen)
  # apple3.render(screen)
  # strawberry1.render(screen)
  # strawberry2.render(screen)
  # strawberry3.render(screen)

  pygame.display.flip()
  clock.tick(60)