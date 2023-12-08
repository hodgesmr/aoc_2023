from collections import defaultdict
from utils import timed, get_input_lines


# Parse the card strings
def parse_card(card):
    card_id, nums = card.split(":")
    card_id = int(card_id.split()[1])
    winning, mine = nums.split("|")
    winning = set([int(w) for w in winning.split()])
    mine = set([int(m) for m in mine.split()])

    return card_id, winning, mine


def part_1(input):
    points = 0
    for card in input:
        _, winning, mine = parse_card(card)
        # Find the number of intersecting numbers from the sets
        win_count = len(mine.intersection(winning))
        if win_count:
            # hooray powers of two
            card_points = 2 ** (win_count - 1)
            points += card_points
    return points


def part_2(input):
    # Keep a dictionary of how many instances of each card
    # default to 1
    instances = defaultdict(lambda: 1)
    for card in input:
        card_id, winning, mine = parse_card(card)
        win_count = len(mine.intersection(winning))

        if win_count:
            # Add to the instance counts
            # multiply by the number of instances of the current card
            multiplier = instances[card_id]
            for i in range(card_id + 1, card_id + win_count + 1):
                instances[i] += multiplier

    return sum([instances[i] for i in range(1, len(input) + 1)])


timed(part_1, [get_input_lines()])
timed(part_2, [get_input_lines()])
