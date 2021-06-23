import pygame

#Assets
from gamemap.sprites.ground import Ground
from gamemap.sprites.dirt_block import DirtBlock
from gamemap.sprites.wall import Wall
from gamemap.sprites.final_box import FinalBox
from gamemap.sprites.visuals import ArrowSign, Tree, Sign, Bush, TombStone, Skeleton, Bone, TextLine

#MapConfig
from gamemap.mapConfig import level_1, level_1_visuals

class GameMap():

    def __init__(self, gamedata, screen):

        self.ground = Ground

        self.screen = screen

        self.screen_width = gamedata['screen_width']
        self.screen_height = gamedata['screen_height']

        self.groundGroup = pygame.sprite.Group()
        self.wallGroup = pygame.sprite.Group()
        self.visualsGroup = pygame.sprite.Group()
        self.boxGroup = pygame.sprite.Group()

        self.generate()

        self.background = pygame.image.load('./assets/Background.png').convert_alpha()
        self.background = pygame.transform.scale(
            self.background,
            [
                self.screen_width,
                self.screen_height
            ]
        )


    def generate(self):

        for sprite in level_1:

            if sprite["type"] == "Wall":
                Wall(
                    group=self.wallGroup,
                    xpos=sprite["xpos"],
                    ypos=sprite["ypos"],
                    ground=sprite["ground"],
                    inverted=sprite["inverted"],
                    repeat_y=sprite["repeat_y"]
                )
            elif sprite["type"] == "Ground":
                Ground(
                    group=self.groundGroup,
                    xpos=sprite["xpos"],
                    ypos=sprite["ypos"],
                    repeat_x=sprite["repeat_x"]
                )
            elif sprite["type"] == "FinalBox":
                FinalBox(
                    group=self.boxGroup,
                    xpos=sprite["xpos"],
                    ypos=sprite["ypos"]
                )

        for sprite in level_1_visuals:

            if sprite["type"] == "DirtBlock":
                DirtBlock(
                    group=self.visualsGroup,
                    xpos=sprite["xpos"],
                    ypos=sprite["ypos"],
                    curve=sprite["curve"],
                    inverted=sprite["inverted"],
                    repeat_x=sprite["repeat_x"],
                    repeat_y=sprite["repeat_y"]
                )
            elif sprite["type"] == "ArrowSign":
                ArrowSign(
                    group=self.visualsGroup,
                    xpos=sprite["xpos"],
                    ypos=sprite["ypos"],
                    inverted=sprite["inverted"]
                )
            elif sprite["type"] == "Tree":
                Tree(
                    group=self.visualsGroup,
                    xpos=sprite["xpos"],
                    ypos=sprite["ypos"]
                )
            elif sprite["type"] == "Sign":
                Sign(
                    group=self.visualsGroup,
                    xpos=sprite["xpos"],
                    ypos=sprite["ypos"],
                    text_pos=sprite["text_pos"],
                    text=sprite["text"]
                )
            elif sprite["type"] == "Bush":
                Bush(
                    group=self.visualsGroup,
                    xpos=sprite["xpos"],
                    ypos=sprite["ypos"]
                )
            elif sprite["type"] == "TombStone":
                TombStone(
                    group=self.visualsGroup,
                    xpos=sprite["xpos"],
                    ypos=sprite["ypos"]
                )
            elif sprite["type"] == "Skeleton":
                Skeleton(
                    group=self.visualsGroup,
                    xpos=sprite["xpos"],
                    ypos=sprite["ypos"],
                    inverted=sprite["inverted"]
                )
            elif sprite["type"] == "Bone":
                Bone(
                    group=self.visualsGroup,
                    xpos=sprite["xpos"],
                    ypos=sprite["ypos"]
                )
            elif sprite["type"] == "TextLine":
                TextLine(
                    group=self.visualsGroup,
                    xpos=sprite["xpos"],
                    ypos=sprite["ypos"],
                    text=sprite["text"],
                    color=sprite["color"]
                )

    def draw(self):

        self.screen.blit(self.background, (0,0))

        self.groundGroup.draw(self.screen)
        self.wallGroup.draw(self.screen)
        self.visualsGroup.draw(self.screen)
        self.boxGroup.draw(self.screen)

    def update(self, playerGroup, zombieGroup):


        player = playerGroup.sprites()[0]


        player_colliding_last_box = pygame.sprite.groupcollide(playerGroup, self.boxGroup, False, True)

        if player_colliding_last_box:
            player.end = True

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
        elif player_colliding_ground:
            playerGroup.update(falling=False)
        else: 
            playerGroup.update(falling=True)


        for zombie_sprite in zombieGroup:

            zombie_colliding_ground = pygame.sprite.spritecollide(zombie_sprite, self.groundGroup, False)
            zombie_colliding_wall = pygame.sprite.spritecollide(zombie_sprite, self.wallGroup, False)

            if zombie_colliding_wall and zombie_colliding_ground:
                if zombie_sprite.rect[0] <= player.rect[0]:
                    zombie_sprite.update(falling=False, opponent=player, wall_position='f')
                else:
                    zombie_sprite.update(falling=False, opponent=player, wall_position='b')

            elif zombie_colliding_wall:

                if zombie_sprite.rect[0] < player.rect[0]:
                    zombie_sprite.update(falling=False, opponent=player, wall_position='f')
                else:
                    zombie_sprite.update(falling=False, opponent=player, wall_position='b')

            elif zombie_colliding_ground:
                zombie_sprite.update(falling=False, opponent=player)
            else:
                zombie_sprite.update(falling=True, opponent=player)

        self.groundGroup.update(player.xSpeed)
        self.wallGroup.update(player.xSpeed)
        self.visualsGroup.update(player.xSpeed)
        self.boxGroup.update(player.xSpeed)