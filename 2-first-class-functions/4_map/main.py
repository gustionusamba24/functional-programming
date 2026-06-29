def change_bullet_style(document: str) -> str:
    splitted_document = document.split("\n")
    changed_bullets = map(convert_line, splitted_document)
    return "\n".join(changed_bullets)


# Don't edit below this line


def convert_line(line: str) -> str:
    old_bullet = "-"
    new_bullet = "*"
    if len(line) > 0 and line[0] == old_bullet:
        return new_bullet + line[1:]
    return line
