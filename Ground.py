import pygame

class Ground(pygame.sprite.Sprite):
    
    def __init__(self, game_data, xpos):

        self.game_data =game_data
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('./assets/ground/Ground__01.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, [128, 128])

        self.rect = pygame.Rect(
            xpos,
            game_data['screen_height']-128,
            100, 
            100
        )
    
    def update(self, speed):
        self.rect[0] -= speed