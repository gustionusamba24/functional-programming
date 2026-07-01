# Recursion Practice
In Doc2Doc, we have a search function to find the longest word in a document.

## Assignment
Complete the `find_longest_word` function without a loop. It accepts two string inputs, `document` and (optionally) `longest_word`, which is the current longest word and defaults to an empty string.
1. If `document` is empty or contains no words, return `longest_word`. (This is the base case.)
2. Split the string into the first word and the rest of the string.

> You can use [`.split`](https://docs.python.org/3/library/stdtypes.html#str.split) with `maxsplit=1` to split a string into a list of `[first_word, rest_of_string]`.

3. Check if the first word is longer than `longest_word`, and update that if necessary.
4. If the rest of the string exists, return the result of a recursive call on it.
5. If no text remains, return the `longest_word`.

Assume that a "word" means any series of consecutive non-whitespace characters. For example, `find_longest_word("How are you?")` should return the string `"you?"`.

Review the provided tests in `main_test.py` to see the expected behavior, including edge cases