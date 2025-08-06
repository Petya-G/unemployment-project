# Example file showing a circle moving on screen
from pygame.math import Vector2
import pygame 
from pygame.time import Clock
from pygame import MOUSEBUTTONDOWN, Surface

# pygame setup
_ = pygame.init()
screen: Surface = pygame.display.set_mode((1280, 720))
clock: Clock = pygame.time.Clock()
running: bool = True
dt: float = 0

player_pos: Vector2 = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == MOUSEBUTTONDOWN:
            pos: Vector2 = Vector2(pygame.mouse.get_pos())
            print(pos[0], pos[1])
            player_pos= pos

    # fill the screen with a color to wipe away anything from last frame
    _ = screen.fill("purple")

    _ = pygame.draw.circle(screen, "red", player_pos, 40)

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
