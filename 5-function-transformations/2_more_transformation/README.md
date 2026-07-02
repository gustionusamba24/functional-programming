# More Transformations
Here's some example code for you to reference as you work through the assignment:

```python
from collections.abc import Callable

def multiply(x: int, y: int) -> int:
    return x * y

def add(x: int, y: int) -> int:
    return x + y

def self_math(math_func: Callable[[int, int], int]) -> Callable[[int], int]:
    def inner_func(x: int) -> int:
        return math_func(x, x)
    return inner_func

square_func: Callable[[int], int] = self_math(multiply)
double_func: Callable[[int], int] = self_math(add)

print(square_func(5))
# prints 25

print(double_func(5))
# prints 10
```
<br />
<br />

## Assignment
Complete the `doc_format_checker_and_converter` function. It takes a `conversion_function` and a list of `valid_formats` as parameters. It should return a new function that takes two parameters of its own:

* `filename`: The name of the file to be converted
* `content`: The content (body text) of the file to be converted

1. If the file extension of the `filename` is in the `valid_formats` list, then return the result of calling the `conversion_function` on the `content`.
2. Otherwise, [raise](https://docs.python.org/3/tutorial/errors.html#raising-exceptions) a [ValueError](https://docs.python.org/3/library/exceptions.html#ValueError) with the following message:
    ```
    invalid file format
    ```

## Tips
* You can use the [`.split()` method](https://docs.python.org/3/library/stdtypes.html#str.split) on the `filename` to get the file extension. Then use the `in` keyword to check if a value is in a list.
* `capitalize_content` and `reverse_content` are "conversion functions" that will be passed into our `doc_format_checker_and_converter` function by the tests.