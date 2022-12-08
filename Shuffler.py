from Card import *
from Errors import *
import random


class Container:
    def __init__(self, slots: int, rigged: bool):
        self.slots = [None] * slots
        self.rigged = rigged

    def insert_card(self, index, card: Card):
        if index < 0 or index >= len(self.slots):
            raise IndexError("Index out of range")
        self.slots[index] = card

    def deal_card_ndx(self, index: int):
        if index < 0 or index >= len(self.slots):
            raise IndexError("Index out of range")
        card = self.slots[index]
        self.slots[index] = None
        return card

    def deal_card_value(self, card: Card):
        for index, slot in enumerate(self.slots):
            if slot == card:
                self.slots[index] = None
                return card
        raise CardNotFoundError(card)

    def deal_random_card(self):
        index = random.randint(0, len(self.slots) - 1)
        card = self.slots[index]
        self.slots[index] = None
        return card

    def deal_rigged_card(self, player: int, dealmap: dict):
        deal = None
        for card in dealmap[player]:
            try:
                deal = self.deal_card_value(card)
            except CardNotFoundError:
                pass
            if deal is not None:
                return deal
        raise CardNotFoundError(deal)

    def get_card(self, index):
        if index < 0 or index >= len(self.slots):
            raise IndexError("Index out of range")
        return self.slots[index]

    def get_empty_slots(self):
        return [i for i, x in enumerate(self.slots) if x is None]

    def __str__(self):
        cards = [str(i) + ': ' + str(card) for i, card in enumerate(self.slots)]
        return "\n".join(cards)
