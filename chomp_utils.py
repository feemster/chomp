import pygame
import random


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
