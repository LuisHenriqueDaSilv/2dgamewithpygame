import pygame

class FinalBox(pygame.sprite.Sprite):
    def __init__(self, group, xpos, ypos):
        
        self.image = pygame.image.load('./assets/visuals/Crate.png')
        self.rect = pygame.Rect(xpos, ypos-106, 106, 106)
        pygame.sprite.Sprite.__init__(self, group)

        self.font = pygame.font.SysFont("./assets/fonts/FFF_Tusj.ttf", 15)
        self.textSurf = self.font.render("Amostra do virus", True, (255,255,255))

        self.image.blit(self.textSurf, [12, 52])

    def update(self, speed):
        self.rect[0] -= speed