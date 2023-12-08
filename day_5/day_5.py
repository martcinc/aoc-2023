
def map_to_dict(entry):
    return dict(
        destination=entry[0],
        source_start=entry[1],
        source_end=entry[1] + entry[2] - 1,
        rng=entry[2],
        offset=entry[0] - entry[1]
    )


def traverse_map(list_of_lists, value):
    out = []
    for entry in list_of_lists:
        out.append(
            map_to_dict(entry)
        )
    for row in out:
        if row.get('source_start') <= value <= row.get('source_end'):
            return row.get('destination') + (value - row.get('source_start'))
    return value


def get_maps(fpath='input_test.txt'):
    with open(fpath, 'r') as f:
        lines = f.read().splitlines()
    seeds = [int(seed) for seed in lines[0].split(': ')[1].split(' ')]

    for idx, line in enumerate(lines):
        if line == 'seed-to-soil map:':
            seed_to_soil_idx = idx
        if line == 'soil-to-fertilizer map:':
            soil_to_fertilizer_idx = idx
        if line == 'fertilizer-to-water map:':
            fertilizer_to_water_idx = idx
        if line == 'water-to-light map:':
            water_to_light_idx = idx
        if line == 'light-to-temperature map:':
            light_to_temperature_idx = idx
        if line == 'temperature-to-humidity map:':
            temperature_to_humidity_idx = idx
        if line == 'humidity-to-location map:':
            humidity_to_location_idx = idx

    seed_to_soil = [
        list(map(int, line.split(' '))) for line in lines[seed_to_soil_idx+1:soil_to_fertilizer_idx-1]
    ]
    soil_to_fertilizer = [
        list(map(int, line.split(' ')))for line in lines[soil_to_fertilizer_idx + 1:fertilizer_to_water_idx - 1]
    ]
    fertilizer_to_water = [
        list(map(int, line.split(' '))) for line in lines[fertilizer_to_water_idx + 1:water_to_light_idx - 1]
    ]
    water_to_light = [
        list(map(int, line.split(' '))) for line in lines[water_to_light_idx + 1:light_to_temperature_idx - 1]
    ]
    light_to_temperature = [
        list(map(int, line.split(' '))) for line in lines[light_to_temperature_idx + 1:temperature_to_humidity_idx - 1]
    ]
    temperature_to_humidity = [
        list(map(int, line.split(' '))) for line in lines[temperature_to_humidity_idx + 1:humidity_to_location_idx - 1]
    ]
    humidity_to_location = [
        list(map(int, line.split(' '))) for line in lines[humidity_to_location_idx + 1: len(lines)]
    ]

    return (
        seeds,
        seed_to_soil,
        soil_to_fertilizer,
        fertilizer_to_water,
        water_to_light,
        light_to_temperature,
        temperature_to_humidity,
        humidity_to_location
    )


def get_ranges(seed_list):
    out = []
    for i in range(0, len(seed_list), 2):
        out.append([[seed_list[i], seed_list[i + 1] + seed_list[i]]])
    return out


if __name__ == '__main__':
    # pt 1
    (
        seeds,
        seed_to_soil,
        soil_to_fertilizer,
        fertilizer_to_water,
        water_to_light,
        light_to_temperature,
        temperature_to_humidity,
        humidity_to_location
    ) = get_maps(fpath='input.txt')
    maps = [
        seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light,
        light_to_temperature, temperature_to_humidity, humidity_to_location
    ]

    res = []
    for val in seeds:
        txt_output = str(val)
        for my_map in maps:
            val = traverse_map(my_map, val)
            txt_output += ' -> '+str(val)
        res.append(val)
    print('lowest_location_number', min(res))

    # pt 2

    locations = []
    seed_ranges = get_ranges(seeds)
    for ranges in seed_ranges:
        # print(ranges)
        results = []
        for my_map in maps:
            while ranges:
                start_range, end_range = ranges.pop()
                # print('my map', my_map)
                for row in my_map:
                    map_row = map_to_dict(row)
                    # print(map_row)
                    if map_row['source_end'] <= start_range or end_range <= map_row['source_start']:
                        continue
                    if start_range < map_row['source_start']:
                        ranges.append([start_range, map_row['source_start']])
                        # print('ranges', ranges)
                        start_range = map_row['source_start']
                        # print('start_range', start_range)
                    if map_row['source_end'] < end_range:
                        ranges.append([map_row['source_end'], end_range])
                        end_range = map_row['source_end']
                    results.append([start_range + map_row['offset'], end_range + map_row['offset']])
                    # print('results', results)
                    break
                else:
                    results.append([start_range, end_range])
                    # print('results', results)
            ranges = results
            results = []
        locations += ranges
    # print('locations', locations)
    print('lowest_location_number pt2', min(loc[0] for loc in locations))
