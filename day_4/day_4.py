

def get_matching_cards(winning_cards, my_cards):
    matching_cards = []
    for c in my_cards:
        if c in winning_cards:
            matching_cards.append(c)
    res = 0
    if matching_cards:
        res = 2 ** (len(matching_cards)-1)
    return matching_cards, res


def fetch_cards(card_number):
    winning_cards = cards.get(card_number).get('winning_cards')
    my_cards = cards.get(card_number).get('my_cards')
    matching_cards, r = get_matching_cards(winning_cards, my_cards)
    card_numbers = [i for i in range(card_number+1, len(matching_cards)+card_number+1)]
    return card_numbers, r


def prepare_file(file_path='input.txt'):
    output = {}
    with open(file_path, 'r') as f:
        lines = f.read().splitlines()
    for idx, line in enumerate(lines):
        card_number, card_sets = line.split(': ')
        winning_cards, my_cards = card_sets.split(' | ')
        winning_cards = [int(c) for c in winning_cards.split(' ') if c]
        my_cards = [int(c) for c in my_cards.split(' ') if c]
        output[idx+1] = dict(
            winning_cards=winning_cards,
            my_cards=my_cards
        )
    return output


if __name__ == '__main__':

    sum_1 = 0
    sum_2 = 0
    cards = prepare_file('input.txt')

    # part 1
    for card in cards:
        new_cards, score = fetch_cards(card)
        sum_1 += score
    print('points_in_total', sum_1)

    # part 2
    card_list = list(cards.keys())
    for card in card_list:
        new_cards, score = fetch_cards(card)
        card_list += new_cards
    sum_2 = len(card_list)
    print('scratchcards in total', sum_2)
