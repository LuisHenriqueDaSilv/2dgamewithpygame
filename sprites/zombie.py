import pygame


class Zombie(pygame.sprite.Sprite):

    def __init__(self, group, xpos, ypos):


        self.walking_images = [
            pygame.image.load('./assets/zombie/walk/Walk_1.png').convert_alpha(),
            pygame.image.load('./assets/zombie/walk/Walk_1.png').convert_alpha(),
            pygame.image.load('./assets/zombie/walk/Walk_2.png').convert_alpha(),
            pygame.image.load('./assets/zombie/walk/Walk_3.png').convert_alpha(),
            pygame.image.load('./assets/zombie/walk/Walk_4.png').convert_alpha(),
            pygame.image.load('./assets/zombie/walk/Walk_5.png').convert_alpha(),
            pygame.image.load('./assets/zombie/walk/Walk_6.png').convert_alpha(),
            pygame.image.load('./assets/zombie/walk/Walk_7.png').convert_alpha(),
            pygame.image.load('./assets/zombie/walk/Walk_8.png').convert_alpha(),
            pygame.image.load('./assets/zombie/walk/Walk_9.png').convert_alpha(),
            pygame.image.load('./assets/zombie/walk/Walk_10.png').convert_alpha(),
        ]

        self.idle_images = [
            pygame.image.load('./assets/zombie/idle/Idle_1.png'),
            pygame.image.load('./assets/zombie/idle/Idle_2.png'),
            pygame.image.load('./assets/zombie/idle/Idle_3.png'),
            pygame.image.load('./assets/zombie/idle/Idle_4.png'),
            pygame.image.load('./assets/zombie/idle/Idle_5.png'),
            pygame.image.load('./assets/zombie/idle/Idle_6.png'),
            pygame.image.load('./assets/zombie/idle/Idle_7.png'),
            pygame.image.load('./assets/zombie/idle/Idle_8.png'),
            pygame.image.load('./assets/zombie/idle/Idle_9.png'),
            pygame.image.load('./assets/zombie/idle/Idle_10.png'),
            pygame.image.load('./assets/zombie/idle/Idle_11.png'),
            pygame.image.load('./assets/zombie/idle/Idle_12.png'),
            pygame.image.load('./assets/zombie/idle/Idle_13.png'),
            pygame.image.load('./assets/zombie/idle/Idle_14.png'),
            pygame.image.load('./assets/zombie/idle/Idle_15.png')

        ]

        self.image = self.walking_images[0]
        self.image = pygame.transform.scale(self.image, [70, 100])
        self.rect = pygame.Rect(xpos, ypos, 70, 100)
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

            elif wall_position == 'b':

                if opponent.rect[0] <= self.rect[0]:
                    if opponent.xSpeed < 0:
                        self.rect[0] -= opponent.xSpeed
                else:
                    if opponent.xSpeed < 0:
                        self.rect[0] -= opponent.xSpeed
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

