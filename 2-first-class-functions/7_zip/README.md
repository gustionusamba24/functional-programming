# Zip
The [zip function](https://docs.python.org/3/library/functions.html#zip) takes two iterables (often lists), and returns a new iterable where each element is a tuple containing one element from each of the original iterables.
```python
a: list[int] = [1, 2, 3]
b: list[int] = [4, 5, 6]

c: list[tuple[int, int]] = list(zip(a, b))
print(c)
# [(1, 4), (2, 5), (3, 6)]
```

## Assignment
Complete the `pair_document_with_format` function. It takes two lists of strings as input:
* `doc_names`: the names of documents
* `doc_formats`: the file formats of the documents

1. `zip` up the lists into a single list of tuples, with the name as the first index and the format as the second index in each tuple.
2. [filter](https://docs.python.org/3/library/functions.html#filter) the list of tuples to include only tuples where the format is one of the given valid_formats.
3. Return the result as a list.