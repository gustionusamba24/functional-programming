# Map
"Map," "filter," and "reduce" are three commonly used [higher-order functions](https://en.wikipedia.org/wiki/Higher-order_function) in functional programming.

In Python, the built-in [map](https://docs.python.org/3/library/functions.html#map) function takes a function and an [iterable](https://docs.python.org/3/glossary.html#term-iterable) (often a list) as inputs. It returns an [iterator](https://en.wikipedia.org/wiki/Iterator) that applies the function to every item, yielding the results.
![alt text](image.png)

With `map`, we can operate on lists without using loops and nasty stateful variables. For example, given this code:
```
def square(x: int) -> int:
    return x * x

nums: list[int] = [1, 2, 3, 4, 5]
squared_nums: list[int] = []
for num in nums:
    num_squared: int = square(num)
    squared_nums.append(num_squared)

print(squared_nums)
# [1, 4, 9, 16, 25]
```
<br />

We could use `map` instead, like this:
```
from collections.abc import Iterator

def square(x: int) -> int:
    return x * x

nums: list[int] = [1, 2, 3, 4, 5]
squared_nums: Iterator[int] = map(square, nums)

print(list(squared_nums))
# [1, 4, 9, 16, 25]
```
<br />

> `map()` returns a "map object," so the [`list()` type constructor](https://docs.python.org/3/library/stdtypes.html#list) is needed to convert it back into a standard list.
<br />
<br />

## Assignment
[Markdown](https://www.markdownguide.org/cheat-sheet/) supports two different styles of bullet points, `-` and `*`. We prefer `*`, so, we need a function to convert any `-` bullet points to `*` bullet points.

Complete the `change_bullet_style` function. It takes a document (a string) as input, and returns a single string as output. The returned string should have any lines that start with a `-` character replaced with a `*` character.

For example, this:
```
- This is a bullet
- This is a bullet
```

Becomes:
```
* This is a bullet
* This is a bullet
```

Use the built-in [map](https://docs.python.org/3/library/functions.html#map) function to apply the provided `convert_line` function to each line of the input string. Use [.split()](https://docs.python.org/3/library/stdtypes.html#str.split) and [.join()](https://docs.python.org/3/library/stdtypes.html#str.join) to split the document into a list of lines, and then join the lines back together. This should preserve the original line breaks. Don't use the `.replace()` string method.

Examples of split and join:
```
# my_document is a string with newlines
lines_list: list[str] = my_document.split("\n")

rejoined_doc: str = "\n".join(lines_list)
```