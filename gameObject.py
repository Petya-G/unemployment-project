from pygame import Vector2


class GameObject: 
    pos: Vector2
    def __init__(self, pos: Vector2) -> None:
        self.pos = pos
