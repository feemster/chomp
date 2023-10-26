import pygame
import sys
import time
from chomp_utils import make_background, make_splash_screen
import random


class Fish:
    def __init__(self, screen, color):

        # Fishy attributes.
        fname = f'assets/sprites/{color}_fish.png'
        self.fish_img = pygame.image.load(fname).convert()
        self.fish_img.set_colorkey((0, 0, 0))

        self.fish_x = random.randint(0, screen.get_width()-self.fish_img.get_width())
        self.fish_x_dir = 1
        self.fish_x_spd = 0.1

        self.fish_y = random.randint(0, 4*self.fish_img.get_height())
        self.fish_y_dir = 1
        self.fish_y_spd = 0

    def update_position(self, screen):

        self.fish_x += self.fish_x_spd*self.fish_x_dir
        self.fish_y += self.fish_y_spd*self.fish_y_dir

        # Check the position of the self.fish.
        if self.fish_x >= screen.get_width() - self.fish_img.get_width():
            self.fish_x_dir = -1
            self.fish_img = pygame.transform.flip(self.fish_img, True, False)

        if self.fish_x < 0:
            self.fish_x_dir = 1
            self.fish_img = pygame.transform.flip(self.fish_img, True, False)

        # Draw the self.fish.
        screen.blit(self.fish_img, (self.fish_x, self.fish_y))


# Initialize Pygame
pygame.init()

# Clear terminal output.
for ii in range(0, 10):
    print()

print('\nRunning main.py.')
print('-------------------------------------------\n')

# Specify screen dimensions.
scr_wid = 800  # (px)
scr_hgt = 600  # (px)

# Create the screen.
scr = pygame.display.set_mode((scr_wid, scr_hgt))
pygame.display.set_caption('CHOMP game')

# Make static background.
background = scr.copy()
make_background(background)

# Show splash screen.
# make_splash_screen(background, scr)

# Create one fish.
charles = Fish(scr, 'green')
ted = Fish(scr, 'orange')
ted.fish_x_spd = 0.5

print('RUNNING GAME ...')
running = True
while running:

    # Get events happening in window.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw background.
    scr.blit(background, (0, 0))

    # Update fish position.
    charles.update_position(scr)
    ted.update_position(scr)

    # Update the display
    pygame.display.flip()

# End of game loop.
print('\n-------------------------------------------')
print('End of line.')

# Quit Pygame
pygame.quit()
sys.exit()
