

def line_to_ints(line_of_nums):
    return list(map(int, line_of_nums.split(' ')))


def number_diffs(nums):
    out =[]
    for idx, val in enumerate(nums):
        if idx > 0:
            out.append(val - nums[idx-1])
    return out


def all_zeros(nums):
    return all(
        list(map(lambda x: x == 0, nums))
    )


def sum_last_numbers(list_of_lists):
    out = 0
    for list in list_of_lists:
        out += list[-1]
    return out


def get_first_number(list_of_lists):
    n = 0
    for i in reversed(list_of_lists):
        first_num = i[0]
        new_val = first_num - n
        n = new_val
        # print(first_num, new_val)
    return new_val

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()

    sum_of_extrapolated_vals = 0
    for line in lines:
        readings = line_to_ints(line)
        diffs = number_diffs(readings)
        sequences=[]
        while not all_zeros(diffs):
            sequences.append(diffs)
            diffs = number_diffs(diffs)
        sum_of_diffs = sum_last_numbers(sequences)
        extrapolated_value = readings[-1] + sum_of_diffs
        print(
            readings, '->', sequences, '->', sum_of_diffs,
            '==>', extrapolated_value
        )
        sum_of_extrapolated_vals += extrapolated_value
    print(sum_of_extrapolated_vals)
    sum_first_nums = 0
    for line in lines:
        # print(line)
        readings = line_to_ints(line)
        diffs = number_diffs(readings)
        sequences = []
        while not all_zeros(diffs):
            sequences.append(diffs)
            diffs = number_diffs(diffs)
        sequences.insert(0, readings)
        # print(sequences)
        # print(get_first_number(sequences))
        sum_first_nums += get_first_number(sequences)
    print('result', sum_first_nums)
