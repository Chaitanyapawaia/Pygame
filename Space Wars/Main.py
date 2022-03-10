import random
import os
import time
import pygame

pygame.font.init()

screenwidth = 1500
screenheight = 800
screen = pygame.display.set_mode([screenwidth, screenheight])
pygame.display.set_caption("Space Wars")


#load Images
#enemy ship
enemy_1 = pygame.image.load(os.path.join(r"C:\Users\Chaitanya\Documents\Python Scripts\Pygame\Space Wars\Assets\Images","enemy_1.png"))
enemy_2 = pygame.image.load(os.path.join(r"C:\Users\Chaitanya\Documents\Python Scripts\Pygame\Space Wars\Assets\Images","enemy_2.png"))
enemy_3 = pygame.image.load(os.path.join(r"C:\Users\Chaitanya\Documents\Python Scripts\Pygame\Space Wars\Assets\Images","enemy_3.png"))

#bullet
enemy_bullet = pygame.image.load(os.path.join(r"C:\Users\Chaitanya\Documents\Python Scripts\Pygame\Space Wars\Assets\Images","enemy_bullet.png"))
power_bullet = pygame.image.load(os.path.join(r"C:\Users\Chaitanya\Documents\Python Scripts\Pygame\Space Wars\Assets\Images","power_bullet.png"))
bullet = pygame.image.load(os.path.join(r"C:\Users\Chaitanya\Documents\Python Scripts\Pygame\Space Wars\Assets\Images","bullet.png"))

#Player ship
player_ship = pygame.image.load(os.path.join(r"C:\Users\Chaitanya\Documents\Python Scripts\Pygame\Space Wars\Assets\Images","myship.png"))

#bg
game_bg = pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\Chaitanya\Documents\Python Scripts\Pygame\Space Wars\Assets\Images","game_bg.png")), (screenwidth,screenheight))

#miscellaneous
game_over = pygame.image.load(os.path.join(r"C:\Users\Chaitanya\Documents\Python Scripts\Pygame\Space Wars\Assets\Images","game_over.png"))

class Ship:
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.bullet_img = None
        self.lasers = []
        self.cool_down_counter = 0

    def draw(self, window):
        screen.blit(self.ship_img, (self.x, self.y))

class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(self, x, y, health)
        self.ship_img = player_ship
        self.bullet_img = bullet
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health

def main():
    run = True
    FPS = 60
    score = 0
    lives = 6
    main_font = pygame.font.SysFont("comicsans", 50)
    player_vel = 5

    player = Player(300, 650)

    clock = pygame.time.Clock()

    def redraw_window():
        screen.blit(game_bg, (0,0))

        #draw text
        score_label = main_font.render(f"Score : {score}", 1, (0,255,0))
        lives_label = main_font.render(f"Lives : {lives}", 1, (255,255,255))

        screen.blit(score_label, (15, 10))
        screen.blit(lives_label, (screenwidth - lives_label.get_width() - 15, 10))

        player.draw(screen)

        pygame.display.update()



    while run:
        clock.tick(FPS)
        redraw_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and Player.x - player_vel > 0 : #left
            Player.x -= player_vel
        if keys[pygame.K_RIGHT] and Player.x + player_vel + 50 < screenwidth: #right
            Player.x += player_vel
        

main()



