import pygame

#Assets
from gamemap.sprites.ground import Ground
from gamemap.sprites.dirty_curve import DirtyCurve

class GameMap():

    def __init__(self, gamedata, screen):

        self.ground = Ground

        self.screen = screen

        self.screen_width = gamedata['screen_width']
        self.screen_height = gamedata['screen_height']

        self.groundGroup = pygame.sprite.Group()
        self.dirtyCurveGroup = pygame.sprite.Group()

        self.generate()


    def generate(self):

        for i in range(20):
            ground = Ground(i*128, self.screen_height - 128)
            self.groundGroup.add(ground)
        
        dirty_curve = DirtyCurve(128*20, self.screen_height - 128)

        self.dirtyCurveGroup.add(dirty_curve)



    def draw(self):
        self.groundGroup.draw(self.screen)
        self.dirtyCurveGroup.draw(self.screen)


    def update(self, playerGroup, zombieGroup):

        player = playerGroup.sprites()[0]

        if player.rect[0] >= self.screen_width /2:
            self.groundGroup.update(player.xSpeed)
            self.dirtyCurveGroup.update(player.xSpeed)


        player_colliding_ground = pygame.sprite.groupcollide(playerGroup, self.groundGroup, False, False)

        if player_colliding_ground:
            playerGroup.update(falling=False)
        else: 
            playerGroup.update(falling=True)

        for zombie_sprite in zombieGroup:

            zombie_colliding_ground = pygame.sprite.groupcollide(zombieGroup, self.groundGroup, False, False)

            if zombie_colliding_ground:
                zombie_sprite.update(falling=False, opponent=player)
            else:
                zombieGroup.update(falling=True, opponent=player)