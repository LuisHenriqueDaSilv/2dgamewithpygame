import pygame

class Ground(pygame.sprite.Sprite):
    
    def __init__(self, group, xpos, ypos, repeat_x=1):



        self.ground = pygame.image.load('./assets/ground/Ground_1.png').convert_alpha()
        self.ground = pygame.transform.scale(self.ground, [128, 128])

        self.image = pygame.Surface((128*repeat_x, 128))
        self.rect = pygame.Rect(
            xpos,
            ypos-128,
            128*repeat_x,
            128
        ) 

        for i in range(0, repeat_x):
            self.image.blit(self.ground,  (128*i, 0))



        pygame.sprite.Sprite.__init__(self, group)

    def update(self, speed):
        self.rect[0] -= speed