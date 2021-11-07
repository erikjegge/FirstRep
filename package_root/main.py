"""
    Jaipur

    START DATE: 10/6/2021

    BY: ERIK EGGE
"""
from game import Globals
from player import Player

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
        print(r.get_Type())
        print(r.display_Card())

    #x = g.get_Token_Piles()

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