# Zipmap
Let's practice another simple recursive function.

You may not understand recursion just yet, but by following the instructions, you will begin to grasp the fundamentals.

## Assignment
Within Doc2Doc we need to map certain properties from one document to properties of another document. **Complete the recursive zipmap function**.

It takes two lists as input and returns a [dictionary](https://docs.python.org/3/tutorial/datastructures.html#dictionaries) where the first list provides the keys and the second list provides the values.

Example usage:
```python
zipped: dict[str, float] = zipmap(
    ["Avatar: The Last Airbender", "Avatar (in Papyrus font)", "The Last Airbender (Live Action)"],
    [9.9, 6.1, 2.1]
)

print(zipped)
# {
#   'Avatar: The Last Airbender': 9.9,
#   'Avatar (in Papyrus font)': 6.1,
#   'The Last Airbender (Live Action)': 2.1,
# }
```

Here's the [pseudocode](https://en.wikipedia.org/wiki/Pseudocode):
1. If either the `keys` or the `values` list is empty, return an empty dictionary (base case). This takes care of creating a dictionary.
2. Recursively call `zipmap` on all but the first elements from `keys` and `values`.
3. Add the first element of `keys` to the resulting dictionary, and set its value to the first element in `values`.
4. Return the updated dictionary.