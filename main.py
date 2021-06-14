import pygame

pygame.init()

SCREEN_HEIGTH = 1100
SCREEN_WIDTH= 650

screen = pygame.display.set_mode((SCREEN_HEIGTH, SCREEN_WIDTH))
pygame.display.set_caption('Ninja Saving The World (Game)')

BACKGROUND = pygame.image.load('./assets/background.png').convert_alpha()
BACKGROUND = pygame.transform.scale(BACKGROUND, (SCREEN_HEIGTH, SCREEN_WIDTH))

clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        self.status = 'Idle' #'Idle'/'Run'

        self.idle_images = [
            pygame.image.load('./assets/player/idle/Idle__000.png').convert_alpha(),
            pygame.image.load('./assets/player/idle/Idle__001.png').convert_alpha(),
            pygame.image.load('./assets/player/idle/Idle__002.png').convert_alpha(),
            pygame.image.load('./assets/player/idle/Idle__003.png').convert_alpha(),
            pygame.image.load('./assets/player/idle/Idle__004.png').convert_alpha(),
            pygame.image.load('./assets/player/idle/Idle__005.png').convert_alpha(),
            pygame.image.load('./assets/player/idle/Idle__006.png').convert_alpha(),
            pygame.image.load('./assets/player/idle/Idle__007.png').convert_alpha(),
            pygame.image.load('./assets/player/idle/Idle__008.png').convert_alpha(),
            pygame.image.load('./assets/player/idle/Idle__009.png').convert_alpha()
        ]

        self.run_images = [
            pygame.image.load('./assets/player/run/Run__000.png').convert_alpha(),
            pygame.image.load('./assets/player/run/Run__001.png').convert_alpha(),
            pygame.image.load('./assets/player/run/Run__002.png').convert_alpha(),
            pygame.image.load('./assets/player/run/Run__003.png').convert_alpha(),
            pygame.image.load('./assets/player/run/Run__004.png').convert_alpha(),
            pygame.image.load('./assets/player/run/Run__005.png').convert_alpha(),
            pygame.image.load('./assets/player/run/Run__006.png').convert_alpha(),
            pygame.image.load('./assets/player/run/Run__007.png').convert_alpha(),
            pygame.image.load('./assets/player/run/Run__008.png').convert_alpha(),
            pygame.image.load('./assets/player/run/Run__009.png').convert_alpha()
        ]

        self.image = self.idle_images[0]
        self.rect = pygame.Rect(300, 300, 100, 100)
        self.current_image = 0
        self.xSpeed = 0
        self.ySpeed = 0
        

    def update(self):

        key = pygame.key.get_pressed()

        if key[pygame.K_d]:
            
            if self.xSpeed < 10:
                self.xSpeed += 1

        elif key[pygame.K_a]:
            
            if self.xSpeed > -10:
                self.xSpeed -= 1

        else:

            if self.xSpeed > 0:
                self.xSpeed -= 1
            elif self.xSpeed < 0:
                self.xSpeed += 1


        if self.xSpeed > 0 and self.ySpeed == 0:

            self.current_image = (self.current_image + 1) % 10
            self.image = self.run_images[self.current_image]
            self.image = pygame.transform.scale(self.image, [50, 70])

        elif self.xSpeed < 0 and self.ySpeed == 0:

            self.current_image = (self.current_image + 1) % 10
            self.image = self.run_images[self.current_image]

            self.image = pygame.transform.scale(self.image, [50, 70])
            self.image = pygame.transform.flip(self.image, True, False)

        else: 

            self.current_image = (self.current_image + 1) % 10
            self.image = self.idle_images[self.current_image]
            self.image = pygame.transform.scale(self.image, [35, 70])


playerGroup = pygame.sprite.Group()
player = Player()

def draw():
    playerGroup.draw(screen)

def update():
    playerGroup.update()

playerGroup.add(player)

while True:

    clock.tick(30)

    screen.blit(BACKGROUND, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break

    update()
    draw()

    pygame.display.flip()

