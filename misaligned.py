
# def print_color_map():
#     major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
#     minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
#     for i, major in enumerate(major_colors):
#         for j, minor in enumerate(minor_colors):
#             print(f'{i * 5 + j} | {major} | {minor}')
#     return len(major_colors) * len(minor_colors)


# result = print_color_map()
# assert(result == 25)
# print("All is well (maybe!)")





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
        line = f'{pair_number} | {major} | {minor}'
        lines.append(line)
    return lines

def print_color_map():
    color_map = get_color_map()
    lines = format_color_map(color_map)
    for line in lines:
        print(line)
    return len(lines)





# test_color_map_module.py

def test_color_map_count():
    result = print_color_map()
    assert result == 25, f"Expected 25 pairs, but got {result}"

def test_alignment():
    color_map = get_color_map()
    lines = format_color_map(color_map)
    for line in lines:
        parts = line.split('|')
        assert len(parts) == 3, f"Line formatting broken: {line}"
        assert parts[0].strip().isdigit(), f"Pair number not a digit: {parts[0]}"
        assert parts[1].strip() in ["White", "Red", "Black", "Yellow", "Violet"], f"Unexpected major color: {parts[1]}"
        assert parts[2].strip() in ["Blue", "Orange", "Green", "Brown", "Slate"], f"Unexpected minor color: {parts[2]}"

def test_alignment_padding():
    color_map = get_color_map()
    lines = format_color_map(color_map)
    
    # This test ensures formatting is visually aligned
    lengths = [len(line.split('|')[0]) for line in lines]
    assert len(set(lengths)) == 1, f"Pair number column is not aligned: {lengths}"

    major_lengths = [len(line.split('|')[1].strip()) for line in lines]
    assert max(major_lengths) == len("Violet"), "Expected max length of major color to be 'Violet'"
    assert len(set(major_lengths)) != 1, "All major colors should not have same length — potential padding issue exposed"

# Run tests
if __name__ == "__main__":
    test_color_map_count()
    test_alignment()
    test_alignment_padding()
    print("All tests completed.")

