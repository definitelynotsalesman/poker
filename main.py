import numpy as np
from Poker import Card, Player, Deck, Game
"""Deck Methods"""
deck = Deck()
deck.fill_deck()
deck.shuffle()

game = Game()

try:
    game.start()
    game.flop(deck=deck.deck)
    game.turn(deck=deck.deck)
    game.river(deck=deck.deck)

except:
    print("Please enter a valid number")

