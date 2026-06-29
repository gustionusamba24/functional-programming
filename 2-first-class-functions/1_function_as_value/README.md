# Functions as Values
In Python, functions are just values, like strings, integers, or objects. For example, we can assign an existing function to a variable:
```
from collections.abc import Callable

def add(x: int, y: int) -> int:
    return x + y

# assign the function to a new variable
# called `addition`. It behaves the same
# as the original `add` function
addition: Callable[[int, int], int] = add
print(addition(2, 5))
# 7
```

*`Callable is the type hint for a function. Callable[[int, int], int] means a function that takes two ints as arguments and returns an int.`*

## Assignment
With the popularity of generative AI (like ChatGPT), we need to be able to convert files into pure text to be injected into prompts.

**Complete the `file_to_prompt`** function. It should take a `file` dictionary and a `to_string` function as inputs and return a formatted string. `to_string` converts a dictionary into a string.
1. Pass the `file` dictionary to the `to_string` function to convert `file` to a string and assign it to a new variable.
2. Wrap the result of the to_string function in triple backticks (```) to format it as a [code block in Markdown](https://www.markdownguide.org/basic-syntax/#code). For example:
```
an example string
```

should become:
```
\```
an example string
\```
```

Including the newlines!

## Tip
Notice the two newlines in the example above! You don't need a trailing newline, but you do need one after the first set of backticks, and another before the second set of backticks. You can achieve this by using the newline `\n` [escape character](https://en.wikipedia.org/wiki/Newline). Here's an example:
```
print("I wish the ring had never come to me.\nI wish none of this had happened.")
```

become:
```
I wish the ring had never come to me.
I wish none of this had happened.
```