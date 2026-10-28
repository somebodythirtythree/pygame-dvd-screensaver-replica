import pygame as pg
from pygame.locals import *
from random import choice, randint
WIDTH = 1280
HEIGHT = 720
FPS = 120
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("DVD Screensaver")
clock = pg.time.Clock()
colors = [pg.Color("red"), pg.Color("green"), pg.Color("blue"), pg.Color("yellow"), pg.Color("magenta")]

class DVDScreensaverBox:
    """The DVD screensaver box class"""
    def __init__(self):
        self.width = 200
        self.height = 100
        self.dx = 2
        self.dy = 1
        self.rect = Rect(randint(300, 900), randint(200, 600), self.width, self.height)  # The hitbox
        self.x = self.rect.x
        self.y = self.rect.y
        self.color = pg.Color("white")

    def draw(self):
        pg.draw.rect(screen, self.color, self.rect)

    def update(self):
        self.x += self.dx
        self.y += self.dy
        self.rect.x = self.x
        self.rect.y = self.y
        if self.rect.right >= WIDTH or self.rect.left <= 0:
            self.dx = -self.dx
            self.color = choice(colors)
        elif self.rect.bottom >= HEIGHT or self.rect.top <= 0:
            self.dy = -self.dy
            self.color = choice(colors)

def main():
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


if __name__ == "__main__":
    main()
