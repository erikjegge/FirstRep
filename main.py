"""
    Jaipur

    START DATE: 10/6/2021

    BY: ERIK EGGE
"""

import random

class Card:
    def __init__(self, Type, Luxury):
        self.Type = Type
        self.Luxury = Luxury

    def get_Type(self):
        return self.Type

    def get_Luxury(self):
        return self.Luxury
    
"""
    Shuffle the deck
"""
def shuffle_deck(deck):
    random.shuffle(deck)

def main():
    deckOfCards = []
    numberOfLuxuryGoods = 6
    numberOfCS = 8
    numberOfL = 10
    numberOfCamel = 11

    for _ in range(numberOfLuxuryGoods):
        deckOfCards.append(Card('Diamond',True))
        deckOfCards.append(Card('Gold',True))
        deckOfCards.append(Card('Silver',True))

    for _ in range(numberOfCS):
        deckOfCards.append(Card('Cloth',False))
        deckOfCards.append(Card('Spice',False))

    for _ in range(numberOfL):
        deckOfCards.append(Card('Leather',False))

    for _ in range(numberOfCamel):
        deckOfCards.append(Card('Camel',False))

    shuffle_deck(deckOfCards)

    for x in deckOfCards:
        print(x.get_Type())

if __name__ == "__main__":
    main()


