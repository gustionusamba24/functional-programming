def stylize_title(document: str) -> str:
    return add_border(center_title(document))



# Don't touch below this line


def center_title(document: str) -> str:
    width = 40
    title = document.split("\n")[0]
    centered_title = title.center(width)
    return document.replace(title, centered_title)


def add_border(document: str) -> str:
    title = document.split("\n")[0]
    border = "*" * len(title)
    return document.replace(title, title + "\n" + border)


# testing for center_title function
center_title = center_title("""The Importance of FP
Learn how functional programming can change the way you think about code.
Benefits include immutability, simplicity, and composability.""")
print(center_title)


add_border = add_border(center_title)
print(add_border)