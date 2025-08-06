from abc import ABC, abstractmethod

from pygame import Vector2

from gameObject import GameObject


class Command(ABC):
    @abstractmethod
    def execute(self, gameObject: GameObject) -> None:
        ...
    def undo(self, gameObject: GameObject) -> None:
        ...

class MoveCommand(Command):
    def __init__(self, gameObject: GameObject, pos: Vector2) -> None:

    def execute(self, gameObject: GameObject) -> None:
        Move