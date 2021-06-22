import pygame

class DirtBlock(pygame.sprite.Sprite):

    def __init__(self, group, xpos, ypos,curve=False, inverted=False):



        if curve:
            self.image = pygame.image.load('./assets/ground/dirt_block__01.png')
        else:
            self.image = pygame.image.load('./assets/ground/dirt_block__02.png').convert_alpha()

        self.image = pygame.transform.scale(self.image, [128,128])

        if inverted:
            self.image = pygame.transform.flip(self.image, True, False)

        self.rect = pygame.Rect(xpos, ypos, 128, 128)
        
        pygame.sprite.Sprite.__init__(self, group)



    def update(self, speed):
        self.rect[0] -= speed