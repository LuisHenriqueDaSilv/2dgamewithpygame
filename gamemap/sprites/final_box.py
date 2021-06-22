import pygame

class FinalBox(pygame.sprite.Sprite):
    def __init__(self, group, xpos, ypos):
        
        self.image = pygame.image.load('./assets/visuals/Crate.png')
        self.rect = pygame.Rect(xpos, ypos, 106, 106)
        pygame.sprite.Sprite.__init__(self, group)

    def update(self, speed):
        self.rect[0] -= speed