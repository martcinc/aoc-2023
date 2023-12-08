import re


def find_numbers(input_string: str):
    pattern = r'\d+'
    search_results = re.finditer(pattern, input_string)
    output = []
    for i in search_results:
        output.append(
            dict(
                value=i.group(0),
                start=i.span()[0],
                end=i.span()[1]
            )
        )
    return output


def find_symbols(input_string: str):
    pattern = r'[^a-zA-Z0-9.]'
    search_results = re.finditer(pattern, input_string)
    output = []
    for i in search_results:
        output.append(
            dict(
                value=i.group(0),
                start=i.span()[0],
                end=i.span()[1]
            )
        )
    return output


def get_numbers_near_a_gear(gear_dict, number_list):
    out = []
    gear_start = gear_dict.get('start')
    gear_end = gear_dict.get('end')
    for num in number_list:
        number_start = num.get('start')
        number_end = num.get('end')
        check = (
            (number_start <= gear_start <= number_end)
            or
            (number_start <= gear_end <= number_end)
        )
        if check:
            out.append(num)
    return out


def list_numbers_near_a_symbol(number_dict, symbol_list):
    output = []
    number_start = number_dict.get('start')
    number_end = number_dict.get('end')
    for symbol in symbol_list:
        symbol_start = symbol.get('start')
        symbol_end = symbol.get('end')
        check = (
            (number_start <= symbol_start <= number_end)
            or
            (number_start <= symbol_end <= number_end)
        )
        if check:
            output.append(number_dict)
    return output


def get_symbols(line_num, list_of_lines):
    current = find_symbols(list_of_lines[line_num])
    max_line_n = len(list_of_lines)-1
    next_line = []
    previous_line = []
    if line_num < max_line_n:
        next_line = find_symbols(list_of_lines[line_num+1])
    if line_num > 0:
        previous_line = find_symbols(list_of_lines[line_num-1])
    return current+next_line+previous_line


def find_gear(input_string: str):
    pattern = r'\*'
    search_results = re.finditer(pattern, input_string)
    output = []
    for i in search_results:
        output.append(
            dict(
                value=i.group(0),
                start=i.span()[0],
                end=i.span()[1]
            )
        )
    return output


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()

    engine_parts = []
    for idx, line in enumerate(lines):
        print('line', idx, ':', line)
        numbers = find_numbers(line)
        if numbers:
            symbols = get_symbols(idx, lines)
            for number in numbers:
                engine_parts += list_numbers_near_a_symbol(number, symbols)
    engine_part_numbers = [int(engine_part.get('value')) for engine_part in engine_parts]
    print('sum_of_engine_pars_near_symbols:', sum(engine_part_numbers))
    sum_2 = 0
    for idx, line in enumerate(lines):
        gears = find_gear(line)
        if gears:
            numbers = find_numbers(line) + find_numbers(lines[idx - 1]) + find_numbers(lines[idx + 1])
            for gear in gears:
                parts_connected_to_gear = get_numbers_near_a_gear(gear, numbers)
                if len(parts_connected_to_gear) == 2:
                    gear_ratio = (
                            int(parts_connected_to_gear[0].get('value'))
                            * int(parts_connected_to_gear[1].get('value'))
                    )
                    sum_2 += gear_ratio
    print('sum_of_gear_ratios:', sum_2)
