import re


def txt_to_digit(digit_string):
    digit_dict = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    return digit_dict.get(digit_string, digit_string)


def line_to_list_digits(txt_line: str, match_also_words=False) -> list[str]:
    pattern = r'([0-9])'
    if match_also_words:
        pattern = r'(?=([0-9]|one|two|three|four|five|six|seven|eight|nine))'
    output = re.findall(pattern, txt_line)
    return output


def list_to_int(list_of_digits: list) -> int:
    return int(f"{list_of_digits[0]}{list_of_digits[-1]}")


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()
    # pt 1
    sum_calibration_value = 0
    for idx, line in enumerate(lines):
        digits = line_to_list_digits(line)
        list_of_ints = list(map(txt_to_digit, digits))
        calibration_value = list_to_int(list_of_ints)
        # print(line, '->', list_of_ints, '->', calibration_value)
        sum_calibration_value += calibration_value
    print('sum_calibration_value pt1:', sum_calibration_value)
    # pt 2
    sum_calibration_value = 0
    for idx, line in enumerate(lines):
        digits = line_to_list_digits(line, match_also_words=True)
        list_of_ints = list(map(txt_to_digit, digits))
        calibration_value = list_to_int(list_of_ints)
        # print(line, '->', list_of_ints, '->', calibration_value)
        sum_calibration_value += calibration_value
    #     print(line, '->', list_ints, '->', calibration_value)
    print('sum_calibration_value pt2:', sum_calibration_value)
