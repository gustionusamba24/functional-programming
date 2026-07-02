from collections.abc import Callable


def new_collection(initial_docs: list[str]) -> Callable[[str], list[str]]:
    docs = initial_docs.copy()

    def add_doc(document: str) -> list[str]:
        docs.append(document)
        return docs

    return add_doc
    