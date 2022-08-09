# Practice 2
This folder contains my codes for practice 2 tasks
of subject *Python programming*.
The full practice document can be found
[here](https://github.com/true-grue/kispython).
Summary of the tasks is as follows:

## Task 1
Write one-liners for the following tasks:
1. Cast elements of list `s` from string to integer.
2. Count unique elements in sequence `s`
3. Reverse sequence `s` without using functions
4. Return list of indexes of occurrences of element x in sequence `s`
5. Sum elements of list `s` with even indexes
6. Find the longest string in string list `s`

## Task 2
In the following fragment one of three strings is chosen by index `i`:
```py
i = 0
['much','code','wow'][i] # 24 symbols
```
Shorten the second line to 19 symbols without using functions.

### Solution:
This can be done by using slices like so:
```py
for i in range(3):
    # old ...05...10...15...20..24
    res = ['much','code','wow'][i]
    # new ...05...10...15..19
    res = 'mcwuoocdwhe'[i::3]
    # ^    m  u  c  h 
    # ^     c  o  d  e
    # ^      w  o  w  
```

## Task 3
Write a `generate_groups()` function that generates
(not just prints) a list of group names like on the
Teacher Digital Assistant [site](http://kispython.ru/).

## Task 5
Write a generator of reports on digital economics.
Data for generation is given in the practice document.

## Task 8
Write a generator of full names.
You may use a list of common names,
but you have to generate the last names yourself.

## Task 10
Implement a `parse_subj(text)` function
to parse titles of letters with tasks.
It needs to parse the group and variant number.

## Task 11
Implement the direct and inverse BWT (Burrows-Wheeler Transform).
Check how it works with RLE (Run-Length Encoding).

## Task 13
Implement a command line script that forms
a tree of directories and files starting from the given path.
The result should be given in
[graphviz](https://dreampuf.github.io/GraphvizOnline/) format.

## Task 14
Implement a function that would format table data like the
[tabulate](https://github.com/astanin/python-tabulate) module.

## Notes:
- I made task 13 in two versions (`pr2-task13.py` and `graphdir.py`).
  The first one is all defined in code, the second one has more functionality
  and takes arguments from the command line. Also it took a lot of time...
