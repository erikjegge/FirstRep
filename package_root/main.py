"""
    Jaipur

    START DATE: 10/6/2021

    BY: ERIK EGGE
"""
from game import Globals
from player import Player
# from tkinter import *
# from tkinter import messagebox

def reset():
    # will reset the screen and initalize new game
    return True

def main():

    boolCont = True
    while boolCont:
        print('<><><><><><><><> JAIPUR <><><><><><><><>')
        print('0.) Play')
        print('1.) Quit')
        
        menuInput = input("Please enter an option from above\n")
        if menuInput not in ('0','1'):
            print('please enter valid input')
        else:
            boolCont = False
            if menuInput == '1':
                #close the program
                quit()
            else:
                #go to game
                #<><><><><><><><><><><><><><><><><><><><><><><><>
                # # initializing gui using tkinter
                # root = Tk()
                # root.title("Jaipur")
                # #root.iconbitmap()

                # root.mainloop()
                #<><><><><><><><><><><><><><><><><><><><><><><><>
                g = Globals()
                g.initialize_Deck()
                g.initialize_Tokens()
                g.draw_Cards(5)

                p1 = Player("Player1",[],[],[])
                p2 = Player("Player2",[],[],[])

                g.deal_Cards(p1, 5)
                g.deal_Cards(p2, 5)

                # any camels that start in hand go to farm, for rest of game, they go directly to farm from display
                for i, r in enumerate(p1.get_Hand()):
                    if r.get_Type() == 'Camel':
                        p1.farm.append(p1.hand.pop(i))
    
                print("Market")
                for r in g.get_Market():
                    print(r.get_Type())
                print("Player 1 Hand:")
                for r in p1.get_Hand():
                    print(r.get_Type())
                print("Player 1 Farm:")
                for r in p1.get_Farm():
                    print(r.get_Type())

                print('<><><><><><><><> Player: Turn: <><><><><><><><>')
                print('0.) Take Cards')
                print('1.) Sell Cards')
                gameInput = input("Please enter an option from above\n")
                if gameInput not in ('0','1'):
                    print('please enter valid input')
                else:
                   if gameInput == '0':
                        #take cards
                        print('<><><><><><><><> Take Cards Action <><><><><><><><>')
                        print('0.) Take Several Goods')
                        print('1.) Take One Good')
                        print('2.) Take All Camels')
                        gameInput = input("Please enter an option from above\n")
                        if gameInput not in ('0','1','2'):
                            print('please enter valid input')
                        else:
                            # move into 
                            takeCards(p1, g, gameInput)

                print("Market")
                for r in g.get_Market():
                    print(r.get_Type())
                print("Player 1 Hand:")
                for r in p1.get_Hand():
                    print(r.get_Type())
                print("Player 1 Farm:")
                for r in p1.get_Farm():
                    print(r.get_Type())

                #    else:
                        #sell cards

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
def takeCards(player, game, option):
    #1: take several goods, then replenish the market cards with a combination of camels and cards from your hand

    #2: take 1 good, then replace the marketcard with the top card of the deck (can't take just one camel)
    if option == '1':
        camels = [i for i in game.get_Market() if i.get_Type() == 'Camel']
        goodCards = [i for i in game.get_Market() if i.get_Type() != 'Camel']

        print('<><><><><><><><> Take One Card Action <><><><><><><><>')
        options = []
        for i, r in enumerate(goodCards):
            print('%i.) %s' % (i, r.get_Type()))
            options.append(str(i))

        gameInput = input("Please enter an option from above\n")
        if gameInput not in (options):
            print('please enter valid input')
        else:
            # do the thing
            cardsToAdd = []
            cardsToAdd.append(goodCards.pop(int(gameInput)))
            player.add_To_Hand(cardsToAdd)

            # add the camels back in
            goodCards.extend(camels)
            # reset market
            game.reset_Market(goodCards)

            game.draw_Cards(1) # draw card from top of deck


    #3: take all the camels from the marketCards and then replace with cards from the top of the deck until there are 5
    if option == '2':
        # list comp for two seperate lists, one of just camels, one of everything else
        camels = [i for i in game.get_Market() if i.get_Type() == 'Camel']
        otherCards = [i for i in game.get_Market() if i.get_Type() != 'Camel']

        # add the camels to the player's farm
        player.add_To_Farm(camels)

        # make the other card's the new market
        game.reset_Market(otherCards)

        # refill the market up to 5
        refillCards = 5 - game.get_Market_Len()
        if refillCards != 0:
            game.draw_Cards(refillCards)

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