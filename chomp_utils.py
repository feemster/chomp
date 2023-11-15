import pygame
import time
import random


class Fish:
    def __init__(self, screen, color):

        # Fishy attributes.
        fname = f'assets/sprites/{color}_fish.png'

        self.fish_img_right = pygame.image.load(fname).convert()
        self.fish_img_right.set_colorkey((0, 0, 0))
        self.fish_img_left = pygame.transform.flip(self.fish_img_right, True, False)

        self.fish_img = self.fish_img_right
        # self.fish_img.set_colorkey((0, 0, 0))

        self.fish_x = random.randint(0, screen.get_width()-self.fish_img.get_width())
        self.fish_x_dir = 1
        self.fish_x_spd = screen.get_width()/(2*60)

        sand = pygame.image.load('assets/sprites/sand.png').convert()
        sand_top = pygame.image.load('assets/sprites/sand_top.png').convert()
        seagrass = pygame.image.load('assets/sprites/seagrass.png').convert()

        self.y_bnd = screen.get_height() - sand.get_height() - sand_top.get_height() - seagrass.get_height() - 5
        self.fish_y = random.randint(0, self.y_bnd)
        self.fish_y_dir = 1
        self.fish_y_spd = self.y_bnd/(2*60)

        # Sounds.
        self.chomp = pygame.mixer.Sound('assets/sounds/chomp.wav')

    def update_position(self, screen, events):

        self.fish_x += self.fish_x_spd*self.fish_x_dir
        self.fish_y += self.fish_y_spd*self.fish_y_dir

        # Check the position of the self.fish.
        if self.fish_x >= screen.get_width() - self.fish_img.get_width():
            self.fish_x_dir = -1
            # self.fish_img = pygame.transform.flip(self.fish_img, True, False)
            self.fish_img = self.fish_img_left

        if self.fish_x < 0:
            self.fish_x_dir = 1
            # self.fish_img = pygame.transform.flip(self.fish_img, True, False)
            self.fish_img = self.fish_img_right

        if self.fish_y >= self.y_bnd:
            self.fish_y_dir = -1

        if self.fish_y < 0:
            self.fish_y_dir = 1

        # Draw the self.fish.
        screen.blit(self.fish_img, (self.fish_x, self.fish_y))

    def check_for_collisions(self, other_fish_list):

        # Check to see if I collide with any of the fish provided in the list.
        other_fish_rect_list = []
        for fish in other_fish_list:
            other_fish_rect_list.append(pygame.Rect(fish.fish_x, fish.fish_y, int(fish.fish_img.get_width()),
                                                    int(fish.fish_img.get_height())))

        my_rect = pygame.Rect(self.fish_x, self.fish_y, int(self.fish_img.get_width()),
                              int(self.fish_img.get_height()))

        # Check me against all the list of fish of rectangles.
        indices = my_rect.collidelistall(other_fish_rect_list)

        # Order the result from biggest index to smallest index.
        indices.sort(reverse=True)

        # Remove collided fish.
        for idx in indices:
            other_fish_list.pop(idx)
            pygame.mixer.Sound.play(self.chomp)


class C_Fish(Fish):
    def __init__(self, screen, color):

        # Initalize parent class.
        super().__init__(screen, color)

        # Keys
        self.key_up = 'not pressed'
        self.key_down = 'not pressed'
        self.key_left = 'not pressed'
        self.key_right = 'not pressed'

    def update_position(self, screen, events):

        # Update position based on keystrokes.
        for event in events:
            # See if user presses a key.
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.key_up = 'pressed'

                if event.key == pygame.K_DOWN:
                    self.key_down = 'pressed'

                if event.key == pygame.K_LEFT:
                    self.key_left = 'pressed'

                if event.key == pygame.K_RIGHT:
                    self.key_right = 'pressed'

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.key_up = 'not pressed'

                if event.key == pygame.K_DOWN:
                    self.key_down = 'not pressed'

                if event.key == pygame.K_LEFT:
                    self.key_left = 'not pressed'

                if event.key == pygame.K_RIGHT:
                    self.key_right = 'not pressed'

        # Update my fish based on status of my keys.
        if self.key_up == 'pressed':
            self.fish_y -= self.fish_y_spd

        if self.key_down == 'pressed':
            self.fish_y += self.fish_y_spd

        # Make right facing fish.
        if self.key_left == 'pressed':
            self.fish_x -= self.fish_x_spd
            self.fish_img = self.fish_img_left

        # Make left facing fish.
        if self.key_right == 'pressed':
            self.fish_img = self.fish_img_right
            self.fish_x += self.fish_x_spd

        # Check the position of the self.fish.
        if self.fish_x >= screen.get_width() - self.fish_img.get_width():
            self.fish_x = screen.get_width() - self.fish_img.get_width()

        if self.fish_x < 0:
            self.fish_x = 0

        if self.fish_y >= self.y_bnd:
            self.fish_y = self.y_bnd

        if self.fish_y < 0:
            self.fish_y = 0

        # Draw the self.fish.
        screen.blit(self.fish_img, (self.fish_x, self.fish_y))


def make_background(surface):
    # Load the images.
    water = pygame.image.load('assets/sprites/water.png').convert()
    sand = pygame.image.load('assets/sprites/sand.png').convert()
    sand_top = pygame.image.load('assets/sprites/sand_top.png').convert()
    seagrass = pygame.image.load('assets/sprites/seagrass.png').convert()

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


def make_splash_screen(background, scr):
    custom_font = pygame.font.Font('assets/fonts/Black_Crayon.ttf', 128)
    text = custom_font.render('Chomp', False, (255, 69, 0))
    scr.blit(background, (0, 0))
    scr.blit(text, (scr.get_width() / 2 - text.get_width() / 2, scr.get_height() / 2 - text.get_height() / 2 - 100))
    # Update the display (show to player).
    pygame.display.flip()

    print('Chomp splash screen.')
    time.sleep(5)
