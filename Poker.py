import numpy as np

class Player:
    def __init__(self):
        self.hand = []
    
    def show(self):
        for card in self.hand:
            print(card)

class Dealer:
    def __init__(self):
        pass
    def deal(self):
        """for i, card in deck:
            give player card i * -1. Make
            sure to handle burns as needed."""

class Deck:
    def __init__(self):
        self.deck = []
        self.card_values = np.array(["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]) 
        """get rid of this and define a stack class in future"""
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
    
class Game:
    def __init__(self):
        self.deck = Deck()
        pass
    def start(self):
        try:
            print("Welcome to the Poker Simulator.")
        except:
            print("Error occured")

    def flop(self, deck):
        print(deck[-6])
        print(deck[-7])
        print(deck[-8])
        pass
    def turn(self, deck):
        print(deck[-9])
        pass
    def river(self, deck):
        print(deck[-11])
        pass
class Bet:
    def __init__(self, bet):
        self.bet = bet
        pass

class GameEvaluator:
    def __init__(self):
        pass
    def high_card(self):
        pass
    def check_pair(self):
        pass
    def check_two_pair(self):
        pass
    def check_set(self):
        pass
    def check_trips(self):
        pass
    def check_flush(self):
        pass
    def check_straight(self):
        pass
    def check_full_house(self):
        pass
    def check_straight_flush(self):
        pass
    def check_royal_flush(self):
        pass

