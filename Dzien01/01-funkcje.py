import math
# Funkcje

def test():
    #return
    pass


def oblicz_pole_kola(r: float) -> float:
    if not type(r) is [int, float]:
        raise TypeError("Zły format danej")
    # return 3.14 * (r ** 2)
    return math.pi * (r ** 2)

print(oblicz_pole_kola(10))