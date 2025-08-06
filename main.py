from pygame.math import Vector2
import pygame 
from pygame.time import Clock
from pygame import MOUSEBUTTONDOWN, Surface

from command import MoveCommand
from unit import Unit

_ = pygame.init()
screen: Surface = pygame.display.set_mode((1280, 720))
clock: Clock = pygame.time.Clock()
running: bool = True
dt: float = 0

unit = Unit(pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == MOUSEBUTTONDOWN:
            pos: Vector2 = Vector2(pygame.mouse.get_pos())
            moveCommand = MoveCommand(pos)
            moveCommand.execute(unit)
            print(pos[0], pos[1])

    _ = screen.fill("purple")

    _ = pygame.draw.circle(screen, "red", unit.pos, 40)

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
