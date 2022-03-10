import random
import os
import time
import pygame

pygame.font.init()

screenwidth = 1500
screenheight = 750

screen = pygame.display.set_mode([screenwidth, screenheight])
pygame.display.set_caption("Space Wars")

icon = pygame.image.load(os.path.join(r"C:\Users\Chaitanya\Documents\Python Scripts\Pygame\Space Wars\Assets\Images","icon.png"))
pygame.display.set_icon(icon)


#load Images
#enemy ship
enemy_1 = pygame.image.load(os.path.join(r"C:\Users\Chaitanya\Documents\Python Scripts\Pygame\Space Wars\Assets\Images","enemy_1.png"))
enemy_2 = pygame.image.load(os.path.join(r"C:\Users\Chaitanya\Documents\Python Scripts\Pygame\Space Wars\Assets\Images","enemy_2.png"))
enemy_3 = pygame.image.load(os.path.join(r"C:\Users\Chaitanya\Documents\Python Scripts\Pygame\Space Wars\Assets\Images","enemy_3.png"))
enemy_4 = pygame.image.load(os.path.join(r"C:\Users\Chaitanya\Documents\Python Scripts\Pygame\Space Wars\Assets\Images","enemy_4.png"))
enemy_5 = pygame.image.load(os.path.join(r"C:\Users\Chaitanya\Documents\Python Scripts\Pygame\Space Wars\Assets\Images","enemy_5.png"))

#enemy lasers
laser_1 = pygame.image.load(os.path.join(r"C:\Users\Chaitanya\Documents\Python Scripts\Pygame\Space Wars\Assets\Images","laser_1.png"))
laser_2 = pygame.image.load(os.path.join(r"C:\Users\Chaitanya\Documents\Python Scripts\Pygame\Space Wars\Assets\Images","laser_2.png"))
laser_3 = pygame.image.load(os.path.join(r"C:\Users\Chaitanya\Documents\Python Scripts\Pygame\Space Wars\Assets\Images","laser_3.png"))
laser_4 = pygame.image.load(os.path.join(r"C:\Users\Chaitanya\Documents\Python Scripts\Pygame\Space Wars\Assets\Images","laser_4.png"))
laser_5 = pygame.image.load(os.path.join(r"C:\Users\Chaitanya\Documents\Python Scripts\Pygame\Space Wars\Assets\Images","laser_5.png"))

#Player laser
player_laser = pygame.image.load(os.path.join(r"C:\Users\Chaitanya\Documents\Python Scripts\Pygame\Space Wars\Assets\Images","laser_myship.png"))

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

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()



class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = player_ship
        self.laser_img = player_laser
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health

class Enemy(Ship):
    ENEMY_MAP = {
        "enemy1":(enemy_1, laser_1),
        "enemy2":(enemy_2, laser_2),
        "enemy3":(enemy_3, laser_3),
        "enemy4":(enemy_4, laser_4),
        "enemy5":(enemy_5, laser_5)
    }

    def __init__(self, x, y, enemy, health=100):
        super().__init__(x, y, health)
        self.ship_img, self.laser_img = self.ENEMY_MAP[enemy]
        self.mask = pygame.mask.from_surface(self.ship_img)

    def move(self, vel):
        self.y += vel


def main():
    run = True
    FPS = 60
    score = 0
    level = 0
    lives = 6
    main_font = pygame.font.SysFont("comicsans", 50)
    lost_font = pygame.font.SysFont("comicsans", 70)

    enemies = []
    wave_length = 5
    enemy_vel = 1

    player_vel = 5

    player = Player(screenwidth/2 - player_ship.get_width()/2, 500)

    clock = pygame.time.Clock()

    lost = False
    lost_count = 0

    def redraw_window():
        screen.blit(game_bg, (0,0))

        #draw text
        score_label = main_font.render(f"Score : {score}", 1, (0,255,0))
        lives_label = main_font.render(f"Lives : {lives}", 1, (255,255,255))

        screen.blit(score_label, (15, 10))
        screen.blit(lives_label, (screenwidth - lives_label.get_width() - 15, 10))

        for enemy in enemies:
            enemy.draw(screen)

        player.draw(screen)

        if lost:
            lost_label = lost_font.render("You Lost!!!!", 1, (255,255,255))
            screen.blit(lost_label, (screenwidth/2 - lost_label.get_width()/2, screenheight/2))


        pygame.display.update()


    while run:
        clock.tick(FPS)

        redraw_window()

        if lives <= 0 or player.health <=0:
            lost =  True
            lost_count += 1

        if lost:
            if lost_count > FPS * 5 :
                run = False
            else:
                continue


        if len(enemies) == 0:
            level += 1
            wave_length += 5
            for i in range(wave_length):
                enemy = Enemy(random.randrange(50, screenwidth-100), random.randrange(-1500, -100), random.choice(["enemy1", "enemy2", "enemy3", "enemy4", "enemy5" ]))
                enemies.append(enemy)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - player_vel > 0 : #left
            player.x -= player_vel
        if keys[pygame.K_RIGHT] and player.x + player_vel + player.get_width() < screenwidth: #right
            player.x += player_vel
        if keys[pygame.K_UP] and player.y - player_vel > 0 : #up
            player.y -= player_vel
        if keys[pygame.K_DOWN] and player.y + player_vel + player.get_height() < screenheight: #down
            player.y += player_vel

        for enemy in enemies[:]:
            enemy.move(enemy_vel)
            if enemy.y + enemy.get_height() > screenheight:
                lives -= 1
                enemies.remove(enemy)

        
        redraw_window()

main()



