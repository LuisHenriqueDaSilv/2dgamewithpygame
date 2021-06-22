import pygame

class Boss(pygame.sprite.Sprite):

    def __init__(self, xpos, ypos):

        pygame.sprite.Sprite.__init__(self)

        self.images = [
            pygame.image.load('./assets/boss/Fly__01.png').convert_alpha(),
            pygame.image.load('./assets/boss/Fly__02.png').convert_alpha(),
            pygame.image.load('./assets/boss/Fly__03.png').convert_alpha(),
            pygame.image.load('./assets/boss/Fly__04.png').convert_alpha(),
            pygame.image.load('./assets/boss/Fly__05.png').convert_alpha(),
            pygame.image.load('./assets/boss/Fly__06.png').convert_alpha(),
            pygame.image.load('./assets/boss/Fly__07.png').convert_alpha(),
            pygame.image.load('./assets/boss/Fly__08.png').convert_alpha(),
            pygame.image.load('./assets/boss/Fly__09.png').convert_alpha(),

        ]

        self.image = self.images[0]
        self.image = pygame.transform.scale(self.image, [70,100])
        self.image = pygame.transform.flip(self.image, True, False)

        self.rect = pygame.Rect(xpos, ypos, 70, 100)

        self.current_image = 0


    def update(self, speed, opponent):

        self.current_image = (self.current_image + 1) % 9

        self.rect[0] -= speed


        on_screen = self.rect[0] >0 and self.rect[0] < 1152-70

        if on_screen:
            if self.rect[1] > 0-70:
                self.rect[1] -= 5
        else:
            pass

        self.image = self.images[self.current_image]
        self.image = pygame.transform.scale(self.image, [70, 100])
        self.image = pygame.transform.flip(self.image, True, False)