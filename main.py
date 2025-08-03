# Example file showing a circle moving on screen
import pygame 
from pygame.key import ScancodeWrapper
from pygame.math import Vector2
from pygame.time import Clock
from pygame import Surface

# pygame setup
_ = pygame.init()
screen: Surface = pygame.display.set_mode((1280, 720))
clock: Clock = pygame.time.Clock()
running = True
dt = 0

player_pos: Vector2 = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    _ = screen.fill("purple")

    _ = pygame.draw.circle(screen, "red", player_pos, 40)

    keys: ScancodeWrapper = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt: float = clock.tick(60) / 1000

pygame.quit()