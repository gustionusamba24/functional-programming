# Anonymous Functions
Anonymous functions have no name, and in Python, they're called [lambda functions](https://docs.python.org/3/reference/expressions.html#lambda) after [lambda calculus](https://en.wikipedia.org/wiki/Lambda_calculus). Here's a lambda function that takes a single argument `x` and returns the result of `x + 1`:
```
lambda x: x + 1
```

Notice that the [expression](https://docs.python.org/3/reference/expressions.html#expressions) `x + 1` is returned automatically, no need for a `return` statement. Compare that to how you'd normally write a function:
```
def add_one(x: int) -> int:
    return x + 1
```

Because functions are just values, we can assign the function to a variable named `add_one`:
```
from collections.abc import Callable

add_one: Callable[[int], int] = lambda x: x + 1
print(add_one(2))
# 3
```

Lambda functions might look scary, but they're still just functions. Because they simply return the result of an expression, they're often used for small, simple evaluations. Here's an example that uses a lambda to get a value from a dictionary
```
get_age: Callable[[str], int | str] = lambda name: {
    "lane": 29,
    "hunter": 69,
    "allan": 17
}.get(name, "not found")
print(get_age("lane"))
# 29
```

## Assignment
Complete the `file_type_getter` function. This function accepts a list of tuples, where each tuple contains:
1. A "file type" (e.g. `"code"`, `"document"`, `"image"`, etc.)
2. A list of associated file extensions (e.g. `[".py", ".js"]` or `[".docx", ".doc"]`)

The function returns a function for looking up the file type of a given file extension.

1. Create an empty dictionary to map each file extension to its file type.
2. Loop through the `file_extension_tuples`:
    * Loop through the file extensions.
        * Add each extension to the dictionary and assign its value to the file type.

For example, if given the following list of tuples:
```
# list of tuples
file_extension_tuples: list[tuple[str, list[str]]] = [
    ("document", [".doc", ".docx"]),
    ("image", [".jpg", ".png"])
]

# resulting dictionary
file_extensions_dict: dict[str, str] = {
    ".doc": "document",
    ".docx": "document",
    ".jpg": "image",
    ".png": "image",
}
```
3. Return a lambda function that accepts a string (a file extension) and returns its file type from the dictionary.
4. Use the [.get](https://docs.python.org/3/library/stdtypes.html#dict.get) dictionary method in the lambda function. Return the file type of the extension if found or `"Unknown"` if it's missing.