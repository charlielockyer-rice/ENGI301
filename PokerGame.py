from Shuffler import *
import random

# Define amount of players
players = 3

# Make a deal map
deal_map = {-1: [Card(Suit.CLUBS, Rank.JACK), Card(Suit.CLUBS, Rank.TEN), Card(Suit.DIAMONDS, Rank.SEVEN),
                 Card(Suit.HEARTS, Rank.THREE), Card(Suit.CLUBS, Rank.QUEEN)],
            0: [Card(Suit.CLUBS, Rank.KING), Card(Suit.CLUBS, Rank.ACE)],
            1: [Card(Suit.DIAMONDS, Rank.ACE), Card(Suit.SPADES, Rank.ACE)],
            2: [Card(Suit.DIAMONDS, Rank.TWO), Card(Suit.SPADES, Rank.TEN)]}

# Create a deck of cards
deck = [Card(suit, rank) for suit in Suit for rank in Rank]
random.shuffle(deck)

# Put the deck into the shuffler
shuffler = Container(64, False)
for i, card in enumerate(deck):
    shuffler.insert_card(i, card)


# Deal the cards to the players (player 1 will always be the dealer)
hands = [[] for _ in range(players)]
for card in range(2):
    for player in range(players):
        if shuffler.rigged:
            hands[player].append(shuffler.deal_rigged_card(player, deal_map))
        else:
            hands[player].append(shuffler.deal_random_card())

# Print the cards dealt to each player
for i, hand in enumerate(hands):
    print(f"Player {i + 1}: {hand[0]} and {hand[1]}")

# Make the table
table = []

# Deal the flop
for card in range(3):
    if shuffler.rigged:
        table.append(shuffler.deal_rigged_card(-1, deal_map))
    else:
        table.append(shuffler.deal_random_card())

# Print the flop
print(f"Flop: {table[0]}, {table[1]}, and {table[2]}")

# Deal the turn
if shuffler.rigged:
    table.append(shuffler.deal_rigged_card(-1, deal_map))
else:
    table.append(shuffler.deal_random_card())

# Print the turn
print(f"Turn: {table[3]}")

# Deal the river
if shuffler.rigged:
    table.append(shuffler.deal_rigged_card(-1, deal_map))
else:
    table.append(shuffler.deal_random_card())

# Print the river
print(f"River: {table[4]}")
