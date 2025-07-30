
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



def get_color_map_string():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    map_lines = []
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            # The bug is in the formatting here, specifically the alignment
            # The current f-string doesn't ensure consistent spacing for the number.
            map_lines.append(f'{i * 5 + j} | {major} | {minor}')
    return "\n".join(map_lines), len(major_colors) * len(minor_colors)

def print_color_map():
    map_string, num_pairs = get_color_map_string()
    print(map_string)
    return num_pairs

# Capture the output to test its format
output_string, result = get_color_map_string()

# We expect a consistent format, for example, " 1 | White | Orange" or "10 | Red | Green".
# The misalignment means the space before '|' will vary.
# Let's check a specific line for misalignment.
# For example, look at line 1 and line 10.
# The single-digit numbers won't take up the same space as double-digit numbers,
# leading to the '|' shifting.

# This assert will now fail because of the inconsistent spacing
# We are checking for a specific pattern that indicates proper alignment.
# The original code will produce different spacing before the first '|' for single vs double digit numbers.
# For example: "1 | White | Orange" vs "10 | Red | Green"
# Notice how '1 ' is 2 chars + space, but '10 ' is 3 chars + space.
# A correctly aligned string would use padding, like "{:2d}".
expected_aligned_pattern_for_single_digit = " 1 | White | Orange"
expected_aligned_pattern_for_double_digit = "10 | Red | Green" # This line's format will also be inconsistent

# Let's pick a line that will clearly show misalignment if not padded.
# The 10th line (index 9 in a 0-indexed list of lines) would be "9 | White | Slate" if it were 0-indexed.
# Let's consider the 11th line (index 10) which is for major color 'Red', minor 'Green', pair number '10'.
# In the original code's output, it would be '10 | Red | Green'.
# Let's compare this to a line like '1 | White | Blue' -> '0 | White | Blue'
# If `get_color_map_string()` is called, the first line is "0 | White | Blue"
# The 11th line (index 10) should correspond to 10 (Red-Green)
lines = output_string.split('\n')

# Check if the separator '|' is at a consistent position
# For this, we can find the index of the first '|' in various lines.
# If they are not equal, it means misalignment.

# Get the position of the first '|' in the first line (single digit number)
pos_first_bar_line0 = lines[0].find('|')

# Get the position of the first '|' in a line with a double digit number, e.g., the 10th pair (index 9 or 10 depending on 0 or 1 based index of number)
# Let's consider the pair for 10 (Red, Green), which is line index 10 in the `map_lines` list.
pos_first_bar_line10 = lines[10].find('|')

# The assertion will fail if these positions are different, indicating misalignment.
assert(pos_first_bar_line0 == pos_first_bar_line10)


assert(result == 25) # This assertion will still pass, as it only checks count.
print("All is well (maybe!)")
