import pygame
import sys
from chomp_utils import make_background, make_splash_screen, Fish

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
make_splash_screen(background, scr)

# Create one fish.
charles = Fish(scr, 'green')
ted = Fish(scr, 'orange')
ted.fish_x_spd = 0.1

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
