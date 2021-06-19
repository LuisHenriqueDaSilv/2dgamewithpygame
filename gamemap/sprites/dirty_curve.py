import pygame

class DirtyCurve(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('./assets/ground/dirty_block__01.png').convert_alpha()

        self.image = pygame.transform.scale(self.image, [128,128])

        self.rect = pygame.Rect(xpos, ypos, 128, 128)


    def update(self, speed):
        self.rect[0] -= speed