import pygame

class Ground(pygame.sprite.Sprite):
    
    def __init__(self, group, xpos, ypos):


        self.image = pygame.image.load('./assets/ground/Ground__01.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, [128, 128])

        self.rect = pygame.Rect(
            xpos,
            ypos,
            128,
            128
        ) 

        pygame.sprite.Sprite.__init__(self, group)

    def update(self, speed):
        self.rect[0] -= speed