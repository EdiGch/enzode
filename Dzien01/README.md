# Python.
Szkolenie przeprowadzone przez firmę AlX https://www.alx.pl/pl/o-nas/ </br>
Data: 11.05.2021r
## Podstawowe typy danych 
Podstawowe typy danych: 
* liczby całkowite - int
* liczby zmiennoprzecinkowe - float
* napisy str
* wartość logiczne - bool

## Napisy 
```
print('Hello' + 'World')
Hello World
```
### Formatowanie napisów 
f-string, możliwe jest umieszczanie nawiasów klamrowych {}
```
print(f'Wynik dodawania to {2 + 2}!')
Wynik dodawania to 4!
```

## Wartości logiczne 
Wartości logiczne reprezentowane są w języku Python poprzez typ bool.
Wartości logiczne posiadają swoje operatory logiczne. </br>
Do łączenia warunków użyjemy operatorów logicznych:
* operator koniunkcji
* operator alternatywy - or
* operator negacji - not 

### Podstawowe operatory porównania 
```
* <	 mniejsze	 
* <=     mniejsze lub równe	 
* >	 większe	 
* >=     większe lub równe	 
==	 równe	 
!=	 różne
<>	 różne
is	 identyfikacja obiektu	 
is not	 zanegowana identyfikacja obiektu
```

```
x = 2
print x == 2 # wypisze True
print x != 2 # wypisze False
print x == 3 # wypisze False
print x < 3  # wypisze True
```

## Struktury danych

Python posiada kilka wbudowanych w język struktur danych, są to: 
* tuple - tuple
* listy - list
* słowniki - dict
* zbiory - set

### Tuple
Tupla jest niemutowalną kolekcją służącą do przechowywania wielu elementów.
Tupla, tak samo jak każda inna kolekcja w Python'ie, może przechowywać jednocześnie elementy różnego typu:

```
('abc', 1, 99.99)
```
Stworzenie pustej tupli jet możliwe przy pomocy konstruktora tuple().

### Operator dostępu 

```
users = ('Grzegorz','Mateusz', 'Kamil', 'Łukasz', 'Krzysztof')
print(users[0])
print(users[1])
print(users[4])

Grzegorz
Mateusz
Krzysztof
```
Operator [ ] umożliwia także indeksowanie elementów od tyłu kolekcji używając do tego liczy ujemnych.
```
print(users[-1])
print(users[-2])
print(users[-5])

Krzysztof
Łukasz
Grzegorz
```
### Wycinanie



```
```

```
```

```
```



## Czym jest Type Hinting 
Type Hints zostały wprowadzone do Pythona w wersji 3.5 i opisane w PEP484, jednak w dalszym ciągu są rozwijane wraz z nowymi wersjami. Umożliwiają one określenie pożądanego typu zmiennych oraz typu zwracanego przez funkcję/metodę. Określenie typu nie ma wpływu na działanie aplikacji, 
jest jednak podpowiedzią dla wszelkiego rodzaju IDE, bądź innych narzędzi sprawdzających poprawność typów. Daje więc Pythonowi kilka zalet języka statycznie typowanego.

``` 
x: str = 'Lorem ipsum dolor sit amet'
x: int = 1_000_000  # https://www.python.org/dev/peps/pep-0515/ ;)
x: float = 0.5
x: bool = True

python
from typing import List, Tuple, Set, Dict
x: List = [1, 2, 3]
x: Tuple = (1, 2, 3)
x: Set = {1, 2, 3}
x: Dict = {'one': 1, 'two': 2, 'three': 3}

```
Do bardziej precyzyjnego Type Hintingu służą parametry podanych wyżej aliasów. Przykładowo, jeśli chcemy sprecyzować możliwe typy, które lista powinna przyjmować, dodajemy argument do aliasu List:
```
python
from typing import List, Tuple, Union, Any
l1: List[int] = [1, 2, 3]  # tylko inty
l2: List[Union[int, str]] = ['text', 1, 2,]  # tylko elementy typu int lub string
l3: List[Tuple[Any, Any]] = [('1', 'two'), (3, 4.0)]  # lista tupli z dokładnie 2 elementami
```

Argumenty opcjonalne w funkcjach
```
python
def multiply(a: int, b: int, c: Optional[int] = None) -> int:
   return a * b * c if c else a * b

multiply(5, 6)
multiply(1, 2, 3)
```


generator - funkcja z pamięcią stanu </br>
decorator - funkcja która pozwala dodać nowe możliwości, nową logikę do istniejącej już funkcji, pozwala na owinięcie naszej funkcji (oryginalnej), wzbogaci ją Memomizacja funkcji

with
context manager
funkcje anonimowe
Wyjątki 