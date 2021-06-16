import pygame

class Zombie(pygame.sprite.Sprite):

    def __init__(self, xposition, yposition):

        pygame.sprite.Sprite.__init__(self)

        self.walking_images = [
            pygame.image.load('./assets/zombie/walk/Walk__0.png').convert_alpha(),
            pygame.image.load('./assets/zombie/walk/Walk__1.png').convert_alpha(),
            pygame.image.load('./assets/zombie/walk/Walk__2.png').convert_alpha(),
            pygame.image.load('./assets/zombie/walk/Walk__3.png').convert_alpha(),
            pygame.image.load('./assets/zombie/walk/Walk__4.png').convert_alpha(),
            pygame.image.load('./assets/zombie/walk/Walk__5.png').convert_alpha(),
            pygame.image.load('./assets/zombie/walk/Walk__6.png').convert_alpha(),
            pygame.image.load('./assets/zombie/walk/Walk__7.png').convert_alpha(),
            pygame.image.load('./assets/zombie/walk/Walk__8.png').convert_alpha(),
            pygame.image.load('./assets/zombie/walk/Walk__9.png').convert_alpha()
        ]

        self.image = self.walking_images[0]
        self.image = pygame.transform.scale(self.image, [70, 100])
        self.rect = pygame.Rect(yposition, xposition, 70, 100)
        self.current_image = 0

    def update(self, opponent, falling=False):
        
        if falling:
            self.rect[1] += 3

        self.current_image = (self.current_image + 1) % 10

        self.image = self.walking_images[self.current_image]
        self.image = pygame.transform.scale(self.image, [70, 100])

        if opponent.rect[0] >= opponent.gamedata['screen_width'] / 2 and opponent.xSpeed > 0:

            self.rect[0] += 1 - opponent.xSpeed /3
            
        else: 

            if opponent.rect[0] > self.rect[0]:
                self.rect[0] += 3

            else: 
                self.rect[0] -= 3 + opponent.xSpeed / 4
                self.image = pygame.transform.flip(self.image, True, False)
        

        
    