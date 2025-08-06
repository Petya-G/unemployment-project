from pygame import Vector2

class Unit: 
    pos: Vector2
    def __init__(self, pos: Vector2) -> None:
        self.pos = pos
        
    def move(self, new_pos: Vector2) -> None:
        self.pos = new_pos
