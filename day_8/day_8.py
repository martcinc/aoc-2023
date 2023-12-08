import math


def cycle_loop(directions_list):
    while 1:
        for entry in directions_list:
            yield entry


def parse_lines(line_list):
    out = {}
    for line_string in line_list:
        location, instructions = line_string.split(' = ')
        left, right = instructions.replace('(', '').replace(')', '').split(', ')
        out[location] = dict(
            L=left,
            R=right
        )
    return out


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()

    direction_list = list(lines[0])
    direction_cycle = cycle_loop(direction_list)
    navigation = parse_lines(lines[2:])
    current_location_idx = 'AAA'
    print('starting_location', current_location_idx)
    current_location = navigation.get(current_location_idx)

    steps = 0
    while current_location_idx != 'ZZZ':
        direction = next(direction_cycle)
        new_location_idx = current_location.get(direction)
        current_location_idx = new_location_idx
        current_location = navigation.get(new_location_idx)

        # print(current_location_idx, current_location, '->', direction, '->', new_location_idx)
        steps += 1
    print('steps needed pt1:', steps)

    current_location_idxs = [k for k, v in navigation.items() if k.endswith('A')]
    print('starting_locations', current_location_idxs)
    step_list = []
    for current_location_idx in current_location_idxs:
        steps = 0
        direction_cycle = cycle_loop(direction_list)
        current_location = navigation.get(current_location_idx)
        direction = next(direction_cycle)
        while not current_location_idx.endswith('Z'):
            new_location_idx = current_location.get(direction)
            current_location_idx = new_location_idx
            current_location = navigation.get(current_location_idx)
            direction = next(direction_cycle)
            # print(current_location_idx, current_location, '->', direction, '->', new_location_idx)
            steps += 1
        step_list.append(steps)
    print(step_list)
    print('lcm of steps needed, pt2', math.lcm(*step_list))
