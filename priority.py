from enum import Enum


class Priority(Enum):
    Niski = 1
    Sredni = 2
    Wysoki = 3

    def __str__(self):
        return str(self.name)
