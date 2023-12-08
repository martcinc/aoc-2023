

def translate_cards(card_string, handle_jokers=False):
    d = dict(
        A='14', K='13', Q='12', J='11', T='10',
    )
    if handle_jokers:
        d['J'] = '1'
    card_list = []
    for card in card_string:
        card_list.append(d.get(card, card))
    card_list = list(map(int, card_list))
    return card_list


def get_hand_value(card_list):
    card_list = reversed(card_list)
    val = 0
    for card_index, card in enumerate(card_list):
        val += card * (16**card_index)
    return val


def whats_in_hand(card_list):
    val = 0
    jokers = len([i for i in card_list if i == 1])
    non_jokers = [i for i in card_list if i != 1]
    counter = {i: non_jokers.count(i) for i in non_jokers}
    values = list(counter.values())
    pairs = [2 for i in values if i == 2]
    if values:
        mx = max(values)
    else:
        mx = 0
    if mx + jokers == 5:
        hand_type = 'five'
        val = 1000000000
    elif (mx + jokers) == 4:
        hand_type = 'four'
        val = 100000000
    elif (3 in values and 2 in values) or (len(pairs) == 2 and jokers == 1):
        hand_type = 'full'
        val = 70000000
    elif mx + jokers == 3:
        hand_type = 'three'
        val = 50000000
    elif len(pairs) == 2:
        hand_type = 'two pairs'
        val = 30000000
    elif mx + jokers == 2:
        hand_type = 'pair'
        val = 20000000
    else:
        hand_type = 'nothing'
    return val + get_hand_value(card_list), hand_type


def get_total_winnings(list_of_lines, handle_jokers):
    out = []
    for line in list_of_lines:
        hand, bet = line.split(' ')
        cards = translate_cards(hand, handle_jokers=handle_jokers)
        hand_value, typ = whats_in_hand(cards)
        out.append(
            dict(
                hand=hand,
                bet=bet,
                hand_value=hand_value,
                typ=typ
            )
        )
    nl = sorted(out, key=lambda x: x['hand_value'])
    sum_winnings = 0
    score_list = []
    for idx, entry in enumerate(nl):
        rank = idx + 1
        score = rank * int(entry.get('bet'))
        sum_winnings += score
        score_list.append(score)
        # print(entry.get('hand'), entry.get('typ'), entry.get('bet'), rank)
    return sum_winnings


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()
    print('part 1 winnings:', get_total_winnings(lines, handle_jokers=False))
    print('part 2 winnings:', get_total_winnings(lines, handle_jokers=True))
