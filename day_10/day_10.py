north = ['|', '7', 'F']
south = ['|', 'L', 'J']
west = ['-', 'F', 'L']
east = ['-', 'J', '7']


def get_next_position(path_direction, symbol, line_num, line_position, list_of_lines):
    current_line = list_of_lines[line_num]
    prev_line = None
    if line_num > 0:
        prev_line = list_of_lines[line_num - 1]
    n_line = None
    if line_num < len(list_of_lines) - 1:
        n_line = list_of_lines[line_num + 1]

    if path_direction == 'south':
        if symbol == '|':
            return 'south', line_num + 1, line_position, n_line[line_position]
        elif symbol == 'L':
            return 'east', line_num, line_position + 1, current_line[line_position + 1]
        elif symbol == 'J':
            return 'west', line_num, line_position - 1, current_line[line_position - 1]
    elif path_direction == 'north':
        if symbol == '|':
            return 'north', line_num - 1, line_position, prev_line[line_position]
        elif symbol == 'F':
            return 'east', line_num, line_position + 1, current_line[line_position + 1]
        elif symbol == '7':
            return 'west', line_num, line_position - 1, current_line[line_position - 1]
    elif path_direction == 'east':
        if symbol == '-':
            return 'east', line_num, line_position + 1, current_line[line_position + 1]
        elif symbol == '7':
            return 'south', line_num + 1, line_position, n_line[line_position]
        if symbol == 'J':
            return 'north', line_num - 1, line_position, prev_line[line_position]
    elif path_direction == 'west':
        if symbol == '-':
            return 'west', line_num, line_position - 1, current_line[line_position - 1]
        elif symbol == 'F':
            return 'south', line_num + 1, line_position, n_line[line_position]
        elif symbol == 'L':
            return 'north', line_num - 1, line_position, prev_line[line_position]


def find_start(list_of_lines):
    for line_number, current_line in enumerate(list_of_lines):
        try:
            return 'S', line_number, current_line.index('S')
        except ValueError:
            pass


def find_start_directions(current_line, line_index, char_index, p_line=None, n_line=None):
    possible_directions = []
    if p_line:
        if p_line[char_index] in north:
            possible_directions.append(('north', p_line[char_index], line_index - 1, char_index))
    if n_line:
        if n_line[char_index] in south:
            possible_directions.append(('south', n_line[char_index], line_index + 1, char_index))
    if char_index > 0:
        if current_line[char_index - 1] in west:
            possible_directions.append(('west', current_line[char_index - 1], line_index, char_index - 1))
    if char_index < len(current_line) - 1:
        if current_line[char_index + 1] in east:
            possible_directions.append(('east', current_line[char_index + 1], line_index, char_index + 1))

    return possible_directions


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()

    char, start_line, start_position = find_start(lines)
    print('starting position', char, start_line, start_position)
    path = [(start_line, start_position)]
    previous_line = start_line - 1
    next_line = start_line + 1
    nex_pos = find_start_directions(lines[start_line], start_line, start_position, lines[previous_line],
                                    lines[next_line])
    print('possible directions:', nex_pos)
    direction, pipe, line_idx, position, = nex_pos[0]
    path.append((line_idx, position))
    steps = 1
    while pipe != 'S':
        # print(direction, line_idx, position, pipe)
        direction, line_idx, position, pipe = get_next_position(direction, pipe, line_idx, position, lines)
        steps += 1
        path.append((line_idx, position))
    print('max_steps', int(steps / 2))
    print('pt 2')

    enclosed_tiles = 0
    for line_idx, line in enumerate(lines):
        tiles_going_south = 0
        new_line = []
        for char_idx, char in enumerate(list(line)):
            if (line_idx, char_idx) in path:
                if char in south:
                    tiles_going_south += 1
                new_line.append('x')
                continue
            if tiles_going_south % 2 == 0:
                new_line.append(" ")
            else:
                new_line.append("*")
                enclosed_tiles += 1
        print(''.join(new_line))
    print('enclosed_tiles', enclosed_tiles)
