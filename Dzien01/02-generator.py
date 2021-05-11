
# Generatory
"""
for x in range(3):
    print(x)
"""

### Create Generator
def my_ganerator():
    n = 1
    print("Pierwsze wzbudzenie")
    yield n

    n += 1
    print("Drugie wzbudzenie")
    yield n

    n += 1
    print("Trzecie wzbudzenie")
    yield n


gen = my_ganerator()
items = []
x = next(gen)
items.append(x)

x = next(gen)
items.append(x)

x = next(gen)
items.append(x)

print(items)


# wykorzystanie generatora w uchwycie pliku
# odczyt danych z pliku.
with open("01-funkcje.py", "rt", encoding="utf8") as fd:
    for line in fd:
        print(line.rstrip())









