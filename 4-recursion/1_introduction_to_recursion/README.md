# Recursion
[Recursion](https://en.wikipedia.org/wiki/Recursion_(computer_science)) is a famously tricky concept to grasp, but it's honestly quite simple – don't let it intimidate you! A recursive function is just a function that calls itself.

> Recursion is the process of defining something in terms of itself.

## Example of Recursion
If you thought loops were the only way to iterate over a list, you were wrong! Recursion is fundamental to functional programming because it's how we iterate over lists while avoiding stateful loops. Take a look at this function that sums the numbers in a list:
```python
def sum_nums(nums: list[int]) -> int:
    if len(nums) == 0:
        return 0
    return nums[0] + sum_nums(nums[1:])

print(sum_nums([1, 2, 3, 4, 5]))
# 15
```

Don't break your brain on the example above! Let's break it down step by step:

### 1. Solve a Small Problem
Our goal is to sum all the numbers in a list, but we're not allowed to loop. So, we start by solving the smallest possible problem: summing the first number in the list with the rest of the list:
```python
return nums[0] + sum_nums(nums[1:])
```

### 2. Recurse
So, what actually happens when we call `sum_nums(nums[1:])`? Well, we're just calling `sum_nums` with a smaller list! In the first call, the `nums` input was `[1, 2, 3, 4, 5]`, but in the next call it's just `[2, 3, 4, 5]`. We just keep calling `sum_nums` with smaller and smaller lists.

### 3. The Base Case
So what happens when we get to the "end"? `sum_nums(nums[1:])` is called, but `nums[1:]` is an empty list because we ran out of numbers. We need to write a base case to stop the madness.
```python
if len(nums) == 0:
    return 0
```
The "base case" of a recursive function is the part of the function that does not call itself.
<br />
<br />

## Assignment
Doc2Doc can automatically generate various layouts for a page. There are a lot of possible layouts, so we need a [factorial](https://en.wikipedia.org/wiki/Factorial) function to calculate the total number of possible layouts.

**Complete the `factorial_r` function**. It should recursively calculate the factorial of a number.

> ⚠️ A factorial is the product of all positive integers less than or equal to a number. 
> For example, `5!` (read: "five factorial") is `5 * 4 * 3 * 2 * 1`, which is `120`.

## Tips
1. What's a small problem you can solve first?
2. How can you go from the "first" value of `x` to the "next" value of `x`, all the way down to the "last" value of `x`?
3. What's the base case that should stop the recursion?
4. Since `0!` is an [empty product](https://en.wikipedia.org/wiki/Empty_product), what should an input of `0` return?