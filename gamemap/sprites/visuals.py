import random
import pygame

class TextLine(pygame.sprite.Sprite):
    def __init__(self,group, xpos, ypos, text, color=(89, 16, 0)):

        pygame.sprite.Sprite.__init__(self)
    
        self.font = pygame.font.SysFont("./assets/fonts/FFF_Tusj.ttf", 25)
        self.textSurf = self.font.render(text, True, color)
        self.image = pygame.image.load('./assets/Invisible.png').convert_alpha()

        self.image = pygame.transform.scale(self.image, [len(text)*25,100])

        self.rect = pygame.Rect(xpos, ypos, 100, 100)

        self.image.blit(self.textSurf, [0,0])

        pygame.sprite.Sprite.__init__(self, group)

    def update(self, speed):
        self.rect[0] -= speed


class Tree(pygame.sprite.Sprite):

    def __init__(self, group, xpos, ypos):


        self.image = pygame.image.load('./assets/visuals/Tree.png').convert_alpha()
        self.rect = pygame.Rect(xpos, ypos, 286, 239)

        pygame.sprite.Sprite.__init__(self, group)

    def update(self, speed):

        self.rect[0] -= speed

class Sign(pygame.sprite.Sprite):

    def __init__(self, group, xpos, ypos,text_pos, text="Sign"):


        self.image = pygame.image.load('./assets/visuals/Sign.png').convert_alpha()
        self.rect = pygame.Rect(xpos, ypos, 91, 93)


        self.font = pygame.font.SysFont("./assets/fonts/FFF_Tusj.ttf", 20)
        self.textSurf = self.font.render(text, True, (255,255,255))
        self.textSurf = pygame.transform.rotate(self.textSurf, 5)

        self.image.blit(self.textSurf, text_pos)

        pygame.sprite.Sprite.__init__(self, group)


    def update(self, speed):


        self.rect[0] -= speed

class Bush(pygame.sprite.Sprite):
    
    def __init__(self, group, xpos, ypos):

        image_index = random.randint(1, 3)

        self.image = pygame.image.load(f'./assets/visuals/Bush_{image_index}.png').convert_alpha()

        self.image = pygame.transform.scale(self.image, [100,64])

        self.rect = pygame.Rect(xpos, ypos, 100, 64)

        pygame.sprite.Sprite.__init__(self, group)

    def update(self, speed):

        self.rect[0] -= speed

class ArrowSign(pygame.sprite.Sprite):
    def __init__(self, group, xpos, ypos, inverted=False):

        self.image = pygame.image.load('./assets/visuals/Arrow.png')

        self.rect = pygame.Rect(xpos, ypos, 86, 87)

        if inverted:
            self.image = pygame.transform.flip(self.image, True, False)

        pygame.sprite.Sprite.__init__(self, group)


    def update(self, speed):
        self.rect[0] -= speed

class TombStone(pygame.sprite.Sprite):
    
    def __init__(self, group, xpos, ypos):

        image_index = random.randint(1, 2)

        self.image = pygame.image.load(f'./assets/visuals/TombStone_{image_index}.png').convert_alpha()

        self.image = pygame.transform.scale(self.image, [53, 76])

        self.rect = pygame.Rect(xpos, ypos, 0, 0)

        pygame.sprite.Sprite.__init__(self, group)

    def update(self, speed):

        self.rect[0] -= speed

class Skeleton(pygame.sprite.Sprite):
    def __init__(self, group, xpos, ypos, inverted=False):

        self.image = pygame.image.load('./assets/visuals/Skeleton.png')
        self.image = pygame.transform.scale(self.image, [50, 25])

        self.rect = pygame.Rect(xpos, ypos, 0,0)

        if inverted:
            self.image = pygame.transform.flip(self.image, True, False)
            
        pygame.sprite.Sprite.__init__(self, group)


    def update(self, speed):
        self.rect[0] -= speed


class Bone(pygame.sprite.Sprite):
    
    def __init__(self, group, xpos, ypos):

        image_index = random.randint(1, 4)


        self.image = pygame.image.load(f'./assets/visuals/Bone_{image_index}.png')

        self.image = pygame.transform.scale(self.image, [100, 100])

        self.rect = pygame.Rect(xpos, ypos, 128, 128)

        pygame.sprite.Sprite.__init__(self, group)

    def update(self, speed):

        self.rect[0] -= speed