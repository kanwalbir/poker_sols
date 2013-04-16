#-----------------------------------------------------------------------------#
#                            PACKAGE AND MODULE IMPORTS                       #
#-----------------------------------------------------------------------------#

"""
Other Python file imports.
"""
from create_deck import create_deck
from deal import deal_cards
from wild_hand import best_wild_hand

#-----------------------------------------------------------------------------#
"""
Check if the cards have been provided beforehand. If not, then create a deck 
of cards and let the system deal some cards to the players. Find the rank of 
every hand and print out some information about the hand. Determine the 
winner of the poker match.

Args: (i)   Dealt hand (optional) - if absent, system will deal cards
      (ii)  Number of players (optional) -  default is 4 players
      (iii) Deck of cards (optional) - default is 'standard' 52 deck
                                     - or 'joker' which adds 2 jokers to 'standard'
                                     - see create_deck.py for more details

Returns: (i) Winner of the poker round
"""
def poker(deal=[], num_players=4, deck='standard'):
    if deal:
        newdeal = deal
    else:
        if num_players > 10: # Maximum 10 players can play using 1 deck of cards
            num_players = 10
        mydeck = create_deck(deck)
        newdeal = deal_cards(mydeck, num_players, 5)

    print '\n', 'Following hands were dealt:'
    poker_results, winner, max_value, i = {}, [], (), 0

    for hand in newdeal:
        poker_results[i] = [hand, best_wild_hand(hand)]
        print poker_results[i][0], '---->', poker_results[i][1][1]

        if poker_results[i][1][0] > max_value:
            max_value = poker_results[i][1][0]
            winner = [poker_results[i][0]]
            win_type = poker_results[i][1][1]
        elif poker_results[i][1][0] == max_value:
            if poker_results[i][0] not in winner:
                winner += [poker_results[i][0]]
        i += 1

    if len(winner) == 1:
        winner = winner[0]
    print '\n', 'The winner is:', winner, '---->', win_type
    print '---------------------------------------------------------------'
    return winner

#-----------------------------------------------------------------------------#
"""
Test values and assert statements for above function.
"""
def test1():
    sf =  ['6C', '7C', '8C', '9C', 'TC'] # Straight Flush
    fk =  ['9C', '9D', '9H', '9S', '7D'] # Four of a Kind
    fh =  ['TC', 'TD', 'TH', '7C', '7D'] # Full House
    sf1 = ['6C', '7C', '8C', '9C', 'TC'] # Straight Flush
    sf2 = ['6D', '7D', '8D', '9D', 'TD'] # Straight Flush
    sf3 = ['6S', '7S', '8S', '9S', 'TS'] # Straight Flush
    assert poker([sf] + 99*[fh]) == sf
    assert poker([sf, fk, fh]) == sf
    assert poker([fk, fh]) == fk
    assert poker([fh, fh]) == fh
    assert poker([sf]) == sf
    assert poker([sf1, sf2, fk, fh]) == [sf1, sf2]
    assert poker([sf1, sf2, sf3, fk, fh]) == [sf1, sf2, sf3]
    return 'All Tests 1 Passed'

def test2():
    bj1 = ['7C', '8C', '9D', 'TD', '?B'] # Straight
    rj1 = ['7C', '8C', '9D', 'TD', '?R'] # Straight
    brj1 = ['TC', 'TD', '7C', '?R', '?B'] # Four of a Kind
    assert poker([bj1, rj1, brj1]) == brj1
    return 'All Tests 2 Passed'

print poker()
print poker([])
print poker([], 2)
print poker([], 8, 'standard')
print poker([], 8, 'joker')
print poker([], 11, 'standard')
print test1()
print test2()

#-----------------------------------------------------------------------------#
