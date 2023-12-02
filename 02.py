from utils import timed, get_input_lines


def part_1(input):
    game_sum = 0
    bag = [12, 13, 14]  # r,g,b

    for game in input:
        # string parsing
        game_data = game.split(":")
        game_id = int(game_data[0].split(" ")[1])
        pulls = game_data[1].split(";")
        game_invalid = False

        # loop the game pulls
        for pull in pulls:
            if not game_invalid:  # we haven't ruled out this game yet
                pull_vector = [0, 0, 0]  # r,g,b
                cubes = pull.split(",")
                for cube in cubes:
                    num, color = cube.strip().split(" ")
                    num = int(num)

                    # update the game vector
                    if color == "red":
                        pull_vector[0] = num
                    elif color == "green":
                        pull_vector[1] = num
                    else:
                        pull_vector[2] = num
                # subtract the vectors
                diff_vector = list(map(lambda x: x[0] - x[1], zip(bag, pull_vector)))

                # invalid games fall below zero
                game_invalid = not all([i >= 0 for i in diff_vector])

        # add to our running total
        if not game_invalid:
            game_sum += game_id

    return game_sum


def part_2(input):
    total_game_power = 0

    for game in input:
        game_mins = [0, 0, 0]  # keep track of the r,g,b mins

        # string parsing
        game_data = game.split(":")
        pulls = game_data[1].split(";")

        for pull in pulls:
            cubes = pull.split(",")
            for cube in cubes:
                num, color = cube.strip().split(" ")
                num = int(num)

                # update the mins
                if color == "red" and num > game_mins[0]:
                    game_mins[0] = num
                elif color == "green" and num > game_mins[1]:
                    game_mins[1] = num
                elif num > game_mins[2]:
                    game_mins[2] = num

        # math
        game_power = game_mins[0] * game_mins[1] * game_mins[2]
        total_game_power += game_power

    return total_game_power


timed(part_1, [get_input_lines()])
timed(part_2, [get_input_lines()])
