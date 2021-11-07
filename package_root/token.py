class Token:
    def __init__(self, Type, Value):   
        self.Type = Type
        self.Value = Value
    
    def get_Type(self):
        return self.Type

    def get_Value(self):
        return self.Value 