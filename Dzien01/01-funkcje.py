import math
# Funkcje

a = "Ala ma kota";
b = 12.34
a , b = "Ala ma kota", 12.34
a = "ala ma kota"; b = 12.34 # nie w duchu pythona

X = 10

def test():
    #return
    global x # Globalna w funkcji, (tylko dla przykładu)
    print(x)
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


### funkcje z dowolną liczbą parametrów ####
### *args - dowolnie *argu
def many_arguments(*args):
    for arg in args:
        print(str(arg)[::-1])


many_arguments("Ala", "ma", "kota")


def many_arguments_second(_id, *args):
    print(f"ID={_id}")
    for arg in args:
        print(str(arg)[::-1])


many_arguments_second(1, "Ala", "ma", "kota")

##### funkcja z parametrami nazwanymi ####
### **kwargs - dowolnie *argu
def many_keys(_id, fallback="BRAK", **kwargs):
    # print(f"fname={kwargs['fname']}")
    # print(f"fname={kwargs.get('fname')}")
    print(f"fname={kwargs.get('fname', fallback)}")
    print(f"fname={kwargs.get('fname', fallback)}")
    print(f"fname={kwargs.get('email', fallback)}")


#many_keys(fname="Jon", lname="Wick", email ="jw@host.pl") # opcjonalny
#many_keys(fname="Jon", lname="Wick") # opcjonalny
many_keys(123, fname="Jon", lname="Wick") # wymagany
many_keys(123, fname="Jon", lname="Wick", fallback="*") # wymagany
many_keys(123, fname="Jon", lname="Wick") # wymagany
