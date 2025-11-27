from dataclasses import dataclass

@dataclass
class Archi:
    h1: int
    h2: int
    valore_medio: float

    def __str__(self):
        return f'{self.h1} {self.h2} {self.valore_medio}'

    def __repr__(self):
        return f'{self.h1} {self.h2} {self.valore_medio}'

    def __eq__(self, other):
        return isinstance(other, Archi) and self.h1 == other.h1 and self.h2 == other.h2