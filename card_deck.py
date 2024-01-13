# Python 3.11
# Harry Mancinelli
# Create card deck

import itertools

def create_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

    deck = list(itertools.product(ranks, suits))

    return(deck)






