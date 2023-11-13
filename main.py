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
print('-------------------------------------------')

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
# charles = Fish(scr, 'green')
# ted = Fish(scr, 'orange')
num_fish = 3
fish_list = []
for ii in range(0, int(num_fish/2)):
    fish_list.append(Fish(scr, 'green'))
for ii in range(0, int(num_fish/2)):
    fish_list.append(Fish(scr, 'orange'))

mary = C_Fish(scr, 'puffer')

print('Running game ...')
running = True
while running:

    t1 = time.time()

    # Store pygame events in a variable.
    events = pygame.event.get()

    # Get events happening in window.
    for event in events:

        # User presses X in window.
        if event.type == pygame.QUIT:
            running = False

    # Draw background.
    scr.blit(background, (0, 0))

    # Update fish position.
    # charles.update_position(scr, events)
    # ted.update_position(scr, events)

    for fish in fish_list:
        fish.update_position(scr, events)

    mary.update_position(scr, events)

    # Check for collision.
    # mary.check_for_collisions([ted, charles])
    mary.check_for_collisions(fish_list)

    # Update the display
    pygame.display.flip()

    # Limit to 60 fps.
    clock.tick(60)

# End of game loop.
print('-------------------------------------------')
print('End of line.')

# Quit Pygame
pygame.quit()
sys.exit()
