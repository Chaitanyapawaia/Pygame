import random
import os
import time
import pygame

screenwidth = 1200
screenheight = 750
screen = pygame.display.set_mode([screenwidth, screenheight])
pygame.display.set_caption("Space Wars")


#load Images
#enemy
enemy_1 = pygame.image.load(os.path.join(r"C:\Users\Chaitanya\Documents\Python Scripts\Pygame\Space Wars\Assets\Images","enemy_1.png"))
enemy_2 = pygame.image.load(os.path.join(r"C:\Users\Chaitanya\Documents\Python Scripts\Pygame\Space Wars\Assets\Images","enemy_2.png"))
enemy_3 = pygame.image.load(os.path.join(r"C:\Users\Chaitanya\Documents\Python Scripts\Pygame\Space Wars\Assets\Images","enemy_3.png"))

#bullet
enemy_bullet = pygame.image.load(os.path.join(r"C:\Users\Chaitanya\Documents\Python Scripts\Pygame\Space Wars\Assets\Images","enemy_bullet.png"))
power_bullet = pygame.image.load(os.path.join(r"C:\Users\Chaitanya\Documents\Python Scripts\Pygame\Space Wars\Assets\Images","power_bullet.png"))
bullet = pygame.image.load(os.path.join(r"C:\Users\Chaitanya\Documents\Python Scripts\Pygame\Space Wars\Assets\Images","bullet.png"))

#our ship
myship =pygame.image.load(os.path.join(r"C:\Users\Chaitanya\Documents\Python Scripts\Pygame\Space Wars\Assets\Images","myship.png"))

#bg
game_bg = pygame.image.load(os.path.join(r"C:\Users\Chaitanya\Documents\Python Scripts\Pygame\Space Wars\Assets\Images","game_bg.png"))

#miscellaneous
game_over = pygame.image.load(os.path.join(r"C:\Users\Chaitanya\Documents\Python Scripts\Pygame\Space Wars\Assets\Images","game_over.png"))


def main():
    run = True
    FPS = 60
    clock = pygame.time.Clock()

    def redraw_window():
        pygame.display.update()

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


main()




'''
pygame.init()




# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()

'''