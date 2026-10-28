import pygame as pg
from pygame.locals import *
from random import choice, randint
import sys
WIDTH = 1280
HEIGHT = 720
FPS = 120
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("DVD Screensaver")
clock = pg.time.Clock()
colors = [(randint(0, 255), randint(0, 255), randint(0, 255)) for _ in range(15)]

class DVDScreensaverBox:
    """The DVD screensaver box class"""
    def __init__(self):
        self.dx = 2
        self.dy = 1
        self.img = pg.image.load("assets/dvd.png").convert_alpha()
        self.rect = self.img.get_rect()
        self.rect.x = randint(self.rect.width + 10, WIDTH - self.rect.width - 10)
        self.rect.y = randint(self.rect.height + 10, HEIGHT - self.rect.height - 10)
        self.x = self.rect.x
        self.y = self.rect.y
        self.color = pg.Color("white")

    def draw(self):
        screen.blit(self.img, self.rect)

    def change_color(self, color):
        new_surface = self.img.copy()
        new_surface.fill((0, 0, 0, 255), special_flags=pg.BLEND_RGBA_MULT)
        new_surface.fill(color + (0,), special_flags=pg.BLEND_RGBA_ADD)
        return new_surface

    def update(self):
        self.x += self.dx
        self.y += self.dy
        self.rect.x = self.x
        self.rect.y = self.y
        if self.rect.right >= WIDTH or self.rect.left <= 0:
            self.dx = -self.dx
            self.img = self.change_color(choice(colors))
        elif self.rect.bottom >= HEIGHT or self.rect.top <= 0:
            self.dy = -self.dy
            self.img = self.change_color(choice(colors))

        if self.rect.topleft == (0, 0) or self.rect.topright == (WIDTH, 0) \
                or self.rect.bottomleft == (0, HEIGHT) or self.rect.bottomright == (WIDTH, HEIGHT):
            self.dx = -self.dx
            self.dy = -self.dy
            self.img = self.change_color(choice(colors))
            print("Corner hit")
            pg.mixer.music.load("assets/wow.mp3")
            pg.mixer.music.play()


def main():
    pg.init()
    pg.mixer.init()
    running = True
    box = DVDScreensaverBox()
    while running:
        pg.display.update()
        screen.fill((0, 0, 0))
        box.draw()
        box.update()
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == QUIT:
                running = False
    pg.quit()
    sys.exit()

if __name__ == "__main__":
    main()
