# This is a file defining the Euchre game, rules and cards

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
