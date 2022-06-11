import pygame, consts, sprites, os

class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((consts.WIDTH, consts.HEIGHT))
        pygame.display.set_caption(consts.GAME_TITLE)
        self.clock = pygame.time.Clock()
        self.isRunning = True
        self.font = pygame.font.match_font(consts.FONT)
        self.loading_files()
        
    def New_game(self):
        self.all_sprites = pygame.sprite.Group()
        self.running()
    
    def running(self):
        self.playing = True
        while self.playing:
            self.clock.tick(consts.FPS)
            self.events()
            self.upgrade_sprites()
            self.draw_sprites()
        
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.isRunning = False
                
    def upgrade_sprites(self):
        self.all_sprites.update()
        
    def draw_sprites(self):
        self.screen.fill(consts.BLACK)
        self.all_sprites.draw(self.screen)
        pygame.display.flip()
    
    def loading_files(self):
        directory_images = os.path.join(os.getcwd(), 'images')
        self.directory_sounds = os.path.join(os.getcwd(), 'sounds')
        self.spritesheet = os.path.join(directory_images, consts.SPRITESHEET)
        self.pacman_start_logo = os.path.join(directory_images, consts.PACMAN_START_LOGO)
        self.pacman_start_logo = pygame.image.load(self.pacman_start_logo).convert()
        
    def show_text(self, text, length, color, x, y):
        font = pygame.font.Font(self.font, length)
        text = font.render(text, True, color)
        text_rect = text.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text, text_rect)
        
    def show_start_logo(self,x,y):
        start_logo_rect = self.pacman_start_logo.get_rect()
        start_logo_rect.midtop = (x, y)
        self.screen.blit(self.pacman_start_logo, start_logo_rect)

    
    def show_screen_start(self):
        pygame.mixer.music.load(os.path.join(self.directory_sounds, consts.MUSIC_START))
        pygame.mixer.music.play()
        
        
        self.show_start_logo(consts.WIDTH / 2, 20)
        
        self.show_text(
            '- Pressione uma tecla para jogar', 
            32, 
            consts.YELLOW,
            consts.WIDTH / 2,
            320
            )
        self.show_text(
            'Create by Tiago S.C., Bruno E. , Max H.T.', 
            19, 
            consts.WHITE,
            consts.WIDTH / 2,
            570
            )
        
        pygame.display.flip()
        self.wait_player()
        
    def wait_player(self):
        wait = True
        while wait:
            self.clock.tick(consts.FPS)
            for event in pygame.event.get():
                if event.type ==  pygame.QUIT:
                    self.isRunning = False
                if event.type == pygame.KEYUP:
                        wait = False
                        pygame.mixer.music.stop()
                        pygame.mixer.Sound(os.path.join(self.directory_sounds, consts.KEY_START)).play()
    
    def show_screen_game_over(self):
        pass
    
g = Game()
g.show_screen_start()

while g.isRunning:
    g.New_game()
    g.show_screen_game_over()
            