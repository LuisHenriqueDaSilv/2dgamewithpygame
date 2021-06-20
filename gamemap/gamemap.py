import pygame

#Assets
from gamemap.sprites.ground import Ground
from gamemap.sprites.dirt_block import DirtBlock
from gamemap.sprites.wall import Wall

class GameMap():

    def __init__(self, gamedata, screen):

        self.ground = Ground

        self.screen = screen

        self.screen_width = gamedata['screen_width']
        self.screen_height = gamedata['screen_height']

        self.groundGroup = pygame.sprite.Group()
        self.dirtBlockGroup = pygame.sprite.Group()
        self.wallGroup = pygame.sprite.Group()

        self.generate()


    def generate(self):

        dirt_block_1 = DirtBlock(xpos=-128, ypos=self.screen_height-128, inverted=True, curve=True)

        self.dirtBlockGroup.add(dirt_block_1)

        for i_x in range(2, 6):
            for i_y in range(1, 7):
                dirt_block = DirtBlock(xpos=-(i_x*128), ypos=self.screen_height-(i_y*128))
                self.dirtBlockGroup.add(dirt_block)


        for i in range(2,7):
            wall = Wall(xpos=-128, ypos=self.screen_height-(i*128), ground=False, inverted=True)
            self.wallGroup.add(wall)

        for i in range(20):
            ground = Ground(xpos=i*128, ypos=self.screen_height - 128)
            self.groundGroup.add(ground)
        
        dirt_block_2 = DirtBlock(xpos=128*20, ypos=self.screen_height - 128, inverted=False, curve=True)

        self.dirtBlockGroup.add(dirt_block_2)

        wall = Wall(xpos=128*20, ypos=self.screen_height -256, ground=True, inverted=False)
        self.wallGroup.add(wall)

        for i in range(128*21,128*24,128):
            
            ground = Ground(xpos=i, ypos=self.screen_height-256)
            self.groundGroup.add(ground)

            dirt_block = DirtBlock(xpos=i, ypos=self.screen_height-128)

            self.dirtBlockGroup.add(dirt_block)




    def draw(self):
        self.groundGroup.draw(self.screen)
        self.dirtBlockGroup.draw(self.screen)
        self.wallGroup.draw(self.screen)


    def update(self, playerGroup, zombieGroup):

        player = playerGroup.sprites()[0]


        player_colliding_ground = pygame.sprite.groupcollide(playerGroup, self.groundGroup, False, False)
        player_colliding_wall = pygame.sprite.groupcollide(playerGroup, self.wallGroup, False, False)

        if player_colliding_wall and player_colliding_ground:

            for wall_sprite in self.wallGroup:
                
                player_colliding_in_this_wall = pygame.Rect.colliderect(wall_sprite.rect, player)

                if player_colliding_in_this_wall:

                    if wall_sprite.ground:

                        if player.rect[1] +90 <= wall_sprite.rect[1]:
                            player.update(falling=False)
                        else:
                            wall_position = 'b' if player.xSpeed < 0 else 'f'
                            player.update(falling=False, wall_position=wall_position)

                    else:
                        wall_position = 'b' if player.xSpeed < 0 else 'f'

                        player.update(falling=False, wall_position=wall_position)

                    break

        elif player_colliding_wall:
            
            for wall_sprite in self.wallGroup:
                
                player_colliding_in_this_wall = pygame.Rect.colliderect(wall_sprite.rect, player)

                if player_colliding_in_this_wall:

                    if wall_sprite.ground:

                        if player.rect[1] +90 <= wall_sprite.rect[1]:
                            player.update(falling=False)
                        else:
                            wall_position = 'b' if player.xSpeed < 0 else 'f'
                            player.update(falling=True, wall_position=wall_position)

                    else:
                        wall_position = 'b' if player.xSpeed < 0 else 'f'

                        player.update(falling=True, wall_position=wall_position)

                    break
            
        elif player_colliding_ground:
            playerGroup.update(falling=False)
        else: 
            playerGroup.update(falling=True)



        for zombie_sprite in zombieGroup:

            zombie_colliding_ground = pygame.sprite.spritecollide(zombie_sprite, self.groundGroup, False, False)

            if zombie_colliding_ground:
                zombie_sprite.update(falling=False, opponent=player)
            else:
                zombie_sprite.update(falling=True, opponent=player)

        self.groundGroup.update(player.xSpeed)
        self.dirtBlockGroup.update(player.xSpeed)
        self.wallGroup.update(player.xSpeed)