import numpy as np
from Poker import Card, Player, Deck, Game,GameEvaluator
"""Deck Methods"""
deck = Deck()
deck.fill_deck()
deck.shuffle()

game = Game()
evaluator = GameEvaluator()

try:
    """Experimentation to check that I can at least display the cards"""
    game.start()
    game.flop(deck=deck.deck)
    game.turn(deck=deck.deck)
    game.river(deck=deck.deck)

except:
    print("Please enter a valid number")

