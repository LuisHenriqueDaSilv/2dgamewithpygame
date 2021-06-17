import pygame
import time

from Sprites.Player import Player
from Sprites.Ground import Ground
from Sprites.Zombie import Zombie
from Sprites.Void import Void
from Sprites.Wall import Wall

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

    zombieGroup = pygame.sprite.Group()
    zombie1 = Zombie(400 , 1400)
    zombie2 = Zombie(400, 3090)
    zombieGroup.add(zombie2)
    zombieGroup.add(zombie1)

    voidGroup = pygame.sprite.Group()
    void = Void()
    voidGroup.add(void)

    wallGroup = pygame.sprite.Group()
    wall = Wall(
        128*20-20,
        game_data['screen_height'] -100,
        False
    )

    wall2 = Wall(
        128*20 +(128 *4),
        game_data['screen_height'] -100,
        True
    )
    wall3 = Wall(
        3584 + 128 -20,
        game_data['screen_height'] -100,
        False        

    )

    wallGroup.add(wall)
    wallGroup.add(wall2)
    wallGroup.add(wall3)


    groundGroup = pygame.sprite.Group()

    for i in range(20):
        ground = Ground(game_data, i*128)
        groundGroup.add(ground)

    for i in range(3072, 3072+ (5*128), 128):
        ground = Ground(game_data, i)
        groundGroup.add(ground)



    def draw():

        screen.blit(BACKGROUND, (0,0))

        groundGroup.draw(screen)
        playerGroup.draw(screen)
        zombieGroup.draw(screen)
        voidGroup.draw(screen)
        #wallGroup.draw(screen)


    gameEnd = False


    while not gameEnd:

        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                gameEnd = True
                break


        player_colliding_ground =  pygame.sprite.groupcollide(playerGroup, groundGroup, False, False)


        if pygame.sprite.groupcollide(playerGroup, wallGroup, False, False):


            if player.last_button == 'a':
                playerGroup.update(falling=True, wall_position='b')

            else: 
                playerGroup.update(falling=True, wall_position='f')

        elif player_colliding_ground or player.jumping:
            playerGroup.update(falling=False)

        else: 
            playerGroup.update(falling=True)

            
        
        if pygame.sprite.groupcollide(playerGroup, zombieGroup, False, False):
            if player.attacking:
                pygame.sprite.groupcollide(playerGroup, zombieGroup, False, True)
            else:
                gameEnd = True
                gameOver()
                startGame()
                break

        if pygame.sprite.groupcollide(playerGroup, voidGroup, False, False):
            gameEnd = True
            gameOver()
            startGame()
            break



        if player.xSpeed > 0 and player.rect[0] >= game_data['screen_width'] /2:
            groundGroup.update(player.xSpeed)
            wallGroup.update(player.xSpeed)

        for zombie_sprite in zombieGroup: 

            if is_off_screen(zombie_sprite):
                zombieGroup.remove(zombie_sprite)

            else:

                if pygame.sprite.spritecollide(zombie_sprite, groundGroup, False):
                    zombie_sprite.update(falling=False, opponent=player)
                elif pygame.sprite.spritecollide(zombie_sprite, wallGroup, False):
                    zombie_sprite.update(falling=False, opponent=player)
                else: 
                    zombie_sprite.update(falling=True, opponent=player)



        pygame.sprite.groupcollide(zombieGroup, voidGroup, True, False)


        voidGroup.update()
        draw()

        pygame.display.flip()


startGame()