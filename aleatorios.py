"""
Nom i cognoms: Martí Fontseca
Tarea 4: Generació de números aleatoris
"""

class Aleat:
    """
    Classe per generar números aleatoris amb l'algoritme LGC.
    
    >>> rand = Aleat(m=32, a=9, c=13, x0=11)
    >>> for _ in range(4):
    ...     print(next(rand))
    16
    29
    18
    15
    >>> rand(29)
    >>> for _ in range(4):
    ...     print(next(rand))
    18
    15
    20
    1
    """
    def __init__(self, *, m=2**48, a=25214903917, c=11, x0=1212121):
        self.m = m
        self.a = a
        self.c = c
        self.x = x0

    def __iter__(self):
        return self

    def __next__(self):
        # Apliquem la fórmula: (a * x + c) % m
        self.x = (self.a * self.x + self.c) % self.m
        return self.x

    def __call__(self, x_nou):
        # Reinicia la semilla
        self.x = x_nou


def aleat(*, m=2**48, a=25214903917, c=11, x0=1212121):
    """
    Funció generadora que fa el mateix que la classe.
    
    >>> rand = aleat(m=64, a=5, c=46, x0=36)
    >>> for _ in range(4):
    ...     print(next(rand))
    34
    24
    38
    44
    >>> rand.send(24)
    38
    >>> for _ in range(4):
    ...     print(next(rand))
    44
    10
    32
    14
    """
    x = x0
    while True:
        x = (a * x + c) % m
        # Si fem .send(valor), s'assigna a 'enviat'
        enviat = yield x
        if enviat is not None:
            x = enviat

if __name__ == "__main__":
    import doctest
    doctest.testmod()
