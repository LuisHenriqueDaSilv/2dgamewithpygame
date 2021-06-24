import pygame

#Gamemap
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
    textSurf = font.render("Game over", True, (201, 18, 49))

    print('Gameover')

    screen.blit(textSurf, [400, game_data['screen_height']-128])
    pygame.display.flip()

def startGame():

    gamemap = GameMap(game_data)

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

        gamemap.draw(screen)
        playerGroup.draw(screen)
        zombieGroup.draw(screen)

    gameEnd = False        

    while not gameEnd:

        draw()
        pygame.display.flip()

        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameEnd = True
                break

        if player.died:
            gameEnd = True
            gameOver()
            startGame()
            break
        elif player.dying:
            player.update()
            continue

        gamemap.update(playerGroup, zombieGroup)

        player_group_colliding_zombie_group = pygame.sprite.groupcollide(playerGroup, zombieGroup, False, False)

        if player_group_colliding_zombie_group:

            for zombie in zombieGroup:

                zombie_colliding_in_left = zombie.rect[0] >= player.rect[0] and zombie.rect[0] <= player.rect[0] -50 + player.rect[2]
                zombie_colliding_in_right = zombie.rect[0] <= player.rect[0] and player.rect[0] <= zombie.rect[0] + zombie.rect[2] -25

                if zombie_colliding_in_left or zombie_colliding_in_right:

                    if player.attacking or player.sliding:
                        pygame.sprite.groupcollide(playerGroup, zombieGroup, False, True)    
                    else:
                        player.set_dying()



startGame()