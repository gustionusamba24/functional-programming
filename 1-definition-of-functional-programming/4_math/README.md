# It's Math
Functional programming tends to be popular among developers with a strong mathematical background. After all, a math equation isn't procedural – it's declarative. Take the following equation:
```
avg = Σx/N
```
To put this calculation in plain English:
1. `Σ` is just the Greek letter Sigma, and it represents "the sum of a collection."
2. `x` is the collection of numbers we're averaging.
3. `N` is the number of elements in the collection.
4. `avg` is equal to the sum of all the numbers in collection `x` divided by the number of elements in collection `x`.

So, the equation really just says that `avg` is the average of all the numbers in collection `x`. This math equation is a declarative way of writing "calculate the average of a list of numbers." Here's some imperative Python code that does the same thing:
```
def get_average(nums: list[int]) -> float:
    total = 0
    for num in nums:
        total += num
    return total / len(nums)
```

However, with functional programming, we would write code that's a bit more declarative:
```
def get_average(nums: list[int]) -> float:
    return sum(nums) / len(nums)
```

Here we're not keeping track of state (the total variable in the first example is "stateful"). We're simply composing functions together to get the result we want.
<br />
<br />

## Assignment
In the world of document conversion, we sometimes need to handle fonts and font sizes.

Complete the get_median_font_size function. Given a list of numbers representing font sizes, return the [median](https://en.wikipedia.org/wiki/Median) of the list.
For example:
```
[1, 2, 3] => 2
[10, 8, 7, 5] => 7
```

- Notice the second list is out of order. Sort the list so that it's in ascending order, then find the middle index, and return the middle number.
- If there's an even amount of numbers, return the smaller of the two middle numbers (I know it's not a true median, but it's good for our purposes).
- If the list is empty, just return `None`.

Here are some helpful docs:
- [sorted](https://docs.python.org/3/library/functions.html#sorted)
- [len](https://docs.python.org/3/library/functions.html#len)
- [//](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex) (floor division)

To be a good little functional programmer, your code for this lesson should not:

1. Use loops
2. Mutate any variables (it's okay to create new ones)