import random

def play_game(seed_number):
    cards = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
    suits = ['\u2665', '\u2666', '\u2663', '\u2660']
    deck = [str(card) + suit for suit in suits for card in cards]

    card_images = ["\U0001F0B1","\U0001F0B2","\U0001F0B3","\U0001F0B4", \
                   "\U0001F0B5","\U0001F0B6","\U0001F0B7","\U0001F0B8", \
                   "\U0001F0B9","\U0001F0BA","\U0001F0BB","\U0001F0BD","\U0001F0BE", \
                   "\U0001F0C1","\U0001F0C2","\U0001F0C3","\U0001F0C4", \
                   "\U0001F0C5","\U0001F0C6","\U0001F0C7","\U0001F0C8", \
                   "\U0001F0C9","\U0001F0CA","\U0001F0CB","\U0001F0CD","\U0001F0CE", \
                    "\U0001F0D1","\U0001F0D2","\U0001F0D3","\U0001F0D4", \
                   "\U0001F0D5","\U0001F0D6","\U0001F0D7","\U0001F0D8", \
                   "\U0001F0D9","\U0001F0DA","\U0001F0DB","\U0001F0DD","\U0001F0DE", \
                   "\U0001F0A1","\U0001F0A2","\U0001F0A3","\U0001F0A4", \
                   "\U0001F0A5","\U0001F0A6","\U0001F0A7","\U0001F0A8", \
                   "\U0001F0A9","\U0001F0AA","\U0001F0AB","\U0001F0AD","\U0001F0AE"]
    
    suits = ['\u2666', '\u2663', '\u2660', '\u2665']
    modified_deck = [str(card) + suit for suit in suits for card in cards]
                   
    card_to_image = {}
    card_to_value = {}
    for i in range(len(deck)):
        card = deck[i]
        card_to_image[card] = card_images[i] 
        if card[0].isdigit() and not card[1].isdigit():
            card_to_value[card] = int(card[0])
        elif card[0] == '1' and card[1] == '0':
            card_to_value[card] = 10
        elif card[0] == 'J':
            card_to_value[card] = 11
        elif card[0] == 'Q': 
            card_to_value[card] = 12
        elif card[0] == 'K': 
            card_to_value[card] = 13
        else:
            card_to_value[card] = 1

    remaining_cards = [card for card in deck if card_to_value[card] != 7]

    diamonds = ['7' + '\u2666']
    clubs = ['7' + '\u2663']
    spades = ['7' + '\u2660']
    hearts = ['7' + '\u2665']
    placed_cards = diamonds + clubs + spades + hearts

    random.seed(seed_number)
    random.shuffle(remaining_cards)

    lines = []

    # Begin game

    lines.append('All 7s removed and placed, rest of deck shuffled, ready to start!')
    lines.append(']' * 48)
    lines.append('')
    state = []
    for _ in range(6):
        state.append('')
    state.append('\t' + card_to_image[diamonds[0]] + \
                 '\t' + card_to_image[clubs[0]] + \
                 '\t' + card_to_image[spades[0]] + \
                 '\t' + card_to_image[hearts[0]])
    for _ in range(7):
        state.append('')
    lines.extend(state)
    
    for i in range(3):
        cards_aside = []
        if i == 0:
            lines.append('Starting first round...')  
        elif i == 1:
            lines.append('')
            lines.append('Starting second round...')
        else:
            lines.append('')
            lines.append('Starting third round...')
        lines.append('')

        while remaining_cards:
            next_card = remaining_cards.pop(-1)
            if next_card[-1] == '\u2666':
                suit = diamonds
            elif next_card[-1] == '\u2663':
                suit = clubs
            elif next_card[-1] == '\u2660':
                suit = spades
            elif next_card[-1] == '\u2665':
                suit = hearts
            same_number_cards = [card for card in modified_deck if card_to_value[card] == card_to_value[next_card]]
            maximum = max(card_to_value[card] for card in suit)
            minimum = min(card_to_value[card] for card in suit)
            if card_to_value[next_card] == maximum + 1 or card_to_value[next_card] == minimum - 1:
                suit.append(next_card)
                placed_cards.append(next_card)
                lines.append('Placing card from top of stack of cards left ' + '😊️')
                lines.append(']' * len(remaining_cards))
                if cards_aside:
                    lines.append('[' * (len(cards_aside) - 1) + card_to_image[cards_aside[-1]])
                else:
                    lines.append('')
                filtered_cards = [card_to_image[card] if card in placed_cards else '' for card in same_number_cards]
                state = state[:(13 - card_to_value[next_card])] + ['\t' + '\t'.join(filtered_cards)] + \
                        state[(14 - card_to_value[next_card]):]
                lines.extend(state)
                if cards_aside:
                    aside_card = cards_aside[-1]
                    if aside_card[-1] == '\u2666':
                        suit = diamonds
                    elif aside_card[-1] == '\u2663':
                        suit = clubs
                    elif aside_card[-1] == '\u2660':
                        suit = spades
                    elif aside_card[-1] == '\u2665':
                        suit = hearts
                    maximum = max(card_to_value[card] for card in suit)
                    minimum = min(card_to_value[card] for card in suit)
                    while card_to_value[aside_card] == maximum + 1 or card_to_value[aside_card] == minimum - 1:
                        cards_aside.pop(-1)
                        suit.append(aside_card)
                        placed_cards.append(aside_card)
                        lines.append('Placing card from top of stack of cards put aside ' + '😊️')
                        lines.append(']' * len(remaining_cards))
                        if cards_aside:
                            lines.append('[' * (len(cards_aside) - 1) + card_to_image[cards_aside[-1]])
                        else:
                            lines.append('')
                        same_number_cards = [card for card in modified_deck if card_to_value[card] == card_to_value[aside_card]]
                        filtered_cards = [card_to_image[card] if card in placed_cards else '' for card in same_number_cards]
                        state = state[:(13 - card_to_value[aside_card])] + ['\t' + '\t'.join(filtered_cards)] + \
                                state[(14 - card_to_value[aside_card]):]
                        lines.extend(state)
                        try:
                            aside_card = cards_aside[-1]
                        except IndexError:
                            break
                        if aside_card[-1] == '\u2666':
                            suit = diamonds
                        elif aside_card[-1] == '\u2663':
                            suit = clubs
                        elif aside_card[-1] == '\u2660':
                            suit = spades
                        elif aside_card[-1] == '\u2665':
                            suit = hearts
                        maximum = max(card_to_value[card] for card in suit)
                        minimum = min(card_to_value[card] for card in suit)
                    else:
                        lines.append('Cannot place card from top of stack of cards put aside ' + '☹️')
                        lines.append('')
                else:
                    pass
            else:
                cards_aside.append(next_card)
                lines.append('Cannot place card from top of stack of cards left ' + '☹️')
                lines.append(']' * len(remaining_cards))
                if cards_aside:
                    lines.append('[' * (len(cards_aside) - 1) + card_to_image[cards_aside[-1]])
                else:
                    lines.append('')
                lines.append('')

        remaining_cards = cards_aside[::-1]

    if remaining_cards:
        lines.append(f'You could not place {len(remaining_cards)} cards, you lost ' + '\U0001F44E')
    else:
        lines.append('You placed all cards, you won ' + '\U0001F44D')

    lines = [line.rstrip() for line in lines]

    return lines, len(cards_aside)

