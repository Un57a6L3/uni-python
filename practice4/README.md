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
  - [Task 2 (In-built functions)](#task-2-in-built-functions)
  - [Task 5 (Context manager)](#task-5-context-manager)
  - [Task 8 (Sierra AGI-graphics)](#task-8-sierra-agi-graphics)

---
## Task 1 (Hash table) *// not in variant*
> Implement a hash table data structure, an analogue of built-in `dict`. Use the function `hash`.
> 1. Implement methods for reading, writing, getting the size of the hash table.
> 2. Make the above mentioned methods standard operators/functions, as in `dict`.
> 3. Implement support of `for` loops.

### Description
So, how does a hash table work? Every key is passed through a hash function, the output hash being the index of the so-called **bucket** where the key-value pair is stored. However, a hash function may output the same hash for different inputs. That is called a **collision**. If a collision occurs, we'll make a linked list at the index and append the new pair.

You can find the full code [here][t1].

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
        self.capacity = capacity  # number of buckets
        self.debug = debug        # flag for debug prints
        self.size = 0             # counter of elements
        self.taken = 0            # counter of non-empty buckets
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

## Task 2 (In-built functions)
> 1. Write code that prints all variables of a class object.
> 2. Write code that calls a class object's method by its name given as string.

As the task name suggests, we'll use in-built functions. For the first subtask we'll use the `vars(obj)` function that does exactly what we want. For the second subtask we can use the `getattr(obj, 'attr')` function. Here's the [code][t2].

## Task 5 (Context manager)
> Implement classes to write HTML code using the `with` statement.
> 
> Usage example:
> ```python
> html = HTML()
> with html.body():
>     with html.div():
>         with html.div():
>             html.p('Line one')
>             html.p('Line two')
>         with html.div():
>             html.p('Line three')
> print(html.get_code())
> ```
> Result:
> ```
> <body>
> <div>
> <div>
> <p>Line one</p>
> <p>Line two</p>
> </div>
> <div>
> <p>Line three</p>
> </div>
> </div>
> </body>
> ```

The `with some_expression:` statement works like this:
1. `some_expression` is processed
2. The special method `__exit__()` is loaded.
3. The special method `__enter__()` is executed.
4. The block inside `with` is executed.
5. The `__exit__()` method is executed.

So we need are a `HTML` class with a list of strings and methods `body()`, `div()` and `p()`. The first two will return an object of a class with overloaded `__enter__()` and `__exit__()` methods that append tags to the list, the last will just append a `<p>...</p>` tag.

Sounds complicated, I know. I was confused as well. Just take a look at the [code][t5] and you'll understand all that.

## Task 8 (Sierra AGI-graphics)

> Background graphics in old Sierra games was represented as a sequence of commands. The result looked similar to vector graphics. The original King's Quest game had a 160x200px resolution, but you can try redrawing them in high resolution. There is a code template given.
> 1. Implement command parsing from graphic files in `data/PIC.*`.
> 2. Using `tkinter`, draw the result in high resolution without fill. Keep in mind the game has two screens: the picture screen and priority screen.
> 3. *(higher difficulty)* Come up with a way to correctly fill screen sections.

No explanation here yet, but you can take a look at the [code][t8].

[t1]: hash.py
[t2]: pr4-task2.py
[t5]: pr4-task5.py
[t8]: pr4-task8.py

[kp-rep]: https://github.com/true-grue/kispython
