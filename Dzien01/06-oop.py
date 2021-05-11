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


cola_cola = Product(1, "CoCa-Cola", 4.99)
print(cola_cola.get_info())

print(cola_cola.set_price(20))
print(cola_cola)