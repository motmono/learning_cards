import random

class deck(object):
    def __init__(self):
        self.fulldeck = []

    def addcards(self, cardslist):
        self.fulldeck += cardslist

    def deal(self, players, cards):
        p, c = players, cards
        self.hand = [[0 for x in range(c)] for y in range(p)]
        y = 0
        while y < c:
            for x in range(p):
                self.hand[x][y] = self.fulldeck.pop(0)
            y += 1

    def shuffle(self):
        self.fulldeck = random.sample(self.fulldeck, len(self.fulldeck))

class suit(object):
    def __init__(self, p):
        self.cards = [p + '2', p + '3', p + '4', p + '5', p + '6', p + '7', p + '8', p + '9', p + '10', p + "J", p +"Q", p + "K", p + "A"]

    def shuffle(self):
        self.cards = random.sample(self.cards, len(self.cards))
            
class player(object):
    def __init__(self):
        self.hand = []

    def reorder(self, first, second):
        x = self.hand[first]
        self.hand[first] = self.hand[second]
        self.hand[second] = x
        
    def play(self, card):
        return self.hand.pop(card)
    
        

clubs = suit('c')
spades = suit('s')
hearts = suit('h')
diamonds = suit('d')

game = deck()
game.addcards(clubs.cards)
game.addcards(spades.cards)
game.addcards(hearts.cards)
game.addcards(diamonds.cards)

game.shuffle()
game.deal(4, 4)

player1 = player()
player1.hand = game.hand[0]

player0 = player()
player0.hand = ['d2', 'c6', 'hK', 'h2']

print(player0.hand)
player0.reorder(2,3)
print(player0.hand)
x = player0.play(1)
print(player0.hand)
print(x)




