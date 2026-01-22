import poker
import pytest

def test_count_hand_figures():
    hand = [['J', 'Hearts'], ['Q', 'Hearts'], ['K', 'Hearts'], ['A', 'Hearts'], ['10', 'Hearts']]
    result = poker.count_hand_figures(hand)
    assert result == {'10': 1, 'A': 1, 'J': 1, 'K': 1, 'Q': 1}

def test_is_pair():
    hand = [['J', 'Hearts'], ['J', 'Hearts'], ['K', 'Hearts'], ['A', 'Hearts'], ['10', 'Hearts']]
    result = poker.is_pair(hand)
    assert result is True

def test_is_two_pair():
    hand = [['J', 'Hearts'], ['J', 'Clubs'], ['K', 'Hearts'], ['K', 'Clubs'], ['6', 'Spades']]
    result = poker.is_two_pair(hand)
    assert result is True

def test_is_three_of_a_kind():
    hand = [['J', 'Hearts'], ['J', 'Clubs'], ['10', 'Hearts'], ['K', 'Clubs'], ['J', 'Spades']]
    result = poker.is_three_of_a_kind(hand)
    assert result is True

def test_is_four_of_a_kind():
    hand =  [['J', 'Hearts'], ['J', 'Clubs'], ['J', 'Diamonds'], ['5', 'Clubs'], ['J', 'Spades']]
    result = poker.is_four_of_a_kind(hand)
    assert result is True

def test_count_hand_colors():
    hand = [['J', 'Hearts'], ['J', 'Hearts'], ['K', 'Hearts'], ['A', 'Hearts'], ['10', 'Hearts']]
    result = poker.count_hand_colors(hand)
    assert result == {'Hearts': 5}

def test_is_flush():
    hand = [['2', 'Hearts'], ['5', 'Hearts'], ['K', 'Hearts'], ['A', 'Hearts'], ['10', 'Hearts']]
    result = poker.is_flush(hand)
    assert result is True

def test_is_full():
    hand =  [['2', 'Hearts'], ['2', 'Clubs'], ['2', 'Diamonds'], ['5', 'Clubs'], ['5', 'Spades']]
    result = poker.is_full(hand)
    assert result is True

def test_mapped_hand_figure():
    hand = [['5', 'Hearts'], ['6', 'Hearts'], ['7', 'Hearts'], ['8', 'Hearts'], ['9', 'Hearts']]
    result = poker.mapped_hand_figures(hand)
    assert result == [5, 6, 7, 8, 9]

def test_is_strit():
    hand = [['5', 'Hearts'], ['6', 'Hearts'], ['7', 'Hearts'], ['8', 'Hearts'], ['9', 'Hearts']]
    result = poker.is_strit(hand)
    assert result is True

def test_is_poker():
    hand = [['7', 'Hearts'], ['8', 'Hearts'], ['9', 'Hearts'], ['10', 'Hearts'], ['J', 'Hearts']]
    result = poker.is_poker(hand)
    assert result is True

def test_is_royal_flush():
    hand = [['10', 'Hearts'], ['J', 'Hearts'], ['Q', 'Hearts'], ['K', 'Hearts'], ['A', 'Hearts']]
    result = poker.is_royal_flush(hand)
    assert result is True

def test_evaluate_hand():
    hand = [['10', 'Hearts'], ['J', 'Hearts'], ['Q', 'Hearts'], ['K', 'Hearts'], ['A', 'Hearts']]
    result = poker.evaluate_hand(hand)
    assert result == [10]

