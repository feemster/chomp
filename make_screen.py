import pygame
import time

# Initialize Pygame
pygame.init()

print('\nRunning make_screen.py.')
print('-------------------------------------------')


# Screen dimensions
scr_wid = 800  # (px)
scr_hgt = 600  # (px)

# Colors
blue = (0, 0, 255)
brown = (139, 69, 19)

# Rectangle 01 properties.
rec_01_hgt = 50
rec_01_wid = scr_wid
rec_01_pos_x = 0
rec_01_pos_y = scr_hgt - rec_01_hgt
rec_01 = pygame.Rect(0, scr_hgt - rec_01_hgt, scr_wid, rec_01_hgt)

# Create the screen
scr = pygame.display.set_mode((scr_wid, scr_hgt))
pygame.display.set_caption('Blue Background with Brown Rectangle')

# Main loop

# Create time epoch.
t0 = time.time()
t = 0

running = True
while running and (t < 2):

    # Update time.
    t = time.time() - t0

    # Get events happening in window.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with blue
    scr.fill(blue)

    if t > 1:
        rec_01.update(0, int(scr_hgt/2), rec_01_wid, rec_01_hgt)
    print(rec_01)

    # Draw the brown rectangle at the bottom of the screen.
    pygame.draw.rect(scr, brown, rec_01)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()

print('\n-------------------------------------------')
print('End of line.')
