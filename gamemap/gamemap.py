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

    def __init__(self, gamedata):


        self.ground = Ground


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
        
        self.win_sound = pygame.mixer.Sound('./assets/audio/win.wav')
        self.win_sound.set_volume(0.3)
        
        pygame.mixer.music.set_volume(0.7)
        pygame.mixer.music.load('./assets/audio/background.ogg')
        pygame.mixer.music.play(-1)


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

    def draw(self, screen):

        screen.blit(self.background, (0,0))

        self.groundGroup.draw(screen)
        self.wallGroup.draw(screen)
        self.visualsGroup.draw(screen)
        self.boxGroup.draw(screen)

    def update(self, playerGroup, zombieGroup):

        player = playerGroup.sprites()[0]


        player_colliding_last_box = pygame.sprite.groupcollide(playerGroup, self.boxGroup, False, True)

        if player_colliding_last_box:
            pygame.mixer.music.set_volume(0.2)
            self.win_sound.play()
            player.end = True


        player_colliding_ground = pygame.sprite.groupcollide(playerGroup, self.groundGroup, False, False)
        player_colliding_wall = pygame.sprite.groupcollide(playerGroup, self.wallGroup, False, False)

        if player_colliding_wall:

            for wall_sprite in self.wallGroup:

                player_colliding_in_this_wall = pygame.Rect.colliderect(wall_sprite.rect, player)

                if player_colliding_in_this_wall:

                    wall_position = None

                    if player.rect[0] >= wall_sprite.rect[0]:
                        wall_position='b'
                    elif player.rect[0] <= wall_sprite.rect[0]+player.rect[2]:
                        wall_position = 'f'

                    if wall_sprite.ground:

                        player_falling_in_ground =  player.rect[1] + player.rect[3]-20<= wall_sprite.rect[1]

                        if player_falling_in_ground:
                            player.update(falling=not player_falling_in_ground)
                        else:
                            player.update(falling=not player_colliding_ground, wall_position=wall_position)
                    else:    
                        player.update(falling=not player_colliding_ground, wall_position=wall_position)

                    break

        else:
            player.update(falling=not player_colliding_ground)



        for zombie_sprite in zombieGroup:

            zombie_colliding_ground = pygame.sprite.spritecollide(zombie_sprite, self.groundGroup, False)
            zombie_colliding_wall = pygame.sprite.spritecollide(zombie_sprite, self.wallGroup, False)

            if zombie_colliding_wall:

                for wall_sprite in self.wallGroup:

                    zombie_colliding_in_this_wall = pygame.Rect.colliderect(wall_sprite.rect, zombie_sprite.rect)

                    if zombie_colliding_in_this_wall:

                        wall_position = None

                        if zombie_sprite.rect[0] >= wall_sprite.rect[0]:
                            wall_position='b'
                        elif zombie_sprite.rect[0] <= wall_sprite.rect[0]+zombie_sprite.rect[2]:
                            wall_position = 'f'

                        if zombie_colliding_ground:
                            zombie_sprite.update(falling=False, opponent=player,wall_position=wall_position)
                        else:
                            zombie_sprite.update(falling=not wall_sprite.ground, opponent=player,wall_position=wall_position)

                        break

            else:
                zombie_sprite.update(falling=not zombie_colliding_ground, opponent=player)


        self.groundGroup.update(player.xSpeed)
        self.wallGroup.update(player.xSpeed)
        self.visualsGroup.update(player.xSpeed)
        self.boxGroup.update(player.xSpeed)