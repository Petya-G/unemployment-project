from pygame.rect import Rect


import io
import pygame
from pygame import Vector2, Surface
import military_symbol 

class Unit: 
    pos: Vector2
    description: str

    def __init__(self, pos: Vector2, description: str) -> None:
        self.pos = pos
        self.description = description
        
    def move(self, new_pos: Vector2) -> None:
        self.pos = new_pos

class UnitView:
    unit: Unit
    surface: Surface

    def _getSurface(self) -> Surface:
        print(self.unit.description)
        svg: str = military_symbol.get_symbol_svg_string_from_name(self.unit.description)
        return pygame.image.load(io.BytesIO(svg.encode()))

    def __init__(self, unit: Unit) -> None:
        self.unit = unit
        self.surface = self._getSurface()
    
    def getPos(self) -> Vector2:
        rect: Rect = self.surface.get_rect()
        return self.unit.pos - Vector2(rect.width / 2, rect.height / 2)
