# Python Practice 3
This folder contains my codes for practice 3 tasks of subject *Python programming*.
The full practice document can be found [here][kp-rep].

---
## Task 1 (Doctest)
> 1. Add documentation to program in docstring format.
> 2. Give examples in doctest format. They must cover border cases.
> 3. Test program by calling doctest module.
> 4. Move examples to another file and test the program again.

Let's write a simple factorial function in `fact.py` and add a docstring with some tests:
```python
def fact(n: int) -> int:
    '''
    Factorial function implementation.
    >>> fact(7)
    5040
    >>> fact(5)
    120
    >>> fact(0)
    1
    '''
    result = 1
    while(n > 0):
        result *= n
        n -= 1
    return result
```

Now let's test it with command `python -m doctest -v fact.py`:
```   
Trying:    
    fact(7)
Expecting: 
    5040   
ok
Trying:
    fact(5)
Expecting:
    120
ok
Trying:
    fact(0)
Expecting:
    1
ok
1 items had no tests:
    fact
1 items passed all tests:
   3 tests in fact.fact
3 tests in 2 items.
3 passed and 0 failed.
Test passed.
```

Let's cut the REPL dialog from the documentation in `fact.py` and paste it to `fact.test`.
Now we'll test the function with `python -m doctest fact.test`.
It is without `-v` key, so we only get a message if testing fails.
Since all the tests passed, there is no message.

[kp-rep]: https://github.com/true-grue/kispython
