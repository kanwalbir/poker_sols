#-----------------------------------------------------------------------------#
"""
Seperate the ranks and suits of a hand. Then, determine the type of hand and 
calculate its hand rank based on the following:
- Straight Flush = Straight + Flush --> 8
- Four of a kind --> 7
- Full House = Three of a kind + Two of a kind --> 6
- Flush =  All same suits --> 5
- Straight = Ordered straight ranks --> 4
- Three of a kind --> 3
- Two Pairs = Two, two of a kind --> 2
- Two of a kind or One pair --> 1
- High Card --> 0

Args: (i) Hand of cards

Returns: (i) Rank of hand, type of hand and related information in a tuple format
"""
def calculate_hand_rank(hand):
    ranks = card_ranks(hand)
    suits = [s for r,s in hand]

    if flush(suits) and straight(ranks): 
        return ((8, max(ranks)), 'Straight Flush')
    elif n_of_kind(ranks, 4):
        return ((7, n_of_kind(ranks, 4), n_of_kind(ranks, 1)), 'Four of a Kind')
    elif n_of_kind(ranks, 3) and n_of_kind(ranks, 2):
        return ((6, n_of_kind(ranks, 3), n_of_kind(ranks, 2)), 'Full House')
    elif flush(suits):
        return ((5, ranks), 'Flush')
    elif straight(ranks):
        return ((4, max(ranks)), 'Straight')
    elif n_of_kind(ranks, 3):
        return ((3, n_of_kind(ranks, 3), single_cards(ranks)[0], single_cards(ranks)[1]), 
                 'Three of a Kind')
    elif two_pair(ranks):
        return ((2, two_pair(ranks)[0], two_pair(ranks)[1], n_of_kind(ranks, 1)), 
                 'Two Pair')
    elif n_of_kind(ranks, 2):
        return ((1, n_of_kind(ranks, 2), single_cards(ranks)[0], single_cards(ranks)[1], 
                 single_cards(ranks)[2]), 'A Pair')
    else:
        return ((0, ranks), 'High Card')

#-----------------------------------------------------------------------------#
"""
Change the card Ace to 1 if its a low straight hand, otherwise keep it as 
an Ace. Then, extract the ranks from the hand and sort them in descending 
order.

Args: (i) Hand of cards

Returns: (i) Ranks of a hand in list format
"""
def card_ranks(hand):
    ranks = ['--23456789TJQKA'.index(r) for r,s in hand]
    ranks.sort(reverse = True)
    if ranks == [14,5,4,3,2]:
        return [5,4,3,2,1]
    return ranks

#-----------------------------------------------------------------------------#
"""
Check if four of a kind, three of a kind, two of a kind, one of a kind exist 
in the hand.

Args: (i)  Ranks of a hand
      (ii) N of a kind 

Returns: (i) Rank of N of a kind or False
"""
def n_of_kind(ranks, n):
    for r in ranks:
        if ranks.count(r) == n:
            return r
    return False

#-----------------------------------------------------------------------------#
"""
Check if the hand contains two pairs of same rank.

Args: (i) Ranks of a hand

Returns: (i) Two pairs in list format or False
"""
def two_pair(ranks):
    h_pair = n_of_kind(ranks, 2)
    l_pair = n_of_kind(list(reversed(ranks)), 2)
    if h_pair and h_pair != l_pair:
        return [h_pair, l_pair]
    return False

#-----------------------------------------------------------------------------#
"""
Find all the single cards in the hand.

Args: (i) Ranks of a hand

Returns: (i) All the single cards in the hand in list format
"""
def single_cards(ranks):
    return [r for r in ranks if ranks.count(r) == 1]

#-----------------------------------------------------------------------------#
"""
Check if all the cards in the hand are of same suit.

Args: (i) Suits of a hand

Returns: (i) True or False
"""
def flush(suits):
    return len(set(suits)) == 1

#-----------------------------------------------------------------------------#
"""
Check if all the cards in the hand are in a continuous file.

Args: (i) Ranks of a hand

Returns: (i) True or False
"""
def straight(ranks):
    return (len(set(ranks)) == 5) and (max(ranks) - min(ranks) == 4)

#-----------------------------------------------------------------------------#
"""
Test values and assert statements for above functions.
"""
"""
def calculate_hand_rank_test():
    print calculate_hand_rank(['7H','6H','5H','4H','3H']) #Straight Flush
    print calculate_hand_rank(['TC','TD','TH','TS','5D']) #Four of a Kind
    print calculate_hand_rank(['TS','4H','TD','4S','4D']) #Full House
    print calculate_hand_rank(['AH','QH','TH','5H','3H']) #Flush
    print calculate_hand_rank(['8S','7S','6H','5H','4S']) #Straight
    print calculate_hand_rank(['QS','QC','5S','3C','QD']) #Three of a Kind
    print calculate_hand_rank(['KH','2C','KD','2D','JH']) #Two Pair
    print calculate_hand_rank(['TC','TS','6S','4H','2H']) #A Pair
    print calculate_hand_rank(['TD','AD','9S','5C','4C']) #High Card

    assert calculate_hand_rank(['7H','6H','5H','4H','3H'])[0][0] == 8 #Straight Flush
    assert calculate_hand_rank(['TC','TD','TH','TS','5D'])[0][0] == 7 #Four of a Kind
    assert calculate_hand_rank(['TS','4H','TD','4S','4D'])[0][0] == 6 #Full House
    assert calculate_hand_rank(['AH','QH','TH','5H','3H'])[0][0] == 5 #Flush
    assert calculate_hand_rank(['8S','7S','6H','5H','4S'])[0][0] == 4 #Straight
    assert calculate_hand_rank(['QS','QC','5S','3C','QD'])[0][0] == 3 #Three of a Kind
    assert calculate_hand_rank(['KH','2C','KD','2D','JH'])[0][0] == 2 #Two Pair
    assert calculate_hand_rank(['TC','TS','6S','4H','2H'])[0][0] == 1 #A Pair
    assert calculate_hand_rank(['TD','AD','9S','5C','4C'])[0][0] == 0 #High Card
    return 'All Tests Passed'

print calculate_hand_rank_test()
"""
#-----------------------------------------------------------------------------#
