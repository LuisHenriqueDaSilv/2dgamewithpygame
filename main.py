import pygame
import time

from gamemap.gamemap import GameMap

#Sprites
from Sprites.Player import Player
from Sprites.Zombie import Zombie

pygame.init()


game_data = {
    'screen_width': 1152,
    'screen_height': 650,
}

screen = pygame.display.set_mode([
        game_data['screen_width'],
        game_data['screen_height']
])

pygame.display.set_caption('Ninja Saving The World (Game)') 

BACKGROUND = pygame.image.load('./assets/background.png').convert_alpha()
BACKGROUND = pygame.transform.scale(
    BACKGROUND,
    [
        game_data['screen_width'],
        game_data['screen_height']
    ]
)

clock = pygame.time.Clock()


def is_off_screen(sprite):
    return (sprite.rect[0]) < -(sprite.rect[2])

def gameOver():
    print('gameover')


def startGame():


    playerGroup = pygame.sprite.Group()
    player = Player(game_data)
    playerGroup.add(player)

    gamemap = GameMap(game_data, screen)


    zombieGroup = pygame.sprite.Group()

    zombie1 = Zombie(400 , 1400)
    zombie2 = Zombie(400, 3090)
    zombieGroup.add(zombie2)
    zombieGroup.add(zombie1)



    def draw():

        screen.blit(BACKGROUND, (0,0))

        gamemap.draw()
        playerGroup.draw(screen)
        zombieGroup.draw(screen)


    gameEnd = False


    while not gameEnd:


        clock.tick(30)

        gamemap.update(playerGroup, zombieGroup)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                gameEnd = True
                break
            
        
        if pygame.sprite.groupcollide(playerGroup, zombieGroup, False, False):
            if player.attacking:
                pygame.sprite.groupcollide(playerGroup, zombieGroup, False, True)
            else:
                gameEnd = True
                gameOver()
                startGame()
                break

        for zombie_sprite in zombieGroup: 

            if is_off_screen(zombie_sprite):
                zombieGroup.remove(zombie_sprite)

        draw()

        pygame.display.flip()


startGame()