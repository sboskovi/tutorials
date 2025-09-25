# Python za razg

## neke osnove
- a,b = b,a
- from collections defaultdict -> d = defailtdict(list) -> d["key_not_in_dict"].append(55)
# Invert string(array)
- return newStr == newStr[::-1]

## Division
- // - integer devision
- devision round down: 
  - 5 // 2 = 2
  - -3 // 2 = -2 (ide na manju cifru, u vecini programskih jezika ide ka nuli - problem kod negativnih brojeva)
  - int(-3 / 2) - workaround

## Modulo operator - %
10 % 3 = 1
-10 % 3 = 1

### Kao u ostalim programskim jezicima
import math
math.fmod(10, -3) # =-1

## Zaokruzivanje
math.floor()
math.ceil()

## Python numbers are infinite, they never overflow
- float("inf")
- float("-inf")

## Nizovi
- arr.append() # ekvivalentno sa stack.pop
- arr.pop() 
- arr.insert(index, val) # O(n)
- arr[index] = val # O(1)
- arr = [1] * 3 # [1, 1, 1]
- arr[-1] # last element
- arr[1:3] # slicing
- a, b, c = [1, 2, 3]
- arr[0:3], arr[5:8] = arr[5:8], arr[0:3]


- for index, value in enumerate(arr): ...
- for val1, val2 in zip(arr1, arr2): ... # Vraca niz parova iz dva niza

- arr.reverse()

- arr.sort(reverse=True)
- arr.sort moze da sortira i niz stringova po abecednom redu
- arr.sort(key = lambda x: len(x)) # sortiranje stringova po duzini npr

## Stringovi
- Immutable su
- s += "abc" # Pravi novi string, slozenost O(n)
- int("123") + int("456")
- ord("a") # ASCII value
- "".join("aabc", "deef", "ggm")

## Queue
```
from collection import dequeue

q = dequeue()
q.append(1)
q.append(2)

q.popleft() # O(1) u odnosu na Niz
q.appendleft(1)

q.pop() # Sa desne strane
```

## HashSet
- Nema duplikata

mySet = set()
mySet = {1, 2, 3}
mySet = { i for i in range(i) }

## HashMap
dct = {}
Pristup elementima je O(1)

for key in dct: ...
for value in dct.values(): ...
for key, val in dct.items(): ...

## Tuples
Imutable, mogu se koristiti kao kljucevi za dictionary-e
t = (1, 2, 3)
d = { (1, 2): "Tuple as a key in dictionary" }

## Heaps
Python Heap-ovi su MIN Heap-ovi po default-u - prvi element niza (heap-a) ce biti najmanji

```
import heapq

minHeap = []
heapq.heappush(minHeap, 3)
heapq.heappush(minHeap, 2)
heapq.heappush(minHeap, 4)

minHeap[0] # = 2

heapq.heapop(minHeap)
```

Max Heap ne postoji - workaround: pomozis svaku vrijednost sa -1 prilikom ubacivanja u niz i opet sa -1 prilikom uzimanja iz niza

## Funckcije

nonlocal za ugnijezdene funkcije, ne treba za nizove npr


### Datetime
.year()

### Generatori:
- yield
- dict.iteritmes() vs dict.itmes()
- range vs xrange


### WTF
- global interpreter lock? Globalni lock za niti?
- Poredjenje dictionary-a i nizova?

- iteritmes?

