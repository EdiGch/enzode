# OOP

class MetaProduct:
    pass


class Product:
    def __init__(self, id, name, price):
        self.__id = id
        self.__name = name
        self.__price = price

    def get_info(self):
        return f"Id={self.__id}, nazwa:{self.__name}, price: {self.__price} "

    def set_price(self, new_price):
        self.__price = new_price

    def __str__(self):
        return self.get_info()

# Dziedziczenie klas
class Alcohol(Product):
    def __init__(self, id, name, price, type="vodka"):
        super(Alcohol, self).__init__(id, name, price) # php -> ::parent -> super
        self.__type = type

    def __str__(self):
        s = f"{super().__str__()}, type={self.__type}"
        return s


cola_cola = Product(1, "CoCa-Cola", 4.99)
print(cola_cola.get_info())

print(cola_cola.set_price(20))
print(cola_cola)

### Badanie klasy
## dir() informacje dotyczące zawartości pul i metod
print(dir(cola_cola))

cola_cola._Product__price = 999 # nadpisanie pola "prywatnego" z zewnątrz obiektu
print(cola_cola)

smirnoff = Alcohol(2, "Smirnoff", 88, "vodkaMa")
print(smirnoff)