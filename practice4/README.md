# Python Practice 4
This folder contains my codes for practice 4 tasks of subject *Python programming*.
The full practice document can be found [here][kp-rep].

Table of Contents:
- [Python Practice 4](#python-practice-4)
  - [Task 1 (Hash table) *// not in variant*](#task-1-hash-table--not-in-variant)
    - [Description](#description)
    - [Classes](#classes)
    - [Basic methods](#basic-methods)
    - [Operators](#operators)
    - [Iteration](#iteration)
    - [Rehashing](#rehashing)
    - [Testing](#testing)

---
## Task 1 (Hash table) *// not in variant*
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

You can find the full code [here][hash-table].

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

### Basic methods
For subtask 1 we need to implement writing and reading methods, and a size method.

To write an element pair into the table, we first need to get the hash of the key. It can be done like this: `hash(key) % self.capacity`. Now we check the bucket with the calculated index. If it is empty, put the element there. If is occupied, iterate it and put the element at the end.

To read an element by key, we need to get its hash and iterate the corresponding bucket. If an element with the given key is found, return it. If not, return `None`.

Getting the table size (length) is simple - just have a variable that stores number of elements, and increment it each time you write a new element.

### Operators
For subtask 2 we need to make the above mentioned methods operators.

It is actually very easy - classes in Python have special methods that are related to functions and operators. What we need to do is overload them as following:
- To make `obj[key] = value` work, we need to name our writing method `__setitem__()`.
- To make `obj[key]` work, we need to name our reading method `__getitem__()`.
- To make `len(obj)` work, we need to name our size method `__len__()`.

### Iteration
For subtask 3 we need to implement `for` loop support.

Making a class object iterable requires two special methods: `__iter__()` serves as a constructor for the iterator object, `__next__()` returns the next item for each iteration. So, we need to iterate all buckets, and all elements for each of the buckets. For that we'll need to store the index of the current bucket, and the current element (node). With each iteration we need to find next node in the current bucket, or if it is empty, the next occupied bucket. After the last element we need to raise the `StopIteration` exception.

### Rehashing
The downside of having linked lists instead of single elements raises is the raise of complexity from constant to linear. So, when the table becomes full enough, we need to increase its capacity and readd the elements, because the indexes will now differ. That process is called **rehashing**. It should be done when about 3/4 of the buckets are occupied.

To rehash the table, we need to create a new set of counters and buckets, as we'll need the old ones in the process. Using the iteration methods we created, we can just add every element to the new set of buckets and update the counters accordingly. When all the elements are added, replace the old counters and buckets with the new ones.

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
>>> ''.join([str(key) for key, value in a])
'0123456789'
>>> ''.join([str(key) for key, value in b.items()]) 
'0123456789'
```

[hash-table]: hash.py

[kp-rep]: https://github.com/true-grue/kispython
