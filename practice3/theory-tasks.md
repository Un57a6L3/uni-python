### Task 1
Write code examples that correspond to given PEP-8 violations.
#### Answer:
1. whitespace before '('
   - `foo ()`
2. missing whitespace around operator
   - `1+2`
3. missing whitespace after ','
   - `[1,2]`
4. unexpected spaces around keyword / parameter equals
   - `foo(par = 5)`
5. expected 2 blank lines, found 1
   - given in code below 
6. multiple statements on one line (colon)
   - `if True: pass`
7. multiple statements on one line (semicolon)
   - `foo(); bar()`
8. comparison to None should be 'if cond is None:'
   - `if a == None:`
9. comparison to True should be 'if cond is True:' or 'if cond:'
   - `if a == True`

Here's a four-line piece of code that has one of each violation (would be two lines without #5):
```python
def foo (a =(1==True)):
    if a == None: bar(); return a,5

def bar(): pass
```

### Task 2
Do modules load once or with every import statement? Prove your answer with code.
#### Answer:
Modules load once. Code that proves this is listed below:
##### File **`test.py`**:
```python
print('test.py loaded successfully.')
```
##### File **`main.py`**:
```python
import test
import test
import test
```
##### Output:
```
test.py loaded successfully.
```

### Task 3
Let's say we want to change the value of a module's global variable,
so that the new value affects all users of the module.
What will the code below lead to? What can be done instead?
```python
from some_module import GLOBAL_VAR
GLOBAL_VAR = 42
```
#### Answer:
Instead of changing the value, `GLOBAL_VAR` will be redeclared.
Here's what can be done instead:
```python
import some_module
some_module.GLOBAL_VAR = 42
```

### Task 4
Uncontrolled import with `*` is no good. Try to make it controlled from the module,
so that using '*' would lead to importing only a certain part of names in the module.
#### Answer:
This can be done by using `__all__`.  It is a list of strings defining what symbols
in a module will be exported when `from <module> import *` is used on the module.
The following code in `test.py` explicitly exports the symbols `foo` and `boo`:
```python
__all__ = ['foo', 'boo']

foo = 5
bar = 10
def boo(): return 'boo'
```
These symbols can be imported like so:
```python
from test import *

print(foo)  # 5
print(boo)  # boo

print(bar)  # triggers an exception
```
