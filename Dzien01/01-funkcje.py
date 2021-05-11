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


# funkcje z parametrami opcjonalnymi
def create_employee(fname, lname, phone="221234567", email="hello@company.com"):
    return {
        "fname": fname, "lname": lname,
        "phone": phone, "email": email
    }

"""
print(create_employee("Marek", "Markiewicz", "606123456", "gmarkiewicz@wick.com"))
print(create_employee("Marek", "Markiewicz"))
print(create_employee("Marek", "Markiewicz", email="gmarkiewcz2@wick.com"))
print(create_employee("Marek", "Markiewicz", phone="500478965"))
print(create_employee("Marek", "Markiewicz", "500478965"))
print("Hello", "world!")
print("Hello", "world!", sep=" | ")
print("Hello", "world!", sep=" | ", end=" **KONIEC LINI") """
