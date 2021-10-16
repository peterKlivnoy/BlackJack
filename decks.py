
class Card:
    
    def __init__(self, number):
        self.card_values = {1:11, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 11:10, 12:10, 0:10}
        
        if number== 10:
            self.card = f"__________\n| {number}     |\n|        |\n|        |\n|     {number} |\n|________|"
        elif number >1 and number<10:
            self.card = f"__________\n| {number}      |\n|        |\n|        |\n|      {number} |\n|________|"
        elif number==1:
            self.card = f"__________\n| A      |\n|        |\n|        |\n|      A |\n|________|"
        elif number == 11:
            self.card = f"__________\n| J      |\n|        |\n|        |\n|      J |\n|________|"
        elif number == 12:
            self.card = f"__________\n| D      |\n|        |\n|        |\n|      D |\n|________|"
        elif number == 0:
            self.card = f"__________\n| K      |\n|        |\n|        |\n|      K |\n|________|"
        elif number == 69:
            self.card = f"__________\n|********|\n|********|\n|********|\n|********|\n|________|"
        self.val = self.card_values.get(number, 0)
class Deck:
    def __init__(self):
        self.deck = [i for i in range(1,53)]
        









