import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Clear terminal output.
for ii in range(0, 10):
    print()

print('\nRunning make_background.py.')
print('-------------------------------------------\n')

# Specify screen dimensions.
scr_wid = 800  # (px)
scr_hgt = 600  # (px)

# Create the screen.
scr = pygame.display.set_mode((scr_wid, scr_hgt))
pygame.display.set_caption('Making a customized background')


# ------------------------------------------------------------------------
def make_background(surface):
    # Load the images.
    water = pygame.image.load("assets/sprites/water.png").convert()
    sand = pygame.image.load("assets/sprites/sand.png").convert()
    sand_top = pygame.image.load("assets/sprites/sand_top.png").convert()
    seagrass = pygame.image.load("assets/sprites/seagrass.png").convert()

    # Makes black pixels transparent.
    sand_top.set_colorkey((0, 0, 0))
    seagrass.set_colorkey((0, 0, 0))

    # Cover screen with water.
    for x in range(0, surface.get_width(), water.get_width()):
        for y in range(0, surface.get_height(), water.get_height()):
            surface.blit(water, (x, y))

    # Draw base sand at bottom of screen.
    for x in range(0, surface.get_width(), sand.get_width()):
        surface.blit(sand, (x, surface.get_height() - sand.get_height()))

    # Draw top sand (has divots) on top of base sand.
    for x in range(0, surface.get_width(), sand_top.get_width()):
        surface.blit(sand_top, (x, surface.get_height() - sand.get_height() - sand_top.get_height()))

    # Draw seagrass.
    for _ in range(0, 5):
        x = random.randint(0, surface.get_width() - seagrass.get_width())
        surface.blit(seagrass, (x, surface.get_height() - sand.get_height() - sand_top.get_height()
                                - seagrass.get_height() + 5))

# ------------------------------------------------------------------------


background = scr.copy()
make_background(background)

running = True
while running:

    # Get events happening in window.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    scr.blit(background, (0, 0))

    # Update the display
    pygame.display.flip()

# End of game loop.
print('\n-------------------------------------------')
print('End of line.')

# Quit Pygame
pygame.quit()
sys.exit()
