# Pure Functions
If you take nothing else away from this course, please take this: [pure functions](https://en.wikipedia.org/wiki/Pure_function) are fantastic. They have two properties:
- They always return the same value given the same arguments.
- Running them causes no [side effects](https://en.wikipedia.org/wiki/Side_effect_(computer_science)).

In short: pure functions don't do anything with anything that exists outside of their scope.


## Example of a Pure Function
```python
def find_max(nums: list[int]) -> float:
    max_val: float = float("-inf")
    for num in nums:
        if max_val < num:
            max_val = num
    return max_val
```

## Example of an Impure Function
```python
# instead of returning a value
# this function modifies a global variable
global_max: float = float("-inf")

def find_max(nums: list[int]) -> None:
    global global_max
    for num in nums:
        if global_max < num:
            global_max = num
```
<br />
<br />

## Assignment
There's a bug in the `convert_file_format` function! Right now, it relies on data outside its own scope. These global values can be changed by other parts of the code, so they are not guaranteed to be the same every time `convert_file_format` is called.

Fix the bug by making `convert_file_format` a pure function. It should depend only on data that is scoped inside the function.

> ⚠️ Don't change the signature of `convert_file_format`.