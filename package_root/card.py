class Card:
    def __init__(self, Type, Luxury):
        self.Type = Type
        self.Luxury = Luxury

    def get_Type(self):
        return self.Type

    def get_Luxury(self):
        return self.Luxury
    
    def display_Card(self):
        print("----------------")
        print("-              -")
        print("-              -")
        print("-              -")
        print("-              -")
        print("-              -")
        print("-              -")
        print("----------------")