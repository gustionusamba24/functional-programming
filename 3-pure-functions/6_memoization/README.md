# Memoization

[Memoization](https://en.wikipedia.org/wiki/Memoization) is a technical term that basically means caching (storing a copy of) the result of a computation so that we don't have to compute it again in the future. For example, take this simple function:
```python
def add(x: int, y: int) -> int:
    return x + y
```

A call of `add(5, 7)` will always evaluate to `12`. If you think about it, once we know that `add(5, 7)` can be replaced with `12`, we can just store `12` in memory as the result value. Then, the next time we need to `add(5, 7)`, we can look up the value instead of repeating a (potentially expensive) CPU operation.

The slower and more complex the function, the more memoization can help speed things up.
  
> It's pronounced "memOization," not "memORization." This confused me for quite a while in college. I thought my professor just didn't speak goodly...
<br />
<br />

## Assignment
Counting the words in a document can be slow, so we want to memoize it. Complete the `word_count_memo` function. It takes two inputs:
1. A `document` string.
2. A `memos` dictionary. The keys are full document strings, and the values are the word count of the document.

It should return a tuple of two values:
1. The word count of the given document.
2. An updated `memos` dictionary.

Here are the steps to follow:
1. Create a [`.copy()`](https://docs.python.org/3/library/copy.html#module-copy) of the memos dictionary.
2. If the document is [in](https://docs.python.org/3/library/stdtypes.html#dict) the `memos` dictionary, just `return` the associated word count and the `memos` copy. No need to recompute the count!
3. Otherwise, use the provided `word_count` function to count the words in the given `document`.
4. Store the word count in the `memos` copy.
5. Return the word count and the updated `memos` copy.