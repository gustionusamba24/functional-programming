# Ternary Expressions
[Ternaries](https://book.pythontips.com/en/latest/ternary_operators.html) are a great way to reduce a series of statements, like an `if`/`else` block, to a single expression. When you first learned how to use conditional logic in Python, it probably looked like this:
```
result: float = 0
if number % 2 == 0:
    result = number / 2
else:
    result = (number * 3) + 1
```
<br />

This code sets `result` to a dummy value like `0` (`None` would also work), then overwrites it with its "real" value based on the condition. A ternary lets us do all that in one expression:

```
result: float = number / 2 if number % 2 == 0 else (number * 3) + 1
```
<br />


Note that we also avoided mutating the `result` variable! Ternary expressions are good for maintaining immutability.
The syntax for a ternary in Python is:

```
value_a if condition else value_b
```
<br />


This qualifies as an expression because it's a single statement that evaluates to a value – one of two values, depending on the condition.
<br />

## When to Use Ternaries
Ternary expressions are cool, but don't overdo it. If you're dealing with complex conditional logic, it's often easier to work with full `if`/`else` blocks than to try to nest ternaries inside each other.

```
msg: str = (
    "Access granted"
    if (
        user.is_authenticated
        and (user.role == "admin" or (user.role == "editor" and not user.suspended))
    )
    else ("Access limited" if user.is_authenticated else "Access denied")
)
```
<br />
<br />

## Assignment
Our Doc2Doc utility is designed to accept input documents in a variety of formats. It chooses the appropriate parser for a document based on the extension of the file name. Currently, only Markdown and plain-text parsers are supported.

Fix the `choose_parser` function. The logic is correct, but we want to simplify the conditional block to a one-line ternary expression.
