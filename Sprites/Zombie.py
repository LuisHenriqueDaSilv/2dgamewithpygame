import pygame


class Zombie(pygame.sprite.Sprite):

    def __init__(self, group, xpos, ypos):


        self.walking_images = [
            pygame.image.load('./assets/zombie/walk/Walk__0.png').convert_alpha(),
            pygame.image.load('./assets/zombie/walk/Walk__1.png').convert_alpha(),
            pygame.image.load('./assets/zombie/walk/Walk__2.png').convert_alpha(),
            pygame.image.load('./assets/zombie/walk/Walk__3.png').convert_alpha(),
            pygame.image.load('./assets/zombie/walk/Walk__4.png').convert_alpha(),
            pygame.image.load('./assets/zombie/walk/Walk__5.png').convert_alpha(),
            pygame.image.load('./assets/zombie/walk/Walk__6.png').convert_alpha(),
            pygame.image.load('./assets/zombie/walk/Walk__7.png').convert_alpha(),
            pygame.image.load('./assets/zombie/walk/Walk__8.png').convert_alpha(),
            pygame.image.load('./assets/zombie/walk/Walk__9.png').convert_alpha()
        ]

        self.idle_images = [
            pygame.image.load('./assets/zombie/idle/Idle__01.png').convert_alpha(),
            pygame.image.load('./assets/zombie/idle/Idle__02.png').convert_alpha(),
            pygame.image.load('./assets/zombie/idle/Idle__03.png').convert_alpha(),
            pygame.image.load('./assets/zombie/idle/Idle__04.png').convert_alpha(),
            pygame.image.load('./assets/zombie/idle/Idle__05.png').convert_alpha(),
            pygame.image.load('./assets/zombie/idle/Idle__06.png').convert_alpha(),
            pygame.image.load('./assets/zombie/idle/Idle__07.png').convert_alpha(),
            pygame.image.load('./assets/zombie/idle/Idle__08.png').convert_alpha(),
            pygame.image.load('./assets/zombie/idle/Idle__09.png').convert_alpha(),
            pygame.image.load('./assets/zombie/idle/Idle__10.png').convert_alpha(),
            pygame.image.load('./assets/zombie/idle/Idle__11.png').convert_alpha(),
            pygame.image.load('./assets/zombie/idle/Idle__12.png').convert_alpha(),
            pygame.image.load('./assets/zombie/idle/Idle__13.png').convert_alpha(),
            pygame.image.load('./assets/zombie/idle/Idle__14.png').convert_alpha(),
            pygame.image.load('./assets/zombie/idle/Idle__15.png').convert_alpha()

        ]

        self.image = self.walking_images[0]
        self.image = pygame.transform.scale(self.image, [70, 100])
        self.rect = pygame.Rect(xpos, ypos, 50, 100)
        self.current_image = 0

        pygame.sprite.Sprite.__init__(self, group)


    def update(self, opponent, falling=False, wall_position=None):


        is_off_screen_and_front_player = self.rect[0] > opponent.rect[0] + (opponent.gamedata['screen_width']/2)
        is_off_screen_and_back_player = (self.rect[0]) < -(self.rect[2])
        
        if falling:
            self.rect[1] += 3

        if wall_position != None:
            self.current_image = (self.current_image + 1) % 15
            self.image = self.idle_images[self.current_image]
            self.image = pygame.transform.scale(self.image, [70, 100])
        else:
            self.current_image = (self.current_image + 1) % 10
            self.image = self.walking_images[self.current_image]
            self.image = pygame.transform.scale(self.image, [70, 100])


        if is_off_screen_and_front_player: 
            self.rect[0] -= opponent.xSpeed
            return
        elif is_off_screen_and_back_player:
            self.rect[0] -= opponent.xSpeed
            return

        else:

            if wall_position == 'f':
                
                if opponent.rect[0] >= self.rect[0]:
                    if opponent.xSpeed > 0:
                        self.rect[0] -= opponent.xSpeed
                else:
                    if opponent.xSpeed > 0:
                        self.rect[0] -= 5 - opponent.xSpeed * 0.7

                    else:
                        self.rect[0] -= 5

            else:
                if opponent.rect[0] >= self.rect[0]:

                    if opponent.xSpeed > 0:
                        self.rect[0] -= 5
                    else: 
                        self.rect[0] += 5 - opponent.xSpeed * 0.7
                else: 

                    self.image = pygame.transform.flip(self.image, True, False)

                    if opponent.xSpeed < 0:
                        self.rect[0] += 5
                    else: 
                        self.rect[0] -= 5 + opponent.xSpeed * 0.7    

