# Python Practice 4
This folder contains my codes for practice 4 tasks of subject *Python programming*.
The full practice document can be found [here][kp-rep].

Table of Contents:
- [Python Practice 4](#python-practice-4)
  - [Task ? (Hash table)](#task--hash-table)
    - [Description](#description)
    - [Classes](#classes)
    - [Methods](#methods)
    - [Testing](#testing)

---
## Task ? (Hash table)
> (EN) Implement a hash table data structure, an analogue of built-in `dict`. Use the function `hash`. Do testing on random data using `assert` and `dict`.
> 1. Implement methods for reading, writing, getting the size of the hash table.
> 2. Make the above mentioned methods standard operators/functions, as in `dict`.
> 3. Implement support of `for` loops.

> (RU) Реализуйте свою структуру данных, хэш-таблицу, аналог встроенного `dict`. Используйте функцию `hash`. Примените тестирование на случайных данных с использованием `assert` и `dict`.
> 1. Реализуйте методы чтения, записи, получения размера хэш-таблицы.
> 2. Сделайте вышеупомянутые методы стандартными операторами/функциями, по аналогии с dict.
> 3. Реализуйте поддержку для цикла for.

### Description
So, how does a hash table work? Every key is passed through a hash function, the output hash being the index of the so-called **bucket** where the key-value pair is stored. However, a hash function may output the same hash for different inputs. That is called a **collision**. If a collision occurs, we'll make a linked list at the index and append the new pair.

The downside is that having linked lists instead of single elements raises the complexity from O(1) to O(n). So, when the table becomes full enough, we need to increase its capacity and readd the elements, because the indexes will now differ. That process is called **rehashing**. It should be done when about 3/4 of the buckets are occupied.

### Classes
For the key-value pairs we'll make a `Node` data structure:
```python
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
```

For the actual hash table we'll make a class `MyDict`. Here's the constructor:
```python
class MyDict:
    def __init__(self, capacity=32, debug=False):
        self.capacity = capacity
        self.debug = debug
        self.size = 0
        self.taken = 0
        self.__buckets = [None] * self.capacity
```

### Methods
In the class `MyDict` we will need to overload the following methods:
- Writing method `__setitem__()`: implements `obj[key] = value`
- Reading method `__getitem__()`: implements `obj[key]`
- Iterating methods `__iter__()` and `__next__()`
- Length method `__len__()` used by `len()` function
- String method `__str__()` used by `str()` function

You can find the actual code [here][hash-table].

Down below are pseudocodes for some of these methods (and rehashing)
```pseudocode setitem
def __setitem__(self, key, value):
    get index with hash function
    increment size (number of elements)

    if bucket empty:
        increment number of taken buckets
        put node in bucket, return
        
    if bucket not empty (collision):
        iterate bucket, put node at end
```
```pseudocode __getitem__
def __getitem__(self, key):
    get index with hash function
    iterate bucket in search of key
    if key is found: return value
    else: return None
```
```pseudocode rehash
def rehash(self):
    check if table need rehashing (3/4 buckets taken)
    create new set of buckets and counters
    iterate through all elements, add them to new set of bucket
    reassign the new set of buckets and counters to object fields
```
```pseudocode __iter__
def __iter__(self):
    set index to 0
    set node to first node of first bucket (may be None)
    return self
```
```pseudocode __next__
def __next__(self):
   if node is None:
       find next filled bucket
       get its first node
   get key and value of node
   set node to next node of bucket (may be None)
   return key and value
```

### Testing
 Down below you can see how this hash table works:
```pycon
>>> from hash import MyDict
>>> a = MyDict()
>>> print(a)
{}

>>> a[4] = 'foo'
>>> a[4]
'foo'

>>> a['bar'] = 7
>>> a['bar']
7

>>> print(a)
{'bar': 7, 4: 'foo'}

>>> a['sampletext'] = 5, 7, 3, 'wow'
>>> a['sampletext']                 
(5, 7, 3, 'wow')

>>> print(a)
{'bar': 7, 4: 'foo', 'sampletext': (5, 7, 3, 'wow')}
```

Here's a comparison with Python's in-built `dict`:
```pycon
>>> # fill hash table and dict with elements
>>> from hash import MyDict
>>> a = MyDict
>>> a = MyDict()
>>> b = dict()
>>> for i in range(5): 
...     a[i] = f'foo_{i}'
...     b[i] = f'foo_{i}'
...
>>> # print hash table and dict
>>> print(a)
{0: 'foo_0', 1: 'foo_1', 2: 'foo_2', 3: 'foo_3', 4: 'foo_4'}
>>> print(b)
{0: 'foo_0', 1: 'foo_1', 2: 'foo_2', 3: 'foo_3', 4: 'foo_4'}

>>> # try iterating through both
>>> # our hash table works fine
>>> ''.join([str(key) for key, value in a])
'0123456789'
>>> # build-in dict throws exception
>>> ''.join([str(key) for key, value in b]) 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 1, in <listcomp>
TypeError: cannot unpack non-iterable int object
>>> ''.join([str(key) for key, value in b])
```

[hash-table]: hash.py