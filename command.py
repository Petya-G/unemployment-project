from abc import ABC, abstractmethod
from typing_extensions import override

from pygame import Vector2

from unit import Unit

class Command(ABC):
    @abstractmethod
    def execute(self, gameObject: Unit) -> None:
        ...

class MoveCommand(Command):
    pos: Vector2

    def __init__(self, pos: Vector2) -> None:
        self.pos = pos

    @override
    def execute(self, gameObject: Unit) -> None:  
        gameObject.move(self.pos)
