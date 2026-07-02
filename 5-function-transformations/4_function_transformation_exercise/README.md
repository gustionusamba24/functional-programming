# Function Transformations Exercise
In Doc2Doc, users are asking for a filtering feature. They want a command that has dynamic options so that they can work as quickly as possible.

## Assignment
**Complete the `get_filter_cmd` function**. It takes two functions as input, `filter_one` and `filter_two`, and returns a function, `filter_cmd`.

`filter_cmd` itself should take as input two strings: `content` and `option`
1. Set the [default value](https://docs.python.org/3/tutorial/controlflow.html#default-argument-values) of the `option` argument to `"--one"`.
2. Complete `filter_cmd` so that it filters and returns the `content` according to the input `option`:
    1. If `"--one"`, use `filter_one`.
    2. If `"--two"`, use `filter_two`.
    3. If `"--three"`, use `filter_one` first, then `filter_two`.
    4. If any other `option` is passed, raise an exception:
        ```
        invalid option
        ```