# Higher-Order Functions Practice
Doc2Doc needs a way to restore documents from saved backups. However, not all original documents necessarily have backups, and some backups might be corrupted.

## Assignment
**Complete the `restore_documents` function** in one line – if you can. It takes two tuples of document strings, `originals` and `backups`, as input. It should return a single clean [set](https://docs.python.org/3/tutorial/datastructures.html#sets) of all valid documents from both tuples.
1. Combine the `originals` and `backups` tuples.
2. Convert all the combined documents to uppercase with [.upper()](https://docs.python.org/3/library/stdtypes.html#str.upper).
3. Filter out documents that are corrupted (where the string is just random numbers, checking with [.isdigit())](https://docs.python.org/3/library/stdtypes.html#str.isdigit).
4. Return a `set` to deduplicate the combined valid documents.

## Tip
I used `map`, `filter`, and lambda functions to complete the function on one "line," but it's formatted in multiple lines for readability.