import pygame
import sys
from chomp_utils import make_background, make_splash_screen, Fish, C_Fish
import time

# Initialize Pygame
pygame.init()

# Create Pygame clock.
clock = pygame.time.Clock()

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
mary = C_Fish(scr, 'puffer')

print('Running game ...')
running = True
while running:

    t1 = time.time()

    # Get events happening in window.
    for event in pygame.event.get():

        # See if user presses a key.
        if event.type == pygame.KEYDOWN:
            print(f'User is presed {event.key}.')

        if event.type == pygame.KEYUP:
            print(f'User is released {event.key}.')

        # User presses X in window.
        if event.type == pygame.QUIT:
            running = False

    # Draw background.
    scr.blit(background, (0, 0))

    # Update fish position.
    charles.update_position(scr)
    ted.update_position(scr)
    mary.update_position(scr)

    # Update the display
    pygame.display.flip()

    # Limit to 60 fps.
    clock.tick(60)

    t2 = time.time()
    print(f'loop rate = {1/(t2-t1):.1f} s. Expected loop rate = 60 hz.')

# End of game loop.
print('\n-------------------------------------------')
print('End of line.')

# Quit Pygame
pygame.quit()
sys.exit()
