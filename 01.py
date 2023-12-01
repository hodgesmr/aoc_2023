import re
from utils import timed, get_input_lines


def part_1(input_lines):
    s = sum(  # sum them all up
        [
            int(d[0]) * 10 + int(d[-1])  # first digit is 10s place, last digit is 1s
            for d in [  # find all the digits in the line
                re.findall(r"\d", line) for line in input_lines
            ]
        ]
    )
    return s


def part_2(input_lines):
    map = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    # Use positive lookahead `?=` to match patterns that might overlap
    # this allows us to find 'two' and 'one' within 'twone'
    # based on the keys in the map, and digits
    # (?=(one|two|three|four|five|six|seven|eight|nine|\d))
    regex_patter = rf"(?=({'|'.join(map.keys())}|\d))"

    sum = 0
    for line in input_lines:
        discovered_numbers = re.findall(regex_patter, line)
        tens = map.get(discovered_numbers[0], discovered_numbers[0])
        ones = map.get(discovered_numbers[-1], discovered_numbers[-1])
        line_value = int(tens) * 10 + int(ones)
        sum += line_value

    return sum


timed(part_1, [get_input_lines()])
timed(part_2, [get_input_lines()])
