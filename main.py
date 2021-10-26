"""
    Jaipur

    START DATE: 10/6/2021

    BY: ERIK EGGE
"""

import random

class Globals: 
    def __init__(self):
        self.deckOfCards = []
        self.marketCards = []
        self.tokenPiles = {
                    'Leather':[], 
                    'Cloth':[], 
                    'Spice':[],
                    'Silver':[],
                    'Gold':[],
                    'Diamond':[],
                    'Bonus5':[],
                    'Bonus4':[],
                    'Bonus3':[],
                    'CamelToken':[]
        }

    def initialize_Deck(self):
        numberOfLuxuryGoods = 6
        numberOfCS = 8
        numberOfL = 10
        numberOfCamel = 11

        for _ in range(numberOfLuxuryGoods):
            self.deckOfCards.append(Card('Diamond',True))
            self.deckOfCards.append(Card('Gold',True))
            self.deckOfCards.append(Card('Silver',True))

        for _ in range(numberOfCS):
            self.deckOfCards.append(Card('Cloth',False))
            self.deckOfCards.append(Card('Spice',False))

        for _ in range(numberOfL):
            self.deckOfCards.append(Card('Leather',False))

        # we start automatically with 3 camels in the market to start the game so we will append them after shuffling
        for _ in range(numberOfCamel - 3):
            self.deckOfCards.append(Card('Camel',False))

        random.shuffle(self.deckOfCards)

        for _ in range(3):
            self.deckOfCards.append(Card('Camel',False))

    def initialize_Tokens(self):
        #initialize the game tokens
        TP1 = [1,1,1,1,1,1,2,3,4]
        TP2 = [1,1,2,2,3,3,5]
        TPS = [5,5,5,5,5]
        TPG = [5,5,5,6,6]
        TPD = [5,5,5,7,7]
        # shuffle these ones
        TP5 = [10,10,9,8,8]
        TP4 = [6,6,5,5,4,4]
        TP3 = [1,1,2,2,2,3,3]

        random.shuffle(TP5)
        random.shuffle(TP4)
        random.shuffle(TP3)

        # goods tokens
        for r in TP1:
            self.tokenPiles['Leather'].append(Token('Leather', r))
        for r in TP2:
            self.tokenPiles['Cloth'].append(Token('Cloth', r))
            self.tokenPiles['Spice'].append(Token('Spice', r))
        for r in TPS:
            self.tokenPiles['Silver'].append(Token('Silver', r))
        for r in TPG:
            self.tokenPiles['Gold'].append(Token('Gold', r))
        for r in TPD:
            self.tokenPiles['Diamond'].append(Token('Diamond', r))

        # bonus tokens
        for r in TP5:
            self.tokenPiles['Bonus5'].append(Token('Bonus5', r))
        for r in TP4:
            self.tokenPiles['Bonus4'].append(Token('Bonus4', r))
        for r in TP3:
            self.tokenPiles['Bonus3'].append(Token('Bonus3', r))

        # camel token
        self.tokenPiles['CamelToken'].append(Token('CamelToken', 5))

    # deal Token
    def deal_Token(self, type, player):
        if self.tokenPiles.get(type):   # checking if this list is empty or not
            if player == 1:
                self.player1Pile.append(self.tokenPiles.get(type).pop())
            elif player == 2:
                self.player2Pile.append(self.tokenPiles.get(type).pop())

    def get_Token_Piles(self):
        return self.tokenPiles

    # just helpers for testing
    def get_Deck_Len(self):
        return len(self.deckOfCards)

    # just helpers for testing    
    def get_Market_Len(self):
        return len(self.marketCards)

    # draw any number of cards from the deck to the market
    def draw_Cards(self, number):
        for _ in range(number):
            self.marketCards.append(self.deckOfCards.pop())

    # see the market
    def get_Market(self):
        return self.marketCards

    # which player 1 or two taking the cards
    def deal_Cards(self, player, number):
        for _ in range(number):
            player.hand.append(self.deckOfCards.pop())

class Card:
    def __init__(self, Type, Luxury):
        self.Type = Type
        self.Luxury = Luxury

    def get_Type(self):
        return self.Type

    def get_Luxury(self):
        return self.Luxury

class Token:
    def __init__(self, Type, Value):   
        self.Type = Type
        self.Value = Value
    
    def get_Type(self):
        return self.Type

    def get_Value(self):
        return self.Value 

class Player: 
    """
        Each player has...
            + a token pile (points)
            + a hand of cards
            + a farm of camels
    """
    def __init__(self, name, tokens, hand, farm):
        self.name = name
        self.tokens = tokens
        self.hand = hand
        self.farm = farm
    
    def get_Tokens(self):
        return self.tokens

    def get_Hand(self):
        return self.hand

    def get_Farm(self):
        return self.farm


def main():
    g = Globals()
    g.initialize_Deck()
    g.initialize_Tokens()
    g.draw_Cards(5)

    p1 = Player("Player1",[],[],[])
    p2 = Player("Player2",[],[],[])
    
    for r in p1.get_Hand():
        print(r)

    print('after 1')
    g.deal_Cards(p1, 5)

    for r in p1.get_Hand():
        print(r)

    x = g.get_Token_Piles()

    #print(x.get('Leather'))

    #for key in list(x):
    #    print(key + ": " + str(len(x[key])))


"""
    on a turn you can do one of two things

    TAKE CARDS

    OR 

    SELL CARDS

    never both
"""
def takeCards(playerHand, market):
    #1: take several goods, then replenish the market cards with a combination of camels and cards from your hand

    #2: take 1 good, then replace the marketcard with the top card of the deck

    #3: take all the camels from the marketCards and then replace with cards from the top of the deck until there are 5
    return

def sellCards():
    # three steps
    # 1: Sell cards from your hand of 1 type, as many as you wish
        # if luxury good, there is a minimum of 2 cards per sale. You cannot sell just 1 luxury good
    # 2: Take as many tokens as cards discarded, descending values so that you are always taking the highest value of the stack
    # 3: Take cooresponding bonus
    #       3 cards sold: 1 random Bonus3 token
    #       4 cards sold: 1 random Bonus4 token
    #       5 cards sold: 1 random Bonus5 token
    return

# type is the Type of card sold coorsponds with the dictionary key
# bonus is true false
# numberOfTokens is the number of tokens you will take
def takeTokens(type, numberOfTokens, bonus):
    if bonus:
        True

    return





if __name__ == "__main__":
    main()


