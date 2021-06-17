import pygame

class Wall(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos, invert):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('./assets/ground/Tile__01.png')
        self.image = pygame.transform.scale(self.image, [20, 128])

        self.rect = pygame.Rect([xpos, ypos, 20, 128])

        self.inverted = invert

        if self.inverted:
            self.image = pygame.transform.flip(self.image, True, False)

    def update(self, speed):
        self.rect[0] -= speed