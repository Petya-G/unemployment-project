from tarfile import HeaderError
from pygame.math import Vector2
import pygame 
from pygame.time import Clock
from pygame import MOUSEBUTTONDOWN, Surface
import pygame_gui

from command import MoveCommand
from unit import Unit, UnitView

_ = pygame.init()
WIDTH = 1280
HEIGHT = 720
manager = pygame_gui.UIManager((WIDTH, HEIGHT))
screen: Surface = pygame.display.set_mode((WIDTH, HEIGHT))
clock: Clock = pygame.time.Clock()
running: bool = True
dt: float = 0

unit = Unit(pygame.Vector2(WIDTH / 2, HEIGHT / 2), ('Enemy armor company'))
unitView = UnitView(unit)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == MOUSEBUTTONDOWN:
            pos: Vector2 = Vector2(pygame.mouse.get_pos())
            moveCommand = MoveCommand(pos)
            moveCommand.execute(unit)
            print(pos[0], pos[1])

        manager.process_events(event)
    manager.update(dt)


    _ = screen.fill("purple")
    screen.blit(unitView.surface, unitView.getPos())

    manager.draw_ui(screen)
    pygame.display.update()

    dt = clock.tick(60) / 1000

pygame.quit()
