def restore_documents(originals: tuple[str, ...], backups: tuple[str, ...]) -> set[str]:
    # combined = set(originals) | set(backups)
    # return {doc.upper() for doc in combined if not doc.isdigit()

    # Using filter and map functions

    return set(
        filter(
            lambda doc: not doc.isdigit(),
            map(lambda doc: doc.upper(), originals + backups)
        )
    )