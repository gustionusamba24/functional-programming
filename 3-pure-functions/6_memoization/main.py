def word_count_memo(document: str, memos: dict[str, int]) -> tuple[int, dict[str, int]]:
    copied_memos = memos.copy()
    if document in copied_memos:
        return copied_memos[document], copied_memos
    else:
        count = word_count(document)
        copied_memos[document] = count
        return count, copied_memos


# Don't edit below this line


def word_count(document: str) -> int:
    count = len(document.split())
    return count
