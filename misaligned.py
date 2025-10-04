def get_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    color_map = []
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            pair_number = i * 5 + j
            color_map.append((pair_number, major, minor))
    return color_map

def format_color_map(color_map):
    lines = []
    for pair_number, major, minor in color_map:
        # BUG: No padding in formatting, causes misalignment
        line = f'{pair_number} | {major} | {minor}'  # <-- intentionally buggy
        lines.append(line)
    return lines

def print_color_map():
    color_map = get_color_map()
    lines = format_color_map(color_map)
    for line in lines:
        print(line)
    return len(lines)

