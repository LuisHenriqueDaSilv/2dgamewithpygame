import pygame

class Void(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('./assets/ground/Ground__01.png')
        self.image = pygame.transform.scale(self.image, [1152,1])

        self.rect = pygame.Rect(0,670,1152,1) 

    def update(self):
        return
