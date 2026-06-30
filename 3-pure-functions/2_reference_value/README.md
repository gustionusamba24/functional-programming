# Reference vs. Value
When you pass a value into a function as an argument, one of two things can happen:
- It's passed by reference: The function has access to the original value and can change it.
- It's passed by value: The function only has access to a copy. Changes to the copy within the function don't affect the original.

There is more nuance to it, but this explanation works for an introduction. In Python, the following types are passed by reference:
- Lists
- Dictionaries
- Sets

These types, on the other hand, are passed by value:
- Integers
- Floats
- Strings
- Booleans
- Tuples

Most container types are passed by reference (except for tuples!), and most basic types are passed by value.

## Example of Pass-By-Reference
Lists are passed by reference and are **mutable**:
```python
def modify_list(inner_lst: list[int]) -> None:
    inner_lst.append(4)
    # the original "outer_lst" is updated
    # because inner_lst is a reference to the original

outer_lst: list[int] = [1, 2, 3]
modify_list(outer_lst)
# outer_lst = [1, 2, 3, 4]
```

## Example of Pass-By-Value
Integers are passed by value; they can be copied freely but are **immutable**:
```python
def attempt_to_modify(inner_num: int) -> None:
    inner_num += 1
    # the original "outer_num" is not updated
    # because inner_num is a copy of the original

outer_num: int = 1
attempt_to_modify(outer_num)
# outer_num = 1
```

## Assignment
We have a way for Doc2Doc users to set their supported formats in their settings. In memory, we store those settings as a simple dictionary:
```python
settings: dict[str, bool] = {
    "docx": True,
    "pdf": True,
    "txt": False
}
```

Unfortunately, there's a bug in our code. When a new format is added or removed, it not only updates the new dictionary, but it changes the defaults themselves! That's not good. We want to create a new dictionary with the updates, not change the original.

Fix the bug by making `add_format` and `remove_format` pure functions that don't mutate their inputs.

## Tip
Simply assigning a new variable to an existing dictionary doesn't copy that dictionary; it points to the same dictionary. Instead, use the [`.copy()` method](https://docs.python.org/3/library/stdtypes.html#dict.copy) to create a new copy of a dictionary.