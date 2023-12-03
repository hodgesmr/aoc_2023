import re
from utils import timed, get_input_lines


def part_1(input):
    part_sum = 0
    input_len = len(input)
    line_len = len(input[0])

    for i, line in enumerate(input):
        num_locations = re.finditer("\d+", line)
        for num_location in num_locations:
            evaluated = False
            start = num_location.start()
            end = num_location.end()  # non-inclusive
            num = int(line[start:end])

            # inspect locations built around [line offset, index]
            inspect_locations = [(0, start - 1), (0, end)]  # [left, right]
            for j in range(start - 1, end + 1):
                inspect_locations.append((-1, j))  # line above
                inspect_locations.append((1, j))  # line below

            # check all the inspection locations
            for il in inspect_locations:
                if not evaluated:
                    line_index = i + il[0]
                    if line_index >= 0 and line_index < input_len:
                        inspect_line = input[line_index]
                        char_index = il[1]
                        if char_index >= 0 and char_index < line_len:
                            inspect_char = inspect_line[char_index]
                            if inspect_char != "." and not inspect_char.isdigit():
                                part_sum += num
                                evaluated = True
    return part_sum


def part_2(input):
    gear_ratio_sum = 0
    input_len = len(input)

    for i, line in enumerate(input):
        # find all the asterisks in the current line
        asterisk_locations = re.finditer("\*", line)
        for asterisk_location in asterisk_locations:
            adjacent_nums = []
            start = asterisk_location.start()
            end = asterisk_location.end()  # non-inclusive

            # find all the numbers in the current line
            current_line_num_locations = [
                (match.start(), match.end()) for match in re.finditer("\d+", line)
            ]
            # find all the numbers in the previous line
            previous_line = None
            previous_line_num_locations = []
            if i > 0:
                previous_line = input[i - 1]
                previous_line_num_locations = [
                    (match.start(), match.end())
                    for match in re.finditer("\d+", previous_line)
                ]
            # find all the numebrs in the next line
            next_line = None
            next_line_num_locations = []
            if i < input_len - 1:
                next_line = input[i + 1]
                next_line_num_locations = [
                    (match.start(), match.end())
                    for match in re.finditer("\d+", next_line)
                ]

            # check them all current line nums if they're next to the asterisk (this is not the most effient way to do this)
            for num_location in current_line_num_locations:
                adjacent = num_location[1] == start or num_location[0] == end
                if adjacent:
                    num = int(line[num_location[0] : num_location[1]])
                    adjacent_nums.append(num)

            # check the previous and next lines for adjacencies
            for inspecting_line, inspecting_line_num_locations in [
                (previous_line, previous_line_num_locations),
                (next_line, next_line_num_locations),
            ]:
                # inspect every number in the previous / next lines
                for num_location in inspecting_line_num_locations:
                    num_start = num_location[0]
                    num_end = num_location[1]
                    # set intersectino to discover overlapping char indexes
                    adjacent = set(range(start, end + 1)).intersection(
                        set(range(num_start, num_end + 1))
                    )
                    if adjacent:
                        num = int(inspecting_line[num_start:num_end])
                        adjacent_nums.append(num)

            if len(adjacent_nums) == 2:
                gear_ratio = adjacent_nums[0] * adjacent_nums[1]
                gear_ratio_sum += gear_ratio

    return gear_ratio_sum


timed(part_1, [get_input_lines()])
timed(part_2, [get_input_lines()])
