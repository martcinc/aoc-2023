import re
import math


def get_big_fat_race(line_list):
    time_str = line_list[0].split(':')[1].replace(' ', '')
    distance_str = line_list[1].split(':')[1].replace(' ', '')
    times = int(time_str)
    distances = int(distance_str)
    return {times: distances}


def get_races(line_list):
    time_str = line_list[0]
    distance_str = line_list[1]
    pattern = r'([0-9]+)'
    times = list(map(int, re.findall(pattern, time_str)))
    distances = list(map(int, re.findall(pattern, distance_str)))
    return dict(zip(times, distances))


def get_ways(race_time, race_distance):
    speed = math.ceil(race_distance / race_time)

    ways = 0
    race_time = race_time - speed
    for i in range(0, race_time):
        if speed * race_time > race_distance:
            ways += 1
        elif ways > 0 and speed * race_time < race_distance:
            break
        # print('try', i, 'speed', speed, 'time', race_time, speed * race_time, speed * race_time > race_distance, ways)
        speed += 1
        race_time -= 1
    return ways


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()

    times_distances = get_races(lines)
    # pt 1
    print(times_distances)
    ways_to_beat_record = 1
    for time, distance in times_distances.items():
        ways_to_beat_record *= get_ways(time, distance)
    print('ways_to_beat_record:', ways_to_beat_record)

    times_distances = get_big_fat_race(lines)
    # pt 2
    print(times_distances)
    ways_to_beat_record = 1
    for time, distance in times_distances.items():
        ways_to_beat_record *= get_ways(time, distance)
    print('ways_to_beat_record_pt2:', ways_to_beat_record)
