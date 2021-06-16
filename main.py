import pygame

from Player import Player
from Ground import Ground
from Zombie import Zombie

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


playerGroup = pygame.sprite.Group()
player = Player(game_data)
playerGroup.add(player)

zombieGroup = pygame.sprite.Group()


zombie = Zombie(4  , 500)
zombieGroup.add(zombie)


groundGroup = pygame.sprite.Group()

for i in range(20):
    ground = Ground(game_data,128*i)
    groundGroup.add(ground)


def draw():

    screen.blit(BACKGROUND, (0,0))

    groundGroup.draw(screen)
    playerGroup.draw(screen)
    zombieGroup.draw(screen)

clock = pygame.time.Clock()

while True:

    clock.tick(30)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break


    if pygame.sprite.groupcollide(playerGroup, groundGroup, False, False) or player.jumping:
        playerGroup.update(falling=False)
    else: 
        playerGroup.update(falling=True)
        
    
    if pygame.sprite.groupcollide(playerGroup, zombieGroup, False, False):
        if player.attacking:
            pygame.sprite.groupcollide(playerGroup, zombieGroup, False, True)
        else: 
            #add game over function here
            print('game over')


    for sprite in zombieGroup: 

        if pygame.sprite.spritecollide(sprite, groundGroup, False):
            sprite.update(falling=False, opponent=player)
        else: 
            sprite.update(falling=True, opponent=player)


    if player.xSpeed > 0 and player.rect[0] >= game_data['screen_width'] /2:
        groundGroup.update(player.xSpeed)

    draw()

    pygame.display.flip()