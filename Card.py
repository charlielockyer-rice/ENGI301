from enum import Enum


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.rank < other.rank
        return NotImplemented

    def __eq__(self, other):
        if self.__class__ is other.__class__:
            return self.suit == other.suit and self.rank == other.rank
        return False

    def __str__(self):
        return f"{self.rank.value} of {self.suit.value}"


class Suit(Enum):
    SPADES = "Spades"
    HEARTS = "Hearts"
    CLUBS = "Clubs"
    DIAMONDS = "Diamonds"

    def __eq__(self, other):
        if self.__class__ is other.__class__:
            return self.value == other.value
        return False

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented


class Rank(Enum):
    ACE = "Ace"
    KING = "King"
    QUEEN = "Queen"
    JACK = "Jack"
    TEN = "10"
    NINE = "9"
    EIGHT = "8"
    SEVEN = "7"
    SIX = "6"
    FIVE = "5"
    FOUR = "4"
    THREE = "3"
    TWO = "2"

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented
