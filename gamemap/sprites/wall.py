import pygame

class Wall(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos, ground=False, inverted=False):

        pygame.sprite.Sprite.__init__(self)

        self.ground = ground

        if self.ground: 
            self.image = pygame.image.load('./assets/ground/wall__02.png')
        else:
            self.image = pygame.image.load('./assets/ground/wall__01.png').convert_alpha()

        if inverted:
            self.image = pygame.transform.flip(self.image, True, False)
            
        self.image = pygame.transform.scale(self.image, [128, 128])

        self.rect = pygame.Rect(xpos, ypos, 128, 128)

    def update(self, speed):
        self.rect[0] -= speed