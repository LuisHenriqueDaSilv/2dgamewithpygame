import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, gamedata):

        self.gamedata = gamedata

        pygame.sprite.Sprite.__init__(self)

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
        self.rect = pygame.Rect(
            self.gamedata['screen_width'] / 2,
            self.gamedata['screen_height']-128-70, #screen height - ground height - Player height
            100,
            100
        )

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

            if self.xSpeed != 0 :
                self.xSpeed = 0


        self.current_image = (self.current_image + 1) % 10


        if self.ySpeed == 0:

            
            if self.xSpeed == 0:
                self.image = self.idle_images[self.current_image]
                self.image = pygame.transform.scale(self.image, [35, 70])
                return 

            self.image = self.run_images[self.current_image]
            self.image = pygame.transform.scale(self.image, [50, 70])

            if self.xSpeed > 0:

                if self.rect[0] < self.gamedata['screen_width'] / 2:
                    self.rect[0] += self.xSpeed

            elif self.xSpeed < 0:

                self.image = pygame.transform.flip(self.image, True, False)

                if self.rect[0] < 1:
                    self.xSpeed = 0
                else:
                    self.rect[0] += self.xSpeed
