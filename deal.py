#-----------------------------------------------------------------------------#
#                            PACKAGE AND MODULE IMPORTS                       #
#-----------------------------------------------------------------------------#

"""
Random module import
"""
import random

#-----------------------------------------------------------------------------#
"""
Shuffle the deck of cards and then deal out the hand to all the players.

Args: (i)   Deck of cards in list format
      (ii)  Number of cards in a hand (poker standard is 5)
      (iii) Number of players in the game

Returns: (i) Dealt cards in list format
"""
def deal_cards(deck, p, n=5):
    random.shuffle(deck)
    dealt_cards = []

    for i in range(p):
        a = i*n
        b = (i+1)*n
        dealt_cards.append(deck[a:b])
    return dealt_cards

#-----------------------------------------------------------------------------#
"""
Test values and assert statements for above functions.
"""
"""
deck = [r+s for r in '23456789TJQKA' for s in 'SHDC']
num_cards = 5
num_players = 4

print deal_cards(deck, num_players, num_cards)
assert len(deal_cards(deck, num_players, num_cards)) == num_players
"""

#-----------------------------------------------------------------------------#