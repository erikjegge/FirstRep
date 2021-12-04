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
    
    def add_To_Farm(self, list):
        self.farm.extend(list)