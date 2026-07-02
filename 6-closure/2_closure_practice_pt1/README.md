/# Closure Practice
Remember, a [closure](https://en.wikipedia.org/wiki/Closure_(computer_programming)) is a function that retains the state of its environment. That makes it useful for tracking data as it changes over time, but it can come at the cost of understandability.

When not to use the `nonlocal` keyword: when the variable is mutable – such as a list, dictionary, or set – and you're modifying its contents rather than reassigning the variable. You only need `nonlocal` if you're reassigning a variable (which you must do to update immutable values like strings and integers).

Let's try a closure without `nonlocal`.

## Assignment
Doc2Doc needs a function to manage a growing collection of documents. **Complete the `new_collection` function**. It accepts:
* `initial_docs`: a list of strings.

The `new_collection` function should:
1. Create a copy of `initial_docs` (don't modify the original list!)
2. Return a new function, `add_doc`, that:
    1. Accepts a single string argument (a document to add)
    2. Appends that document to the copied list
    3. Returns the updated list

Each time you call the returned function, it should add to the same list (the closure keeps track of the list's state).

## Example Usage
```python
from collections.abc import Callable

my_collection: Callable[[str], list[str]] = new_collection(["doc1", "doc2", "doc3"])
print(my_collection("doc4"))
# ['doc1', 'doc2', 'doc3', 'doc4']
print(my_collection("doc5"))
# ['doc1', 'doc2', 'doc3', 'doc4', 'doc5']
```