def list_files(
    parent_directory: dict[str, dict | None], current_filepath: str = ""
) -> list[str]:
    file_paths: list[str] = []

    for name in parent_directory.keys():
        if parent_directory[name] is None:
            file_paths.append(f"{current_filepath}/{name}")

            # Debugging
            print(f"File found: {current_filepath}/{name}")
        else:
            file_paths.extend(list_files(parent_directory[name], f"{current_filepath}/{name}"))

    return file_paths


musics: dict[str, dict | None] = {
    "Music": {
        "Rock": {
            "enter-sandman.mp3": None,
            "back-in-black.mp3": None,
        },
        "Pop": {
            "Maroon5": {
                "sugar.mp3": None,
                "animals.mp3": None,
            },
            "demons.mp3": None,
        },
    }
}

print(list_files(musics))