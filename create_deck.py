#-----------------------------------------------------------------------------#
"""
Create a deck of cards depending on the following requirements:
- black cards only (26 cards - Clubs, Spades)
- red cards only (26 cards - Diamonds, Hearts)
- standard deck (52 cards - Clubs, Diamonds, Hearts, Spades)
- joker deck (54 cards - standard deck + black joker + red joker)

Args: (i) Type of deck that is needed

Returns: (i) Deck of cards in list format
"""

def create_deck(x='standard'):
    allranks = '23456789TJQKA'

    if str(x).lower() == 'black':
        return [r+s for r in allranks for s in 'CS']
    elif str(x).lower() == 'red':
        return [r+s for r in allranks for s in 'DH']
    elif str(x).lower() == 'standard':
        return [r+s for r in allranks for s in 'CDHS']
    elif str(x).lower() == 'joker':
        return [r+s for r in allranks for s in 'CDHS'] + ['?B', '?R']
    else:
        return [r+s for r in allranks for s in 'CDHS']

#-----------------------------------------------------------------------------#
"""
Test values and assert statements for above functions.
"""
"""
assert create_deck('black') == ['2C', '2S', '3C', '3S', '4C', '4S', '5C', '5S', '6C', '6S', 
                                '7C', '7S', '8C', '8S', '9C', '9S', 'TC', 'TS', 'JC', 'JS', 
                                'QC', 'QS', 'KC', 'KS', 'AC', 'AS']

assert create_deck('red') == ['2D', '2H', '3D', '3H', '4D', '4H', '5D', '5H', '6D', '6H', 
                              '7D', '7H', '8D', '8H', '9D', '9H', 'TD', 'TH', 'JD', 'JH', 
                              'QD', 'QH', 'KD', 'KH', 'AD', 'AH']

assert create_deck('standard') == ['2C', '2D', '2H', '2S', '3C', '3D', '3H', '3S', 
                                   '4C', '4D', '4H', '4S', '5C', '5D', '5H', '5S', 
                                   '6C', '6D', '6H', '6S', '7C', '7D', '7H', '7S', 
                                   '8C', '8D', '8H', '8S', '9C', '9D', '9H', '9S', 
                                   'TC', 'TD', 'TH', 'TS', 'JC', 'JD', 'JH', 'JS', 
                                   'QC', 'QD', 'QH', 'QS', 'KC', 'KD', 'KH', 'KS', 
                                   'AC', 'AD', 'AH', 'AS']

assert create_deck('joker') == ['2C', '2D', '2H', '2S', '3C', '3D', '3H', '3S', 
                                '4C', '4D', '4H', '4S', '5C', '5D', '5H', '5S', 
                                '6C', '6D', '6H', '6S', '7C', '7D', '7H', '7S', 
                                '8C', '8D', '8H', '8S', '9C', '9D', '9H', '9S', 
                                'TC', 'TD', 'TH', 'TS', 'JC', 'JD', 'JH', 'JS', 
                                'QC', 'QD', 'QH', 'QS', 'KC', 'KD', 'KH', 'KS', 
                                'AC', 'AD', 'AH', 'AS', '?B', '?R']

assert create_deck() == ['2C', '2D', '2H', '2S', '3C', '3D', '3H', '3S', 
                         '4C', '4D', '4H', '4S', '5C', '5D', '5H', '5S', 
                         '6C', '6D', '6H', '6S', '7C', '7D', '7H', '7S', 
                         '8C', '8D', '8H', '8S', '9C', '9D', '9H', '9S', 
                         'TC', 'TD', 'TH', 'TS', 'JC', 'JD', 'JH', 'JS', 
                         'QC', 'QD', 'QH', 'QS', 'KC', 'KD', 'KH', 'KS', 
                         'AC', 'AD', 'AH', 'AS']

print create_deck('black'), '\n'
print create_deck('red'), '\n'
print create_deck('standard'), '\n'
print create_deck('joker'), '\n'
print create_deck(), '\n'
"""

#-----------------------------------------------------------------------------#
