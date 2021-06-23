import pygame

class DirtBlock(pygame.sprite.Sprite):

    def __init__(self, group, xpos, ypos,curve=False, inverted=False, repeat_y=1, repeat_x=1):


        self.image = pygame.Surface((128*repeat_x, 128*repeat_y))

        if curve:
            self.dirt = pygame.image.load('./assets/ground/DirtBlock_1.png').convert_alpha()
        else:
            self.dirt = pygame.image.load('./assets/ground/DirtBlock_2.png').convert_alpha()

        self.dirt = pygame.transform.scale(self.dirt, [128,128])

        if inverted:
            self.dirt = pygame.transform.flip(self.dirt, True, False)


        self.rect = pygame.Rect(xpos, ypos-(128*repeat_y), 128*repeat_x, 128*repeat_y)

        for i_y in range(0,repeat_y):
            for i_x in range(0, repeat_x):
                self.image.blit(self.dirt, [i_x*128,i_y*128])


        
        pygame.sprite.Sprite.__init__(self, group)



    def update(self, speed):
        self.rect[0] -= speed