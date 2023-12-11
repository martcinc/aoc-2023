from itertools import combinations


def get_empty_columns(space_matrix):
    empty_space = []
    col_counter = {}
    for row_idx, row in enumerate(space_matrix):
        for char_idx, char in enumerate(row):
            if char == '.':
                if char_idx not in col_counter:
                    col_counter[char_idx] = [row_idx]
                else:
                    col_counter[char_idx].append(row_idx)
    for col_idx, empty_spaces in col_counter.items():
        if len(empty_spaces) == len(space_matrix):
            empty_space.append(col_idx)
    return empty_space


def get_empty_rows(space_matrix):
    empty_space = []
    for idx, line_row in enumerate(space_matrix):
        if all(map(lambda char: char == '.', line_row)):
            empty_space.append(idx)
    return empty_space


def get_galaxies(space_matrix):
    galaxy_list = []
    galaxy_counter = 1
    for row_idx, row in enumerate(space_matrix):
        for char_idx, char in enumerate(row):
            if char == '#':
                galaxy_list.append((row_idx, char_idx))
                galaxy_counter += 1
    return galaxy_list


def list_galaxy_pairs(galaxy_list):
    return list(combinations(galaxy_list, 2))


def get_distance(galaxy_a, galaxy_b, expansion=1):

    galaxy_a_x = galaxy_a[1]
    galaxy_a_y = galaxy_a[0]
    galaxy_b_x = galaxy_b[1]
    galaxy_b_y = galaxy_b[0]
    distance_x = abs(galaxy_a_x - galaxy_b_x)
    distance_y = abs(galaxy_a_y - galaxy_b_y)
    expansion_multiplier = expansion - 1
    if expansion_multiplier:
        if galaxy_b_x > galaxy_a_x:
            traversed_empty_cols = len(list(filter(lambda x: galaxy_a_x < x < galaxy_b_x, empty_cols)))
        else:
            traversed_empty_cols = len(list(filter(lambda x: galaxy_b_x < x < galaxy_a_x, empty_cols)))
        if galaxy_b_y > galaxy_a_y:
            traversed_empty_rows = len(list(filter(lambda x: galaxy_a_y < x < galaxy_b_y, empty_rows)))
        else:
            traversed_empty_rows = len(list(filter(lambda x: galaxy_b_y < x < galaxy_a_y, empty_cols)))
        distance_x += traversed_empty_cols * expansion_multiplier
        distance_y += traversed_empty_rows * expansion_multiplier

    return distance_x + distance_y


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()

    star_map = [[char for char in line] for line in lines]
    empty_rows = get_empty_rows(star_map)
    empty_cols = get_empty_columns(star_map)
    galaxies = get_galaxies(star_map)
    pairs = list_galaxy_pairs(galaxies)

    sum_dist_2 = 0
    sum_dist_1000000 = 0

    for (galaxy_1, galaxy_2) in pairs:
        distance_with_expansion_2 = get_distance(galaxy_1, galaxy_2, expansion=2)
        sum_dist_2 += distance_with_expansion_2
        sum_dist_1000000 += get_distance(galaxy_1, galaxy_2, expansion=1000000)
    print('number of pairs', len(pairs), '-> distance:', sum_dist_2, '-> expansion 1000000:', sum_dist_1000000)
