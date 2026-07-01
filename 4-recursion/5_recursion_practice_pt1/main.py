def find_longest_word(document: str, longest_word: str = "") -> str:
    if len(document) == 0:
        return longest_word

    if document == " ":
        return longest_word

    words: list[str] = document.split(maxsplit=1)
    first_word: str = words[0]
    rest_of_string: str = words[1] if len(words) > 1 else ""

    if len(first_word) > len(longest_word):
        longest_word: str = first_word

    if rest_of_string:
        return find_longest_word(rest_of_string, longest_word)
    else:
        return longest_word