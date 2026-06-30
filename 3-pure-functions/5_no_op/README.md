# No-Op
A [no-op](https://en.wikipedia.org/wiki/NOP_(code)) is an operation that does... nothing.

If a function doesn't return anything, it's probably impure. Apart from returning a value, the only reason for a function to exist is to perform a side effect. Otherwise it would be a no-op, right?

## Example No-Op
This function performs a useless computation, since it doesn't return anything or perform a side effect. It's a no-op.
```python
def square(x: int) -> None:
    x * x
```

## Example Side Effect
This function lacks a return statement but performs a side effect: it changes the value of the `y` variable that is outside of its scope. It's impure.
```python
y: int = 5

def add_to_y(x: int) -> None:
    global y
    y += x

add_to_y(3)
# y = 8
```

> The [global keyword](https://docs.python.org/3/reference/simple_stmts.html#global) tells Python to allow modification of the outer-scoped y variable.

## Printing is Impure
Even the `print` function (technically) has a side effect! It doesn't return anything, but it does print text to the console, which is a form of I/O.
<br />
<br />

## Assignment
Fix the `remove_emphasis` function by making it pure. `remove_emphasis` takes a document with any number of lines and removes any number of `*` characters that are at the start or end of a word. (In case you need it, here's a primer on [emphasis in Markdown](https://www.markdownguide.org/basic-syntax/#emphasis).)
For example, this:
```python
I *love* Markdown.
I **really love** Markdown.
I ***really really love*** Markdown.
```

Should become:
```python
I love Markdown.
I really love Markdown.
I really really love Markdown.
```

1. The problem is that `remove_emphasis` currently modifies a global variable called `doc`. It should instead accept a document as an argument and return a new document with emphasis removed.
2. Once you've purified `remove_emphasis`, you can also delete the global `doc` variable.

## Tips
The functions in this assignment use some Python built-ins that are definitely worth knowing:
* [`str.split`](https://docs.python.org/3/library/stdtypes.html#str.split) – splits a string into a list of substrings based on a separator (by default, whitespace)
* [`str.strip`](https://docs.python.org/3/library/stdtypes.html#str.strip) – removes leading and trailing characters (by default, whitespace) from a string
* [`map`](https://docs.python.org/3/library/functions.html#map) – applies a function to every item of an iterable (like a list) and returns an iterator of the results
* [`join`](https://docs.python.org/3/library/stdtypes.html#str.join) – combines an iterable of strings into a single string, with a specified separator between them

The syntax of `join` is simple but can be a bit counterintuitive:
```python
# We call join as a method on the separator, not on the list of strings
" ".join(["I", "love", "Python"])
# "I love Python"
```