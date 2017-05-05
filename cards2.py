import random

# deck class, allows the user to create a deck of cards, shuffle and deal them
class deck(object):
    # initailize the deck with an empty list fulldeck and a number of players set to zero
    def __init__(self):
        self.fulldeck = []
        self.numplayers = 0

    # method to add cards to the deck
    # input: a list of cards
    def addcards(self, cardslist):
        self.fulldeck += cardslist

    # method to deal cards out of the deck to a given nuber of players
    # input: number of players and cards to deal each player
    def deal(self, players, cards):
        self.numplayers = players
        p, c = players, cards
        self.hand = [[0 for x in range(c)] for y in range(p)]
        y = 0
        while y < c:
            for x in range(p):
                self.hand[x][y] = self.fulldeck.pop(0)
            y += 1

    # method to randomize all the cards in the deck
    def shuffle(self):
        self.fulldeck = random.sample(self.fulldeck, len(self.fulldeck))

# suit class, creates custom suit of cards pulling from a dictionary
class suit(object):
    # initialize the suit class
    # input: single character to specify suit
    def __init__(self, p):
        self.cards = []
        self.mysuit = p

    # method to randomize all the cards in the suit if desired
    def shuffle(self):
        self.cards = random.sample(self.cards, len(self.cards))

    # method to add cards to a given suit, includes jokers
    # inputs: low value of cards to add, high card to add
    def addcards(self, low, high):
        carddict = {11: 'J', 12: 'Q', 13: 'K', 14: 'A', 15: 'jok', 16: 'jok'}
        while low <= high:
            if low <= 10:
                self.cards.append(self.mysuit + str(low))
            else:
                self.cards.append(self.mysuit + carddict[low])
            low += 1
            
#  player class, assigns the player a hand allowing them to reorder and play cards           
class player(object):
    # initialize the player class with a hand variable
    def __init__(self):
        self.hand = []

    # method to reorder two cards in a list
    # input: first card to swtich, second card to switch 
    def reorder(self, first, second):
        x = self.hand[first]
        self.hand[first] = self.hand[second]
        self.hand[second] = x

    # method to take a given card in a list and play it
    # input: index of the card to play in the list
    def play(self, card):
        return self.hand.pop(card)

# game class, defines the rules and gameplay of a given game    
class game(object):
    # initialize the game with a type variable determining the game type
    def __init__(self):
        self.type = ""
        
# define the suits in the game (Euchre in this case)
clubs = suit('c')
clubs.addcards(9, 14)
spades = suit('s')
spades.addcards(9, 14)
hearts = suit('h')
hearts.addcards(9, 14)
diamonds = suit('d')
diamonds.addcards(9, 14)

# create and add the respective cards and suits to the deck
mydeck = deck()
mydeck.addcards(clubs.cards)
mydeck.addcards(spades.cards)
mydeck.addcards(hearts.cards)
mydeck.addcards(diamonds.cards)

# shuffle and deal the deck
mydeck.shuffle()
mydeck.deal(4, 5)

# assign the players their respective hands
player1 = player()
player1.hand = mydeck.hand[0]

player2 = player()
player2.hand = mydeck.hand[1]

player3 = player()
player3.hand = mydeck.hand[2]

player4 = player()
player4.hand = mydeck.hand[3]


print(player1.hand)
print(player2.hand)
print(player3.hand)
print(player4.hand)




