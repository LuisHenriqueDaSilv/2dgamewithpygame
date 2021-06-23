import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, gamedata):

        self.gamedata = gamedata

        pygame.sprite.Sprite.__init__(self)

        self.idle_images = [
            pygame.image.load('./assets/player/idle/Idle_1.png').convert_alpha(),
            pygame.image.load('./assets/player/idle/Idle_2.png').convert_alpha(),
            pygame.image.load('./assets/player/idle/Idle_3.png').convert_alpha(),
            pygame.image.load('./assets/player/idle/Idle_4.png').convert_alpha(),
            pygame.image.load('./assets/player/idle/Idle_5.png').convert_alpha(),
            pygame.image.load('./assets/player/idle/Idle_6.png').convert_alpha(),
            pygame.image.load('./assets/player/idle/Idle_7.png').convert_alpha(),
            pygame.image.load('./assets/player/idle/Idle_8.png').convert_alpha(),
            pygame.image.load('./assets/player/idle/Idle_9.png').convert_alpha(),
            pygame.image.load('./assets/player/idle/Idle_10.png').convert_alpha()
        ]

        self.run_images = [
            pygame.image.load('./assets/player/run/Run_1.png').convert_alpha(),
            pygame.image.load('./assets/player/run/Run_2.png').convert_alpha(),
            pygame.image.load('./assets/player/run/Run_3.png').convert_alpha(),
            pygame.image.load('./assets/player/run/Run_4.png').convert_alpha(),
            pygame.image.load('./assets/player/run/Run_5.png').convert_alpha(),
            pygame.image.load('./assets/player/run/Run_6.png').convert_alpha(),
            pygame.image.load('./assets/player/run/Run_7.png').convert_alpha(),
            pygame.image.load('./assets/player/run/Run_8.png').convert_alpha(),
            pygame.image.load('./assets/player/run/Run_9.png').convert_alpha(),
            pygame.image.load('./assets/player/run/Run_10.png').convert_alpha()
        ]

        self.falling_images = [
            pygame.image.load('./assets/player/falling/Glide_1.png').convert_alpha(),
            pygame.image.load('./assets/player/falling/Glide_2.png').convert_alpha(),
            pygame.image.load('./assets/player/falling/Glide_3.png').convert_alpha(),
            pygame.image.load('./assets/player/falling/Glide_4.png').convert_alpha(),
            pygame.image.load('./assets/player/falling/Glide_5.png').convert_alpha(),
            pygame.image.load('./assets/player/falling/Glide_6.png').convert_alpha(),
            pygame.image.load('./assets/player/falling/Glide_7.png').convert_alpha(),
            pygame.image.load('./assets/player/falling/Glide_8.png').convert_alpha(),
            pygame.image.load('./assets/player/falling/Glide_9.png').convert_alpha(),
            pygame.image.load('./assets/player/falling/Glide_10.png').convert_alpha()
        ]

        self.attacking_images = [
            pygame.image.load('./assets/player/attack/Attack_1.png').convert_alpha(),
            pygame.image.load('./assets/player/attack/Attack_2.png').convert_alpha(),
            pygame.image.load('./assets/player/attack/Attack_3.png').convert_alpha(),
            pygame.image.load('./assets/player/attack/Attack_4.png').convert_alpha(),
            pygame.image.load('./assets/player/attack/Attack_5.png').convert_alpha(),
            pygame.image.load('./assets/player/attack/Attack_6.png').convert_alpha(),
            pygame.image.load('./assets/player/attack/Attack_7.png').convert_alpha(),
            pygame.image.load('./assets/player/attack/Attack_8.png').convert_alpha(),
            pygame.image.load('./assets/player/attack/Attack_9.png').convert_alpha(),
            pygame.image.load('./assets/player/attack/Attack_10.png').convert_alpha(),
        ]
        
        self.jumping_images = [
            pygame.image.load('./assets/player/jump/Jump_1.png').convert_alpha(),
            pygame.image.load('./assets/player/jump/Jump_2.png').convert_alpha(),
            pygame.image.load('./assets/player/jump/Jump_3.png').convert_alpha(),
            pygame.image.load('./assets/player/jump/Jump_4.png').convert_alpha(),
            pygame.image.load('./assets/player/jump/Jump_5.png').convert_alpha(),
            pygame.image.load('./assets/player/jump/Jump_6.png').convert_alpha()
        ]

        self.sliding_images = [
            pygame.image.load('./assets/player/slide/Slide_1.png').convert_alpha(),
            pygame.image.load('./assets/player/slide/Slide_2.png').convert_alpha(),
            pygame.image.load('./assets/player/slide/Slide_3.png').convert_alpha(),
            pygame.image.load('./assets/player/slide/Slide_4.png').convert_alpha(),
            pygame.image.load('./assets/player/slide/Slide_5.png').convert_alpha(),
            pygame.image.load('./assets/player/slide/Slide_6.png').convert_alpha(),
            pygame.image.load('./assets/player/slide/Slide_7.png').convert_alpha(),
            pygame.image.load('./assets/player/slide/Slide_8.png').convert_alpha(),
            pygame.image.load('./assets/player/slide/Slide_9.png').convert_alpha(),
            pygame.image.load('./assets/player/slide/Slide_10.png').convert_alpha()
        ]


        self.image = pygame.transform.scale(self.idle_images[0], [70,100])
        self.rect = pygame.Rect(
            self.gamedata['screen_width'] / 2,
            self.gamedata['screen_height']-128-100, #screen height - ground height - Player height
            70, 
            100 

        )

        self.current_image = 0
        self.xSpeed = 0

        self.last_button = 'd'
        self.jumping = False
        self.jump_covered = 0
        self.jump_limit = 200
        self.jump_speed = 20

        self.attacking = False
        self.attacking_frames = 0
        self.last_wall = None

        self.sliding = False

        self.end = False

        

    def update(self, falling=False, wall_position=None):

        if self.rect[0] > 1152:
            pygame.quit()
            return

        if self.end:
            self.xSpeed = 0
            self.rect[0] += 5

        if self.last_wall == None:
            self.last_wall = wall_position
        elif self.last_wall == wall_position:
            self.xSpeed =0
        elif wall_position == None:
            self.last_wall = None

        if self.attacking:
            self.rect[2] = 100
        else:
            self.rect[2] = 70


        if self.jumping:

            if self.rect[0] < 1:
                self.xSpeed = 0

            if self.current_image < 5:
                self.current_image += 1

            if self.jump_covered >= self.jump_limit:
                self.jumping = False
                self.jump_covered = 0
                self.xSpeed /= 2
                self.jump_speed = 20

            else: 
                self.image = self.jumping_images[self.current_image]
                self.image = pygame.transform.scale(self.image, [70, 100])

                self.rect[1] -= self.jump_speed
                self.jump_covered += self.jump_speed
                self.jump_speed -= 1

                if self.last_button == 'a':
                    self.image = pygame.transform.flip(self.image, True, False)

                if self.rect[0] < self.gamedata['screen_width']/2:
                    self.rect[0] += self.xSpeed

            return
        else:
            self.current_image = (self.current_image + 1) %10


        if falling:
            self.rect[1] += 3
            self.image = self.falling_images[self.current_image]
            self.image = pygame.transform.scale(self.image, [70, 100])
            
            if self.last_wall == 'b':
                self.image = pygame.transform.flip(self.image, True, False)


        key = pygame.key.get_pressed()


        if self.attacking:

            if self.attacking_frames > 9:
                self.attacking = False
                self.attacking_frames = 0

            else: 
                self.image = self.attacking_images[self.attacking_frames]
                self.image = pygame.transform.scale(self.image, [100, 110])
                self.attacking_frames += 1
                
                if self.last_button == 'a':
                    self.image = pygame.transform.flip(self.image, True, False)

            return

        elif self.sliding:

            self.image = self.sliding_images[self.current_image]
            self.image = pygame.transform.scale(self.image, [70,80])

            if self.xSpeed > 0:
                self.xSpeed -= 0.5
            elif self.xSpeed < 0:
                self.xSpeed += 0.5
                self.image = pygame.transform.flip(self.image, True, False)

            if (self.xSpeed > -5 and self.xSpeed <= 0) or (self.xSpeed < 5 and self.xSpeed >=0):
                self.sliding = False
                self.xSpeed = 0

            return


        if key[pygame.K_d] and not self.sliding and not self.end:
            self.last_button = 'd'

            if self.xSpeed < 0:
                self.xSpeed = 0

            if self.xSpeed < 10:
                self.xSpeed +=1
        elif key[pygame.K_a] and not self.sliding and not self.end:
            self.last_button = 'a'

            if self.xSpeed > 0:
                self.xSpeed = 0
            if self.xSpeed > -10:
                self.xSpeed -= 1

        else:

            if self.xSpeed != 0 and not falling and not self.sliding:
                self.xSpeed = 0


        if key[pygame.K_SPACE]:
            if not falling and not self.attacking and not self.sliding:
                self.jumping = True
                self.current_image = 0


        player_speed_in_limit = self.xSpeed == 10 or self.xSpeed == -10
        if key[pygame.K_f]:
            if not self.attacking and not falling and not self.sliding: 
                self.attacking = True
                self.current_image = 0
                self.xSpeed = 0

        elif key[pygame.K_s] and player_speed_in_limit:
            if not self.attacking and not falling and not self.sliding:
                self.current_image = 0
                self.sliding = True
                if self.xSpeed > 0:
                    self.xSpeed = 15
                else:
                    self.xSpeed = -15
            



        if self.xSpeed == 0 and not falling and not self.end:

            self.image = self.idle_images[self.current_image]
            self.image = pygame.transform.scale(self.image, [45, 100])
            
            if self.last_button == 'a':
                self.image = pygame.transform.flip(self.image, True, False)

            return
            


        if not falling:

            self.image = self.run_images[self.current_image]
            self.image = pygame.transform.scale(self.image, [70, 100])

            if self.last_wall == 'b':
                self.image = pygame.transform.flip(self.image, True, False)


        if self.xSpeed < 0 and self.last_wall != 'b':

            self.image = pygame.transform.flip(self.image, True, False)

        if self.last_wall == 'b' and self.xSpeed < 0:
            self.xSpeed =0

        elif self.last_wall == 'f' and self.xSpeed > 0:
            self.xSpeed = 0