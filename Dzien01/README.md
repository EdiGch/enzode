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
Operator dostępu [ ] moze służyć także do tworzenia "wycinków" kolekcji na podstawie oryginalnego obiektu.

```
users = ('Grzegorz','Mateusz', 'Kamil', 'Łukasz', 'Krzysztof')
print(users[1:3])
('Mateusz', 'Kamil')
print(users[2:4])
('Kamil', 'Łukasz')
print(users[:3])
('Grzegorz', 'Mateusz', 'Kamil')
print(users[2:])
('Kamil', 'Łukasz', 'Krzysztof')
print(users[:-1])
('Grzegorz', 'Mateusz', 'Kamil', 'Łukasz')
print(users[-2:])
('Łukasz', 'Krzysztof')
```
Podczas wycinania kolekcji możemy ustalić także "krok" wg. którego będą pobierane elementu w celu
utworzenia nowego obiektu. Dzięki temu parametrowi możemy stworzyć kolekcję z np. co drugiego elementu oryginału.
Ujemny krok oznacza rozpoczęcie tworzenia nowej kolekcji od końca.

```
users = ('Grzegorz','Mateusz', 'Kamil', 'Łukasz', 'Krzysztof')
print(users[0:4:2])
('Grzegorz', 'Kamil')
print(users[4:0:-1])
('Krzysztof', 'Łukasz', 'Kamil', 'Mateusz')
print(users[::3])
('Grzegorz', 'Łukasz')
print(users[::-1])
('Krzysztof', 'Łukasz', 'Kamil', 'Mateusz', 'Grzegorz')
```

### Funkcja len()
Liczba elementów utworzonej kolekcji.
```
testList = []
print(testList, 'length is', len(testList))
[] length is 0
testList = [1, 2, 3]
print(testList, 'length is', len(testList))
[1, 2, 3] length is 3
testTuple = (1, 2, 3)
print(testTuple, 'length is', len(testTuple))
(1, 2, 3) length is 3
testRange = range(1, 10)
print('Length of', testRange, 'is', len(testRange))
Length of range(1, 10) is 9
```
### Listy
Lista jest mutowalną kolekcją. W odrużnieniu do niemutowalnej tupli, długośc listy jak i jej zawartość mogą zostać zmienione po jej utworzeniu. 
**Pustą listę** możemy utworzyć na dwa sposoby - poprzez nawiasy kwadratowe [], lub używając konstruktora list().

```
[10,20,50,100,200]
[]
list()
print(len([10,20,50,100]))
4
liczby = [10,20,30,50]
print(liczby[2])
30
print(100 in liczby)
False
print(100 not in liczby)
True
```
#### Tym czym **lista** różni się od tupli jest jej mutowalność - stan listy może być zmieniony po jej utworzeniu.
Do zmiany pojedynczego elementu listy używamy operatora przypisania: 
``` 
numery = [20,40,80,160]
numery[0] = 10
print(numery)
[10, 40, 80, 160]

liczby = [10,20,50,100]
liczby.append(200)
print(liczby)
[10, 20, 50, 100, 200]
```
Dodanie elementu pod wskazany indeksem umożliwia mmetoda insert() przyjmująca dwa parametry:
* index - pod którym ma zostać umieszczony nowy element
* warość 

Możliwe jest także wykorzystanie wycinania w celu zastąpienia zadanego zakresu elementami z innej kolekcji:

``` 
liczby = [10,20,50,100]
liczby.insert(0,5)
print(liczby)
[5, 10, 20, 50, 100]

numery = [20,40,80,160]
numery[1:3] = [1,2]
print(numery)
[20, 1, 2, 160]
```
Usunięcie elementu spod wskazanego indeksu relizowanie jest przy pomocy metody de;:
``` 
liczby = [10,20,50,100]
del liczby[0]
print(liczby)
[20,50,100]
```

### Zbiory



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