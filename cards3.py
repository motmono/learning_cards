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
    # initialize the "pot" where cards will be played
    def __init__(self):
        self.type = ""
        self.pot = []
        self.dealer = 0
        self.trump = ""
        self.flip = ""

    # start the game
    def start(self):
        if self.type == "euchre":
            # initialize the deck using euchre defining file
            exec(open("euchre.py").read(), globals())

            # "flip up" the potential trump card
            self.flip = mydeck.fulldeck.pop()
            print(self.flip)
        else:
            print("No game defined")

    # method to define the the necessary actions by a player to perform a turn
    def callturn(self, player, ans):
        # if the player calls trump on the starting card assign that prump
        if self.type == "euchre":
            if(ans == 1):
                if(self.flip.find("h") == 1):
                    self.trump = "h"
                elif(self.flip.find("c") == 1):
                    self.trump = "c"
                elif(self.flip.find("d") == 1):
                    self.trump = "d"
                elif(self.flip.find("s") == 1):
                    self.trump = "s"

                print("player" + str(self.dealer) + " pick it up")

                
            else:
                print("player" + str(player) + " pass")
        else:
            print("No game defined")
                
# define and start the desired game
mygame = game()
mygame.type = "euchre"
mygame.start()

mygame.callturn(1, 0)
mygame.callturn(2, 0)
mygame.callturn(3, 0)
mygame.callturn(4, 1)

print(mygame.flip)
print(mygame.trump)



