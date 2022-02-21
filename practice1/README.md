# Practice 1
This folder contains my codes for practice 1 tasks of subject *Python programming*.
The full practice document can be found
[here](https://github.com/true-grue/kispython).
Summary of the tasks is as follows:

### Task 4
Create multiplication functions without use of actual multiplication.
There are specific limitations to number of addition and subtraction operators used.
### Task 10
Create a `fast_mul` multiplication function based on the "peasant method".
Also create a power function based on `fast_mul` and an automatic testing function.
### Task 11
Create a function that generates multiplication functions like in *Task 4*
for given parameters, that is based on the `fast_mul` function from *Task 10*.
### Task 12
Write a script that passes 4 levels in the game
[DandyBot](https://github.com/true-grue/DandyBot).
All code goes to `user_bot.py` and is executed each game tick.

## Notes:
- The "peasant method" is halving `x` and doubling `y` until `x` equals 1.
The result is the sum of all `y` values corresponding to odd `x` values.
Integer division is used, rounding down.
- The *DandyBot* game's code is not included is this repository.
The repository with the game is linked in the list above.