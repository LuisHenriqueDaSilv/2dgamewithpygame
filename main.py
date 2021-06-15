import pygame

from Player import Player
from Ground import Ground

pygame.init()


game_data = {
    'screen_width': 1152,
    'screen_height': 650
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

groundGroup = pygame.sprite.Group()

for i in range(20):
    ground = Ground(game_data,128*i)
    groundGroup.add(ground)


def draw():
    groundGroup.draw(screen)
    playerGroup.draw(screen)

def update():

    playerGroup.update()

    if player.xSpeed < 0 or player.rect[0] < game_data['screen_width'] /2:
        groundGroup.update(0)

    else:
        groundGroup.update(player.xSpeed)



clock = pygame.time.Clock()

while True:

    clock.tick(30)

    screen.blit(BACKGROUND, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break


    update()
    draw()

    pygame.display.flip()

