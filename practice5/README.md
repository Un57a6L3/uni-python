# Python Practice 5
This folder contains my codes for practice 5 tasks of subject *Python programming*.
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

Here are the [code][t1] and [test][t1-test] files
(they've been edited since this readme).

The second subtask in task 4 requires 100% branch coverage.
To check it I ran these three commands:
- `coverage run --branch -m pytest fact.py`
- `coverage run --branch -m pytest test_fact.py`
- `coverage report`

Here's what I got:
```
Name           Stmts   Miss Branch BrPart  Cover
------------------------------------------------
fact.py           13      0      8      0   100%
test_fact.py      10      0      0      0   100%
------------------------------------------------
TOTAL             23      0      8      0   100%
```

---
## Task 4 (Mutation testing)
> 1. Generate some mutant programs.
> 2. Generate some mutant programs with 100% branch coverage.
> 3. Try to finish testing with no surviving mutants.
> 4. It would be convenient to move the mutation testing code
> to separate module. Unfortunately, that won't work. Why?

Here's the [code][t4]. This task was probably the hardest I've done so far.
I won't explain it here in the readme, but I took some time to write
documentation in the code itself, so check that out if you're interested.

To see the mutants (subtasks 1, 2) and how they are all killed in
testing (subtask 3), you can take a look at the [log file][t4-log].
As for subtask 4, I tried to move the function and test
into a separate file, but that resulted in all mutants surviving.
Why is that? I don't actually know, but have a couple guesses.

Maybe the testing function doesn't get a working function as
parameter if it is separate from the mutation testing module.
Or it has to do with the way **AST** handles data. Or smth else.

[kp-rep]: https://github.com/true-grue/kispython

[t1]: fact.py
[t1-test]: fact.test
[t4]: mut.py
[t4-log]: example_test.log
