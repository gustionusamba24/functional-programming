# Closure
A [closure](https://en.wikipedia.org/wiki/Closure_(computer_programming)) is a function that references variables from outside its own function body. The function definition and its environment are bundled together into a single entity.

Put simply, a closure is just a function that **keeps track of some values** from the place where it was defined, no matter where it's executed later on.

## Example
The `concatter()` function returns a function called `doc_builder` (yay higher-order functions!) that has a reference to an enclosed `doc` value.
```python
from collections.abc import Callable

def concatter() -> Callable[[str], str]:
    doc: str = ""

    def doc_builder(word: str) -> str:
        # "nonlocal" tells Python to use the 'doc'
        # variable from the enclosing scope
        nonlocal doc
        doc += word + " "
        return doc

    return doc_builder

# save the returned 'doc_builder' function
# to the new function 'harry_potter_aggregator'
harry_potter_aggregator: Callable[[str], str] = concatter()
harry_potter_aggregator("Mr.")
harry_potter_aggregator("and")
harry_potter_aggregator("Mrs.")
harry_potter_aggregator("Dursley")
harry_potter_aggregator("of")
harry_potter_aggregator("number")
harry_potter_aggregator("four,")
harry_potter_aggregator("Privet")

print(harry_potter_aggregator("Drive"))
# Mr. and Mrs. Dursley of number four, Privet Drive
```
When `concatter()` is called, it creates a new "stateful" function that remembers the value of its internal `doc` variable. Each successive call to `harry_potter_aggregator` appends to that same `doc`!

## nonlocal
Python has a keyword called [`nonlocal`](https://docs.python.org/3/reference/simple_stmts.html#nonlocal) that is required to modify a variable from an enclosing scope. Most programming languages don't require this keyword, but Python does.

## Assignment
Doc2Doc needs to keep track of how many words are in a collection of documents. **Complete the `word_count_aggregator` function**.
1. Define a `count` variable to keep track of the total number of words across all documents. Initialize it to `0`.
2. Define an inner function that accepts a string argument – i.e., a single document – and returns an integer value. In the inner function:
    1. Calculate the number of words in the input string.
    2. Add that word count to the total `count` from the outer function. You'll need to use `nonlocal` for this.
    3. Return `count`, i.e., the `nonlocal` variable.
3. From the outer function, return the inner function.

`word_count_aggregator` essentially keeps a running total of the `count` variable within a closure.

## Tip
I used [`.split()`](https://docs.python.org/3/library/stdtypes.html#str.split) to count the number of words in each document.