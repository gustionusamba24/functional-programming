# Recursion Practice Part 2
In Doc2Doc, we might have documents nested inside other documents, forming a kind of tree. You know how crazy `.docx` files can get...

Anyway, we want to find out how deeply nested a given document is.

## Assignment
**Complete the `count_nested_levels` function**. It takes a dictionary of nested documents, the target document ID, and the current level of the document.

1. Iterate over the `nested_documents` dictionary. For each:
    1. If the current `document_id` matches the `target_document_id`, return its `level` of nesting.
    2. Otherwise, recursively call `count_nested_levels` on the nested dictionary for this `document_id`, with the `level` incremented by `1`.
    3. If the recursive call found the `target_document_id's` level, return it.
2. If the `target_document_id` doesn't exist, the function should return `-1`.

## Example
In this dictionary, the document with ID `3` is nested 2 levels deep. Document `2` is nested 1 level deep.

```python
nested_documents: dict[int, dict] = {
    1: {
        3: {}
    },
    2: {}
}
```