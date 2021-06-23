import pygame

#Assets
from gamemap.sprites.ground import Ground
from gamemap.sprites.dirt_block import DirtBlock
from gamemap.sprites.wall import Wall
from gamemap.sprites.final_box import FinalBox
from gamemap.sprites.visuals import ArrowSign, Tree, Sign, Bush, TombStone, Skeleton, Bone, TextLine

#MapConfig
from gamemap.mapConfig import level_1

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



        DirtBlock(group=self.visualsGroup,xpos=-128, ypos=self.screen_height, inverted=True, curve=True)
        DirtBlock(group=self.visualsGroup, xpos=-(5*128), ypos=self.screen_height, repeat_y=6, repeat_x=4)
        #Wall(group=self.wallGroup, xpos=-128, ypos=self.screen_height-128, ground=False, inverted=True, repeat_y=5)
        #Ground(group=self.groundGroup,xpos=0, ypos=self.screen_height, repeat_x=20)
        
        Sign(group=self.visualsGroup,xpos=0, ypos=(self.screen_height- 93-128), text="Inicio", text_pos=[20, 20])
        TombStone(group=self.visualsGroup, xpos=2*128, ypos=self.screen_height-128-76)
        TombStone(group=self.visualsGroup, xpos=2*128+40, ypos=self.screen_height-128-76)
        Tree(group=self.visualsGroup,xpos=(self.screen_width/2-100), ypos=(self.screen_height - 239 - 128))
        Bush(group=self.visualsGroup, xpos=(self.screen_width/2+300), ypos=(self.screen_height - 64-128))
        ArrowSign(group=self.visualsGroup, xpos=4*128, ypos=self.screen_height-128-87)
        TextLine(group=self.visualsGroup, xpos=11*128+50, ypos=400, text="Objetivo da missão:", color=(214, 63, 49))
        TextLine(group=self.visualsGroup, xpos=11*128, ypos=425, text="Atravessar o cemitério e extrair ", color=(255,255,255) )
        TextLine(group=self.visualsGroup, xpos=11*128+50, ypos=450, text="a amostra do vírus", color=(255,255,255))
        TextLine(group=self.visualsGroup, xpos=11*128, ypos=475, text="para o desenvolvimento da cura.", color=(255,255,255))
        TombStone(group=self.visualsGroup, xpos=15*128, ypos=self.screen_height-128-76)
        TombStone(group=self.visualsGroup, xpos=15*128+64, ypos=self.screen_height-128-76)
        TombStone(group=self.visualsGroup, xpos=16*128, ypos=self.screen_height-128-76)
        Skeleton(group=self.visualsGroup, xpos=16*128-30, ypos=self.screen_height-128-25)
        
        DirtBlock(group=self.visualsGroup,xpos=128*20, ypos=self.screen_height, inverted=False, curve=True)
        
        Tree(group=self.visualsGroup, xpos=128*16,ypos=self.screen_height - 239-128)
        Bush(group=self.visualsGroup, xpos=128*19+28, ypos=(self.screen_height - 64-128))

        #Wall(group=self.wallGroup, xpos=128*20, ypos=self.screen_height -128, ground=True, inverted=False)            
        #Ground(group=self.groundGroup,xpos=128*21, ypos=self.screen_height-128, repeat_x=3)

        DirtBlock(group=self.visualsGroup, xpos=128*21, ypos=self.screen_height, repeat_x=3)
        TextLine(group=self.visualsGroup, xpos=22*128, ypos=400, text="Como jogar:", color=(214, 63, 49))
        TextLine(group=self.visualsGroup, xpos=22*128, ypos=425, text="Spaço: Pula ", color=(255,255,255))
        TextLine(group=self.visualsGroup, xpos=22*128, ypos=450, text="A-D: Anda", color=(255,255,255))
        TextLine(group=self.visualsGroup, xpos=22*128, ypos=475, text="F: Ataca", color=(255,255,255))
        TextLine(group=self.visualsGroup, xpos=22*128, ypos=500, text="S: ataque rapido", color=(255,255,255))
        ArrowSign(group=self.visualsGroup, xpos=24*128, ypos=self.screen_height-256-87)
        #Wall(group=self.wallGroup,xpos=128*24, ypos=self.screen_height-128, ground=True, inverted=True)
        DirtBlock(group=self.visualsGroup, xpos=128*24, ypos=self.screen_height, curve=True, inverted=True)
        Bone(group=self.visualsGroup, xpos=2*128, ypos=self.screen_height-128)
        Bone(group=self.visualsGroup, xpos=7*128, ypos=self.screen_height-100)
        Bone(group=self.visualsGroup, xpos=18*128, ypos=self.screen_height-120)
        Bone(group=self.visualsGroup, xpos=21*128, ypos=self.screen_height-256)
        Bone(group=self.visualsGroup, xpos=23*128, ypos=self.screen_height-70)
        
        #Ground(group=self.groundGroup,xpos=128*25, ypos=self.screen_height, repeat_x=18)
        
        Bush(group=self.visualsGroup, xpos=128*27+28, ypos=(self.screen_height - 64-128))
        TombStone(group=self.visualsGroup, xpos=29*128, ypos=self.screen_height-128-76)
        Bone(group=self.visualsGroup, xpos=27*128, ypos=self.screen_height-90)
        Tree(group=self.visualsGroup, xpos=31*128, ypos=self.screen_height-128-239)
        TombStone(group=self.visualsGroup, xpos=(34*128), ypos=self.screen_height-128-76)
        Bone(group=self.visualsGroup, xpos=34*128, ypos=self.screen_height-90)
        Bush(group=self.visualsGroup, xpos=128*35, ypos=(self.screen_height - 64-128))
        TombStone(group=self.visualsGroup, xpos=(36*128), ypos=self.screen_height-128-76)
        TombStone(group=self.visualsGroup, xpos=(37*128)-50, ypos=self.screen_height-128-76)
        TombStone(group=self.visualsGroup, xpos=(38*128)-100, ypos=self.screen_height-128-76)
        TombStone(group=self.visualsGroup, xpos=(39*128)-150, ypos=self.screen_height-128-76)
        ArrowSign(group=self.visualsGroup, xpos=41*128, ypos=self.screen_height-128-87)
        Tree(group=self.visualsGroup, xpos=39*128, ypos=self.screen_height-128-239)
        DirtBlock(group=self.visualsGroup, xpos=43*128, ypos=self.screen_height, curve=True)
        
        #Wall(group=self.wallGroup, xpos=43*128, ypos=self.screen_height-128, ground=True)
        #Ground(group=self.groundGroup, xpos=44*128, ypos=self.screen_height-128)
        
        DirtBlock(group=self.visualsGroup, xpos=45*128, ypos=self.screen_height-128, curve=True)
        DirtBlock(group=self.visualsGroup, xpos=44*128, ypos=self.screen_height, repeat_x=4)
        DirtBlock(group=self.visualsGroup, xpos=46*128, ypos=self.screen_height-128, repeat_x=2)


        #Wall(group=self.wallGroup, xpos=45*128, ypos=self.screen_height-256, ground=True)
        #Ground(group=self.groundGroup, xpos=44*128, ypos=self.screen_height-128)
        #Ground(group=self.groundGroup, xpos=46*128, ypos=self.screen_height-256, repeat_x=2)
        #Wall(group=self.wallGroup, xpos=48*128, ypos=self.screen_height-256, ground=True, inverted=True)
        #Wall(group=self.wallGroup, xpos=48*128, ypos=self.screen_height-128, ground=False, inverted=True)
        

        DirtBlock(group=self.visualsGroup, xpos=48*128, ypos=self.screen_height, curve=True, inverted=True)
        
        #Ground(group=self.groundGroup, xpos=49*128, ypos=self.screen_height, repeat_x=21)
        #Wall(group=self.wallGroup, xpos=60*128, ypos=self.screen_height-128, ground=False, repeat_y=5)
        
        DirtBlock(group=self.visualsGroup, xpos=61*128, ypos=self.screen_height-128, repeat_x=4, repeat_y=4)
        #FinalBox(group=self.boxGroup, xpos=59*128, ypos=self.screen_height-128-106)



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