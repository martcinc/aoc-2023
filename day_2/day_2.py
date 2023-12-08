import re
from functools import reduce
from typing import Dict, Tuple, List


def parse_line(input_line: str) -> Tuple[int, List[Dict[str, int]]]:
    game_id, games = input_line.split(': ')
    return get_game_id(game_id), [game_to_dict(game) for game in games.split('; ')]


def get_game_id(input_string: str) -> int:
    return int(re.search('Game ([0-9]+)', input_string).group(1))


def game_to_dict(game_str) -> Dict[str, int]:
    cubes = game_str.split(', ')
    cubes_dict = {}
    for roll in cubes:
        cubes_dict[roll.split(' ')[1]] = int(roll.split(' ')[0])
    return cubes_dict


def check_roll(roll_dict: Dict[str, int]) -> bool:
    return all([
        roll_dict.get('red', 0) <= 12,
        roll_dict.get('green', 0) <= 13,
        roll_dict.get('blue', 0) <= 14,
    ])


def get_min_cubes(cubes_sets: List[Dict[str, int]]) -> Dict[str, int]:
    output_dict = {}
    for cube_set in cubes_sets:
        for k, v in cube_set.items():
            if k not in output_dict:
                output_dict[k] = v
            elif v > output_dict[k]:
                output_dict[k] = v
    return output_dict


def get_game_power(game_dict):
    return reduce(lambda x, y: x * y, game_dict.values())


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()

    sum_possible_games = 0
    sum_game_power = 0
    for line in lines:
        game_number, sets_of_cubes = parse_line(line)
        possible_game = all([check_roll(set_of_cubes) for set_of_cubes in sets_of_cubes])
        if possible_game:
            sum_possible_games += game_number
        print('game:', game_number, '| cubes:', sets_of_cubes, '| possible: ', possible_game)
        min_number_of_cubes = get_min_cubes(sets_of_cubes)
        game_power = get_game_power(min_number_of_cubes)
        print('min_number_of_cubes:', min_number_of_cubes, 'game_power:', game_power)
        sum_game_power += game_power

    print('sum_possible_games:', sum_possible_games)
    print('sum_game_power:', sum_game_power)

