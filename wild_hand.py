#-----------------------------------------------------------------------------#
#                            PACKAGE AND MODULE IMPORTS                       #
#-----------------------------------------------------------------------------#

"""
Other Python file imports.
"""
from create_deck import create_deck
from hand_rank import calculate_hand_rank

#-----------------------------------------------------------------------------#
"""
Module designed to handle Joker cards. If no joker cards exist in hand, then 
calculate the rank of the hand straightaway. Else, calculate the ranks of all 
possible joker relacement combinations and output the max of it.

Args: (i) Hand of cards

Returns: (i) Rank of hand, type of hand and related information in a tuple format
             (see hand_rank.py for more information)
"""

def best_wild_hand(hand):
    
    if '?B' in hand or '?R' in hand:
        all_combos = joker_combo(hand[:]) # Send a copy of the list to avoid mutation
        all_combos_ranks = [calculate_hand_rank(a) for a in all_combos]
        return max(all_combos_ranks)
    else:
        return calculate_hand_rank(hand)

#-----------------------------------------------------------------------------#
"""
Replace red joker with red cards only (Diamonds + Hearts) and replace black 
joker with black cards only (Clubs + Spades). Don't replace joker with a card 
that already exists in the hand. Replacements happen in one of three ways:
- Replace both black and red joker (if both jokers exist in hand)
- Replace black joker only
- Replace red joker only

Args: (i) Hand of cards

Returns: (i) Joker replacement combinations in list format
"""

def joker_combo(hand):
    hand = hand[:]
    b_joker_deck, r_joker_deck = create_deck('black'), create_deck('red')
    all_combos = []

    if '?B' in hand and '?R' in hand: # Hand has both red joker and black joker
        hand.remove('?B')
        hand.remove('?R')
        for b in b_joker_deck:
            for r in r_joker_deck:
                # Can't replace joker with a card that already exists in the hand, like ['2H', '2H']
                if b not in hand and r not in hand:
                    all_combos += [hand + [b] + [r]]
    else:
        if '?B' in hand: # Hand has only black joker
            joker_deck = b_joker_deck
            hand.remove('?B')
        elif '?R' in hand: # Hand has only red joker
            joker_deck = r_joker_deck
            hand.remove('?R')

        for j in joker_deck:
            if j not in hand: # Can't replace joker with a card that already exists in the hand
                all_combos += [hand + [j]]
    return all_combos

#-----------------------------------------------------------------------------#
"""
Test values and assert statements for above function.
"""
"""
def wild_hand_test():
    bj1 = ['7C', '8C', '9D', 'TD', '?B'] # Straight
    rj1 = ['7C', '8C', '9D', 'TD', '?R'] # Straight
    brj1 = ['TC', 'TD', '7C', '?R', '?B'] # Four of a Kind
    print best_wild_hand(bj1)
    print best_wild_hand(rj1)
    print best_wild_hand(brj1)

    assert best_wild_hand(bj1)[0][0] == 4
    assert best_wild_hand(rj1)[0][0] == 4
    assert best_wild_hand(brj1)[0][0] == 7
    return 'All Tests Passed'

print wild_hand_test()
"""

#-----------------------------------------------------------------------------#