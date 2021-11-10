import pygame
pygame.init()
screen = pygame.display.set_mode([500, 500])

class GameObject(pygame.sprite.Sprite):
  def __init__(self, x, y, image):
    super(GameObject, self).__init__()
    self.surf = pygame.image.load(image)
    self.x = x
    self.y = y
  
  def render(self, screen):
    screen.blit(self.surf, (self.x, self.y))
    
apple = GameObject(100, 100, 'apple.png')
apple = GameObject(100, 250, 'strawberry.png')
apple = GameObject(100, 400, 'apple.png')
apple = GameObject(250, 100, 'strawberry.png')
apple = GameObject(250, 250, 'apple.png')
apple = GameObject(250, 400, 'strawberry.png')
apple = GameObject(400, 100, 'apple.png')
apple = GameObject(400, 250, 'strawberry.png')
apple = GameObject(400, 400, 'apple.png')

running = True
while running:
  # Looks at events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  screen.fill((255, 255, 255))
  apple.render(screen)
  pygame.display.flip()
  
