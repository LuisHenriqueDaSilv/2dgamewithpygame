import pygame

class Wall(pygame.sprite.Sprite):
    def __init__(self,group, xpos, ypos, ground=False, inverted=False, repeat_y=1):

        self.ground = ground

        if self.ground: 
            self.wall = pygame.image.load('./assets/ground/Wall_2.png').convert_alpha()
        else:
            self.wall = pygame.image.load('./assets/ground/Wall_1.png').convert_alpha()

        if inverted:
            self.wall = pygame.transform.flip(self.wall, True, False)
            
        self.wall = pygame.transform.scale(self.wall, [128, 128])

        self.image = pygame.image.load('./assets/Invisible.png')
        self.image = pygame.transform.scale(self.image, [128, repeat_y*128])

        self.rect = pygame.Rect(xpos, ypos-(repeat_y*128), 128, 128*repeat_y)

        for i in range(repeat_y):
            self.image.blit(self.wall, [0, i*128])

        self.image.convert_alpha()

        pygame.sprite.Sprite.__init__(self, group)

    def update(self, speed):
        self.rect[0] -= speed