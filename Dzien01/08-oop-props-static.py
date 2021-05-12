# OOP - metody statyczne, classmethods, propertis
from datetime import date


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"name={self.name}, age{self.age}"

    @staticmethod  # dekorator. Utworzenie statycznej metody
    def is_adult(age):
        return age >= 18

    @classmethod
    def create_from_year(cls, name, yob):
        age = date.today().year - yob
        return cls(name, age)


person1 = Person("Jan", 33)
print(Person.is_adult(17))

person2 = Person.create_from_year("Bob", 1980)
print(person2)