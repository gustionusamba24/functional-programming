def hex_to_rgb(hex_color: str) -> tuple[int, int, int]:
    # ?
    if len(str(hex_color)) != 6 or not is_hexadecimal(hex_color):
        raise Exception("not a hex color string")

    r = int(hex_color[:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:], 16)
    return r, g, b


# Don't edit below this line


def is_hexadecimal(hex_string: str) -> bool:
    try:
        int(hex_string, 16)
        return True
    except Exception:
        return False


hex_code = "A020F0"
r = int(hex_code[0:2], 16)
g = int(hex_code[2:4], 16)
b = int(hex_code[4:], 16)
print(r, g, b)