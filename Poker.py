import numpy as np
from Poker import Card

class Player:
    def __init__(self):
        self.hand = []
    
    def show(self):
        for card in self.hand:
            print(card)
    
class Deck:
    def __init__(self):
        self.deck = []
        self.card_values = np.array(["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"])
        pass
    def fill_deck(self):
        for i in range(52):
            if i <= 12:
                self.deck.append(Card("Heart", self.card_values[i]))
            elif i >= 13 and i <= 25:
                self.deck.append(Card("Spade", self.card_values[i - 13]))
            elif i >= 26 and i <= 38:
                self.deck.append(Card("Club", self.card_values[i - 26]))
            elif i >= 39:
                self.deck.append(Card("Diamond", self.card_values[i - 39]))
        self.deck = np.array(self.deck)
    def print_deck(self):
        for element in self.deck:
            print(element)
    def shuffle(self):
        np.random.shuffle(self.deck)
        pass
    def flop(self):
        pass
    def turn():
        pass
    def river():
        pass
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    def __str__(self):
        return f"{self.value} of {self.suit}s"

    def getSuit(self, suit):
        return suit
    def getValue(self, value):
        return value