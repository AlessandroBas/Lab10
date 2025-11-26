from dataclasses import dataclass

@dataclass
class Archi:
    h1: int
    h2: int
    valore_totale: float
    n_spedizioni: int

    def __str__(self):
        return f'{self.h1} {self.h2} {self.valore_totale}'

    def __repr__(self):
        return f'{self.h1} {self.h2} {self.valore_totale}'

    def get_valore_medio(self):
        return self.valore_totale / self.n_spedizioni if self.n_spedizioni > 0 else 0