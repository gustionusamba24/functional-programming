# Closure Practice Part 2
Doc2Doc should be able to add [CSS](https://en.wikipedia.org/wiki/CSS) styling to an HTML file. CSS uses selectors to identify the HTML element to add the style property. Styles are essentially a chain of keys and values.
```css
p {
  color: red;
}
```

* **Selector**: `p` (targets all `<p>` elements)
* **Property**: `color`
* **Value**: `red`

## Assignment
**Complete the `css_styles` function**. It accepts a nested dictionary (`initial_styles`) as input, and returns a function (`add_style`).
1. Copy `initial_styles` to avoid modifying the original dictionary.

    > ⚠️ Because we're dealing with nested dictionaries here, the `.copy()` method will produce a shallow copy: the outer dict is a > new object, but mutating inner dicts will still affect the original one. So, you should `import copy` and use [`copy.deepcopy()`](https://docs.python.org/3/library/copy.html) instead.

2. Return an `add_style` function that:    
    1. Takes three string arguments: `selector`, `property`, and `value`. `selector` is a key in the `initial_styles` dictionary, and its value should be a dictionary.
    2. Checks if the `selector` exists in the dictionary. If not, creates a new dictionary for the `selector` value.
    3. Adds or updates the `property` with the given `value` for the selector dictionary.
    4. Returns the updated dictionary.

For example:
```python
from collections.abc import Callable

initial_styles: dict[str, dict[str, str]] = {
    "body": {
        "background-color": "white",
        "color": "black"
    },
    "h1": {
        "font-size": "16px",
        "padding": "10px"
    }
}

add_style: Callable[[str, str, str], dict[str, dict[str, str]]] = css_styles(initial_styles)

new_styles: dict[str, dict[str, str]] = add_style("p", "color", "grey")

# {
#    "body": {
#        "background-color": "white",
#        "color": "black"
#    },
#    "h1": {
#        "font-size": "16px",
#        "padding": "10px"
#    },
#    "p": {
#        "color": "grey",
#    }
# }
```
<br />
<br />

## Tip
Remember, you can assign a value to a dictionary within a dictionary like so:
```python
parent_dictionary[nested_dictionary_key][key] = value
```