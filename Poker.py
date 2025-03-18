import numpy as np
import random

class Player:
    def __init__(self):
        self.hand = []
        self.buy_in = 0
    
    def show(self):
        for card in self.hand:
            print(card, end=' ')

class Dealer:
    def __init__(self):
        pass
    def deal(self, deck, player1, player2):
        """for i, card in deck:
            give player card i * -1. Make
            sure to handle burns as needed."""
        for i, card in enumerate(reversed(deck)):
            if i == 4:
                break
            if i % 2 == 0:
                player1.hand.append(card)
            else:
                player2.hand.append(card)
            pass
        #add logic here

class Deck:
    def __init__(self):
        self.deck = []
        self.card_values = [1,2,3,4,5,6,7,8,9,10,11,12,13]
        """get rid of this and define a stack class in future"""
        pass
    def fill_deck(self):
        for i in range(52):
            if i <= 12: 
                self.deck.append(Card("♥", self.card_values[i]))
            elif i >= 13 and i <= 25:
                self.deck.append(Card("♠", self.card_values[i - 13]))
            elif i >= 26 and i <= 38:
                self.deck.append(Card("♣", self.card_values[i - 26]))
            elif i >= 39:
                self.deck.append(Card("♦", self.card_values[i - 39]))
    def print_deck(self):
        for element in self.deck:
            print(element)
    def shuffle(self):
        random.shuffle(self.deck)
        pass
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    def __str__(self):
        lookup_table = {}
        return f"{self.value}{self.suit}"

    def getSuit(self, suit):
        return suit
    def getValue(self, value):
        return value
    
class Game:
    def __init__(self):
        self.deck = Deck()
        self.board = Board()
        pass
    def start(self):
        try:
            print("Welcome to the Poker Simulator.")
        except:
            print("Error occured")

    def flop(self, deck):
        """burn card 5 before dealing the flop after dealing to both players"""
        self.board.board.append(deck[-6])
        self.board.board.append(deck[-7])
        self.board.board.append(deck[-8])
        pass
    def turn(self, deck):
        self.board.board.append(deck[-10])
        """burn card 9 before dealing the turn"""
        pass
    def river(self, deck):
        self.board.board.append(deck[-12])
        """burn card 11 before dealing the river"""
        pass

class Board:
    def __init__(self):
        self.board = []
        pass
    def print_board(self):
        for card in self.board:
            print(card, end=' ')
        print("\n")

class Bet:
    def __init__(self, bet):
        self.bet = bet
        pass

class GameEvaluator:
    def __init__(self):
        self.hand = Player()
        self.board = Board()
        """7 Card Hand that will be evaluated for various features"""
        self.evaluate_board = self.hand.hand + self.board.board 
        pass
    def high_card(self):
        high_card_value = max(self.evaluate_board, key=lambda card: card.value)
        return high_card_value
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

"""Three different classes of play preflop for the artificial player, able to be determined at runtime. """

class GTOEvaluator:
    def __init__(self):
        pass

class GTO_Aggresive:
    def __init__(self):
        pass

class GTO_Tight:
    def __init__(self):
        pass