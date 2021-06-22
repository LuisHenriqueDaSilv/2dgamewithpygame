import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, gamedata):

        self.gamedata = gamedata

        pygame.sprite.Sprite.__init__(self)

        self.idle_images = [
            pygame.image.load('./assets/player/idle/Idle__000.png').convert_alpha(),
            pygame.image.load('./assets/player/idle/Idle__001.png').convert_alpha(),
            pygame.image.load('./assets/player/idle/Idle__002.png').convert_alpha(),
            pygame.image.load('./assets/player/idle/Idle__003.png').convert_alpha(),
            pygame.image.load('./assets/player/idle/Idle__004.png').convert_alpha(),
            pygame.image.load('./assets/player/idle/Idle__005.png').convert_alpha(),
            pygame.image.load('./assets/player/idle/Idle__006.png').convert_alpha(),
            pygame.image.load('./assets/player/idle/Idle__007.png').convert_alpha(),
            pygame.image.load('./assets/player/idle/Idle__008.png').convert_alpha(),
            pygame.image.load('./assets/player/idle/Idle__009.png').convert_alpha()
        ]

        self.run_images = [
            pygame.image.load('./assets/player/run/Run__000.png').convert_alpha(),
            pygame.image.load('./assets/player/run/Run__001.png').convert_alpha(),
            pygame.image.load('./assets/player/run/Run__002.png').convert_alpha(),
            pygame.image.load('./assets/player/run/Run__003.png').convert_alpha(),
            pygame.image.load('./assets/player/run/Run__004.png').convert_alpha(),
            pygame.image.load('./assets/player/run/Run__005.png').convert_alpha(),
            pygame.image.load('./assets/player/run/Run__006.png').convert_alpha(),
            pygame.image.load('./assets/player/run/Run__007.png').convert_alpha(),
            pygame.image.load('./assets/player/run/Run__008.png').convert_alpha(),
            pygame.image.load('./assets/player/run/Run__009.png').convert_alpha()
        ]

        self.falling_images = [
            pygame.image.load('./assets/player/falling/Glide_000.png').convert_alpha(),
            pygame.image.load('./assets/player/falling/Glide_001.png').convert_alpha(),
            pygame.image.load('./assets/player/falling/Glide_002.png').convert_alpha(),
            pygame.image.load('./assets/player/falling/Glide_003.png').convert_alpha(),
            pygame.image.load('./assets/player/falling/Glide_004.png').convert_alpha(),
            pygame.image.load('./assets/player/falling/Glide_005.png').convert_alpha(),
            pygame.image.load('./assets/player/falling/Glide_006.png').convert_alpha(),
            pygame.image.load('./assets/player/falling/Glide_007.png').convert_alpha(),
            pygame.image.load('./assets/player/falling/Glide_008.png').convert_alpha(),
            pygame.image.load('./assets/player/falling/Glide_009.png').convert_alpha()
        ]

        self.attacking_images = [
            pygame.image.load('./assets/player/attack/Attack__000.png').convert_alpha(),
            pygame.image.load('./assets/player/attack/Attack__001.png').convert_alpha(),
            pygame.image.load('./assets/player/attack/Attack__002.png').convert_alpha(),
            pygame.image.load('./assets/player/attack/Attack__003.png').convert_alpha(),
            pygame.image.load('./assets/player/attack/Attack__004.png').convert_alpha(),
            pygame.image.load('./assets/player/attack/Attack__005.png').convert_alpha(),
            pygame.image.load('./assets/player/attack/Attack__006.png').convert_alpha(),
            pygame.image.load('./assets/player/attack/Attack__007.png').convert_alpha(),
            pygame.image.load('./assets/player/attack/Attack__008.png').convert_alpha(),
            pygame.image.load('./assets/player/attack/Attack__009.png').convert_alpha()
        ]
        
        self.jumping_images = [
            pygame.image.load('./assets/player/jump/Jump__000.png').convert_alpha(),
            pygame.image.load('./assets/player/jump/Jump__001.png').convert_alpha(),
            pygame.image.load('./assets/player/jump/Jump__002.png').convert_alpha(),
            pygame.image.load('./assets/player/jump/Jump__003.png').convert_alpha(),
            pygame.image.load('./assets/player/jump/Jump__004.png').convert_alpha(),
            pygame.image.load('./assets/player/jump/Jump__005.png').convert_alpha()
        ]

        self.sliding_images = [
            pygame.image.load('./assets/player/slide/Slide__000.png').convert_alpha(),
            pygame.image.load('./assets/player/slide/Slide__001.png').convert_alpha(),
            pygame.image.load('./assets/player/slide/Slide__002.png').convert_alpha(),
            pygame.image.load('./assets/player/slide/Slide__003.png').convert_alpha(),
            pygame.image.load('./assets/player/slide/Slide__004.png').convert_alpha(),
            pygame.image.load('./assets/player/slide/Slide__005.png').convert_alpha(),
            pygame.image.load('./assets/player/slide/Slide__006.png').convert_alpha(),
            pygame.image.load('./assets/player/slide/Slide__007.png').convert_alpha(),
            pygame.image.load('./assets/player/slide/Slide__008.png').convert_alpha(),
            pygame.image.load('./assets/player/slide/Slide__009.png').convert_alpha()
        ]


        self.image = pygame.transform.scale(self.idle_images[0], [70,100])
        self.rect = pygame.Rect(
            self.gamedata['screen_width'] / 2,
            self.gamedata['screen_height']-128-105, #screen height - ground height - Player height
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

        

    def update(self, falling=False, wall_position=None):

        if self.last_wall == None:
            self.last_wall = wall_position
        elif self.last_wall == wall_position:
            self.xSpeed =0

        elif wall_position == None:
            self.last_wall = None


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
                self.xSpeed -= 1
            elif self.xSpeed < 0:
                self.xSpeed += 1
                self.image = pygame.transform.flip(self.image, True, False)

            if self.xSpeed == 0:
                print('a')
                self.sliding = 0

            return


        if key[pygame.K_d] and not self.sliding:
            self.last_button = 'd'

            if self.xSpeed < 0:
                self.xSpeed = 0

            if self.xSpeed < 10:
                self.xSpeed +=1
        elif key[pygame.K_a] and not self.sliding:
            self.last_button = 'a'

            if self.xSpeed > 0:
                self.xSpeed = 0
            if self.xSpeed > -10:
                self.xSpeed -= 1

        else:

            if self.xSpeed != 0 and not falling and not self.sliding:
                self.xSpeed = 0


        if key[pygame.K_SPACE]:
            if not falling and not self.attacking:
                self.jumping = True
                self.current_image = 0

        if key[pygame.K_f]:
            if not self.attacking and not falling and not self.sliding: 
                self.attacking = True
                self.current_image = 0
                self.xSpeed = 0
        elif key[pygame.K_s] and self.xSpeed != 0:
            if not self.attacking and not falling and not self.sliding:
                self.current_image = 0
                self.sliding = True
                if self.xSpeed > 0:
                    self.xSpeed = 20
                else:
                    self.xSpeed = -30
            



        if self.xSpeed == 0 and not falling:

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