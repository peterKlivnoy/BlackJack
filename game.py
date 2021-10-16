import player
import decks

t = int(input('Hvor mange spillere skal spille'))
d = decks.Deck()
players = [player.Player(i) for i in range(1,t+1)]
dealer = player.Dealer()
pre = True
for i in players:
    i.take_bet()
for i in players:
    i.draw_card(d)
dealer.draw_card(d)
dealer.show_hand_dealer(pre)
for i in players:
    i.draw_card(d)
    i.show_hand()
dealer.draw_card(d)
pre = False



for i in players:
    x = True
    while x:
        s = input(f"Do you {i.name} want to draw a card?")
        if s.lower() == "yes":
            i.draw_card(d)
            i.show_hand()
            if i.totals() >= 21:
                x = False
        else:
            x = False

while dealer.totals() < 16:
    dealer.show_hand_dealer(pre)
    dealer.draw_card(d)
    
dealer.show_hand_dealer(pre)
for i in players:
    i.win(dealer)





