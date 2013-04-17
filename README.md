#-----------------------------------------------------------------------------#
#                            Poker Solutions                                  #
#-----------------------------------------------------------------------------#

PROBLEM: Write a program to find the winner of a Poker match (five card game).

The match can be played with either a standard 52 card deck or with a 54 card deck (52 cards plus 2 joker cards). In the match involving jokers, a red joker can be replaced by any diamonds/hearts card, while a black joker can be replaced by any clubs/spades card. The program must first create a deck of cards, then shuffle the deck, then deal cards to the players. Based on the hand received by every player, a hand rank is calculated and the poker winner is determined as per the standard rules of poker listed below.

- Straight flush
- Four of a kind
- Full house
- Flush
- Straight
- Three of a kind
- Two pair
- One pair
- High card

Multiple winners are also possible (e.g. [6S 5S 4S 3S 2S] and [6D 5D 4D 3D 2D])

SOURCE: http://en.wikipedia.org/wiki/List_of_poker_hands

IMPLEMENTATION: python main.py
#-----------------------------------------------------------------------------#