def display_output(lines):
    total_lines = len(lines)

    print(f"There are {len(results)} lines of output; what do you want me to do?")

    while True:
        print("")
        print("Enter: q to quit")
        print(f"       a last line number (between 1 and {total_lines})")
        print(f"       a first line number (between -1 and -{total_lines})")
        print(f"       a range of line numbers (of the form m--n with 1 <= m <= n <= {total_lines})")  

        user_input = input("       ")

        if user_input.strip() == "q":
            break  

        elif (user_input.strip()).isdigit():
            n = int(user_input.strip())
            if 1 <= n <= total_lines:
                print("")
                print("\n".join(lines[:n]))  

        elif (user_input.strip()).startswith("-") and user_input[1:].isdigit():
            n = int(user_input)
            if -total_lines <= n <= -1:
                print("")
                print("\n".join(lines[n:]))

        elif "--" in user_input:
            user_input = user_input.replace(" ", "")
            m, n = map(int, user_input.split("--"))
            if 1 <= m <= n <= total_lines:
                print("")
                print("\n".join(lines[m-1:n])) 

def simulate(n, i):
    results = []
    seed_number = i
    for _ in range(n):
        results += [play_game(seed_number)[1]]
        seed_number += 1
    results.sort(reverse=True)
    results_set = list(dict.fromkeys(results))
    counts = []
    for result in results_set:
        counts.append(results.count(result))
    frequencies = [f'{count / n * 100:0.2f}%' for count in counts]
    print('Number of cards left | Frequency')
    print('-' * 32)
    for result, frequency in zip(results_set, frequencies):
        print(f'{result:>20}' + ' |' + f'{frequency:>10}')

if __name__ == '__main__':
    seed_number = int(input('Please enter an integer to feed the seed() function: '))
    results = play_game(seed_number)[0]
    print('')
    display_output(results)







