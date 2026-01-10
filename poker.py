import random
from collections import Counter

def prepare_deck():
    figures = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    colors = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    #deck = [ ['2', 'Hearts'], ['2', 'Diamonds'], ['2', 'Clubs'], ['2', 'Spades'],
    deck = []

    for figure in figures:
        for color in colors:
            deck.append([figure, color])
    return deck


def deal_hands(deck,players,hand_size=5):
    random.shuffle(deck)
    for player in players:
        players[player]=deck[:hand_size]
        del deck[:hand_size]
    return players
    #return random.sample(deck, hand_size)


def count_hand_figures(hand):
    hand_figures = []
    for card in hand:
        hand_figures.append(card[0])
    counted_figures = Counter(hand_figures)
    return counted_figures


def is_pair(hand):
    counted_figures = count_hand_figures(hand)
    if len(counted_figures) == 4:
        return True
    return False


def is_two_pair(hand):
    counted_figures = count_hand_figures(hand)
    if sorted(counted_figures.values()) == [1,2,2]:
        return True
    return False


def is_three_of_a_kind(hand):
    counted_figures = count_hand_figures(hand)
    if sorted(counted_figures.values()) == [1,1,3]:
        return True
    return False


def is_four_of_a_kind(hand):
    counted_figures = count_hand_figures(hand)
    if sorted(counted_figures.values()) == [1,4]:
        return True
    return False


def count_hand_colors(hand):
    hand_colors = []
    for card in hand:
        hand_colors.append(card[1])
    counted_colors = Counter(hand_colors)
    return counted_colors


def is_flush(hand):
    counted_colors = count_hand_colors(hand)
    if len(counted_colors) == 1:
        return True
    return False


def is_full(hand):
    counted_figures = count_hand_figures(hand)
    if sorted(counted_figures.values()) == [2,3]:
        return True
    return False


def mapped_hand_figures(hand):
     
    hand_figures = []
    for card in hand:
        hand_figures.append(card[0])

    mapping = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':11, 'Q':12, 'K':13, 'A':14}
    
    mapped_hand_figures = []
    for card in hand_figures:
        mapped_hand_figures.append(mapping[card])
    return mapped_hand_figures


def is_strit(hand):

    mapped_hand = mapped_hand_figures(hand)
    sorted_cards = sorted(mapped_hand)
    
    strit_range = list(range(sorted_cards[0], sorted_cards[0]+5))
    if sorted_cards == strit_range:
        return True
    return False


def is_poker(hand):
    
    flush = is_flush(hand)
    mapped_hand = mapped_hand_figures(hand)

    sorted_cards = sorted(mapped_hand)
    
    strit_range = list(range(sorted_cards[0], sorted_cards[0]+5))
    if sorted_cards == strit_range and flush is True:
        return True
    return False


def is_royal_flush(hand):
   
    flush = is_flush(hand)
    mapped_hand = mapped_hand_figures(hand)

    sorted_cards = sorted(mapped_hand)
    
    strit_range = list(range(sorted_cards[0], sorted_cards[0]+5))
    if (sorted_cards == strit_range and sorted_cards[0] == 10) and flush is True:
        return True
    return False

def evaluate_hand(hand):
    if is_royal_flush(hand): return 10
    if is_poker(hand): return 9
    if is_four_of_a_kind(hand): return 8
    if is_full(hand): return 7
    if is_flush(hand): return 6
    if is_strit(hand): return 5
    if is_three_of_a_kind(hand): return 4
    if is_two_pair(hand): return 3
    if is_pair(hand): return 2
    return 1 

def determine_winner(users_cards):
    scores = {}
    for player_name, deck in users_cards.items():
        scores[player_name] = evaluate_hand(deck)

    player1_name, player2_name = list(scores.keys())
    score1, score2 = scores[player1_name], scores[player2_name]

    if score1 > score2:
        return f"Wygrał: {player1_name}"
    elif score2 > score1:
        return f"Wygrał: {player2_name}"
    else:
        return "Remis"

def main():
    deck = prepare_deck()

    players = {
        "Gracz_1": [],
        "Gracz_2": [],
    }

    users_cards =  deal_hands(deck, players)
    print(users_cards)
    #cards_hand = deal_hands(deck)
    #cards_hand = [['J', 'Hearts'], ['Q', 'Hearts'], ['K', 'Hearts'], ['A', 'Hearts'], ['10', 'Hearts']]

    for players, cards_hand in users_cards.items():
        

        if is_royal_flush(cards_hand) is True:
            print("Poker królewski")
        elif is_poker(cards_hand) is True:
            print("Poker")
        elif is_strit(cards_hand) is True:
            print("Strit")
        elif is_flush(cards_hand) is True:
            print("Kolor")
        elif is_four_of_a_kind(cards_hand) is True:
            print("Kareta")
        elif is_full(cards_hand) is True:
            print("Full")
        elif is_three_of_a_kind(cards_hand) is True:
            print("Trójka")
        elif is_two_pair(cards_hand) is True:
            print("Dwie pary")
        elif is_pair(cards_hand) is True:
            print("Para")
        else:
            print("Wysoka karta")
        print(f"Karty w tali: {cards_hand}")

    result = determine_winner(users_cards)
    print(result)


if __name__ == "__main__":
    main()