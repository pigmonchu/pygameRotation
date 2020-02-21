import pygame as pg
from pygame.locals import *
import sys, os 

BLANCO = (250,250,250)
FPS = 60

class Corredor(pg.sprite.Sprite):
    velocidad = 5
    def __init__(self, x, y):
        self.w = 240
        self.h = 296
        
        pg.sprite.Sprite.__init__(self)

        self.image = pg.Surface((self.w, self.h), pg.SRCALPHA, 32)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # Almacenar los frames
        self.frames = []
        self.index = 0
        self.how_many = 0
        self.animation_time = FPS//2

        self.loadFrames()
        self.current_time = 0

    def loadFrames(self):
        sprite_sheet = pg.image.load('corredor.png').convert_alpha()
        for fila in range(5):
            y = fila * self.h
            for columna in range(6):
                x = columna * self.w

                image = pg.Surface((self.w, self.h), pg.SRCALPHA).convert_alpha()
                image.blit(sprite_sheet, (0,0), (x, y, self.w, self.h))

                self.frames.append(image)

        self.how_many = len(self.frames)
        self.image = self.frames[self.index]

    def update(self, dt):
        self.current_time += dt

        if self.current_time > self.animation_time:
            self.current_time = 0
            self.index += 1

            if self.index >= self.how_many:
                self.index = 0

            self.image = self.frames[self.index]

            self.rect.x += self.velocidad
            if self.rect.x > 800:
                self.rect.x = -240
                self.velocidad += 5


class Game():
    clock = pg.time.Clock()

    def __init__(self, width, height):
        self.display = pg.display
        self.screen = self.display.set_mode((width, height))
        self.display.set_caption('Corredor')
        self.w = width
        self.h = height

        corredor = Corredor(400, 300)
        self.allSprites = pg.sprite.Group()
        self.allSprites.add(corredor)

    def handleevent(self):
        for event in pg.event.get():
            if event == QUIT or event.type == KEYDOWN and event.key == K_q:
                return True
        
        return False

    def render(self, dt):
        self.screen.fill(BLANCO)

        self.allSprites.update(dt)
        self.allSprites.draw(self.screen)

        self.display.flip()

    def mainloop(self):
        game_over = False

        while game_over == False:
            dt = self.clock.tick(FPS)

            game_over = self.handleevent()

            self.render(dt)

        self.game_over()

    def game_over(self):
        pg.quit()
        sys.exit()

if __name__ == '__main__':
    pg.init()
    game = Game(800, 600)
    game.mainloop()
