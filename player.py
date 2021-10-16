import decks
import random

class Player:
    
    def __init__(self, name):
        self.hand = []
        self.val = []
        self.aces = self.val.count(1)
        self.name = "Player "+str(name)
        self.total = sum(self.val)
    
    def take_bet(self):
        self.bet = int(input(f'Hvor mye vil {self.name} vedde?'))
    
    def draw_card(self, deck):
        rand_int = random.randint(0, len(deck.deck))
        number = deck.deck[rand_int]
        c = decks.Card(number%13)
        self.hand.append(c.card)
        self.val.append(c.val)
        deck.deck.pop(rand_int)
        self.total = sum(self.val)
    
    def show_hand(self):
        if self.name != "Dealer":
            print(f'{self.name} hand is:')
            for i in self.hand:
                print(i)
    
    def totals(self):
        while self.aces > 0 and self.total > 21:
            self.total -= 10
            self.aces -= 1
        return self.total
    
    def win(self, dealer):
        if self.totals()>21:
            print(f'{self.name} loses {self.bet}.')
        elif dealer.totals()>21:
            print(f'{self.name} wins {self.bet *2}.')
        elif self.totals() == 21 and len(self.hand)== 2 and dealer.totals() != 21:
            print(f"{self.name} wins {self.bet*3} with blackjack")
        elif self.totals() == dealer.totals():
            print(f'{self.name} push, {self.totals()} is equal to {self.totals()}.')
        elif self.totals()>dealer.totals():
            print(f'{self.name} wins {self.bet *2}, {self.totals()} is greater than {dealer.totals()}.')
        elif dealer.totals()>self.totals():
            print(f'{self.name} loses {self.bet}, {dealer.totals()} is greater than {self.totals()}.')
class Dealer(Player):
    
    def __init__(self):
        super().__init__(None)
        self.name = "Dealer"
        
    def show_hand_dealer(self, pre):
        if pre:
            print(f'{self.name} hand is:')
            c = decks.Card(69)
            print(c.card)
            print(self.hand[0])
        else:
            print(f'{self.name} hand is:')
            for i in self.hand:
                print(i)

