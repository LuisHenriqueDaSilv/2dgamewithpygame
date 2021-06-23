import pygame
import time

from gamemap.gamemap import GameMap

#Sprites
from sprites.player import Player
from sprites.zombie import Zombie

pygame.init()
pygame.font.init()


game_data = {
    'screen_width': 1152,
    'screen_height': 650,
}

screen = pygame.display.set_mode([
        game_data['screen_width'],
        game_data['screen_height']
])

pygame.display.set_caption('Ninja Saving The World (Game)') 

clock = pygame.time.Clock()

def gameOver():

    font = pygame.font.SysFont("./assets/fonts/FFF_Tusj.ttf", 100)
    textSurf = font.render("Game over", True, (50, 168, 60))

    print('Gameover')

    screen.blit(textSurf, [400, game_data['screen_height']-128])
    pygame.display.flip()
    time.sleep(3)

def startGame():

    gamemap = GameMap(game_data, screen)

    playerGroup = pygame.sprite.Group()
    player = Player(game_data)
    playerGroup.add(player)


    zombieGroup = pygame.sprite.Group()

    Zombie(group=zombieGroup,xpos=29*128 , ypos=650-128-100)
    Zombie(group=zombieGroup, xpos=(36*128) , ypos=650-128-100)
    Zombie(group=zombieGroup,xpos=(37*128)-50 , ypos=650-128-100)
    Zombie(group=zombieGroup,xpos=(38*128)-10 , ypos=650-128-100)
    Zombie(group=zombieGroup,xpos=56*128 , ypos=650-128-100)


    def draw():

        gamemap.draw()
        playerGroup.draw(screen)
        zombieGroup.draw(screen)

    gameEnd = False        

    while not gameEnd:

        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameEnd = True
                break

        gamemap.update(playerGroup, zombieGroup)

            
        
        if pygame.sprite.groupcollide(playerGroup, zombieGroup, False, False):
            for zombie in zombieGroup:
                if zombie.rect[0] >= player.rect[0] and zombie.rect[0] <= player.rect[0] -50 + player.rect[2]:

                    if player.attacking or player.sliding:
                        pygame.sprite.groupcollide(playerGroup, zombieGroup, False, True)    
                    else:   
                        gameEnd = True
                        gameOver()
                        startGame()
                        break
                elif zombie.rect[0] <= player.rect[0] and player.rect[0] <= zombie.rect[0] + zombie.rect[2] -25:
                    if player.attacking or player.sliding:
                        pygame.sprite.groupcollide(playerGroup, zombieGroup, False, True)    
                    else:   
                        gameEnd = True
                        gameOver()
                        startGame()
                        break

        draw()
        pygame.display.flip()


startGame()