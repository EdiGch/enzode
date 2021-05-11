import math
# Funkcje

def test():
    #return
    pass

# type hint dla parametrów funkcji
def oblicz_pole_kola(r: float) -> float:
    r = float(r)
    if not type(r) in [int, float]:
        raise TypeError("Zły format danej")
    # return 3.14 * (r ** 2)
    return math.pi * (r ** 2)

print(oblicz_pole_kola("2.0"))