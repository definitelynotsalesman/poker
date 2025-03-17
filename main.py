import numpy as np
from Poker import Card, Player, Deck, Game,GameEvaluator, GTOEvaluator, Board
"""Deck Methods"""
deck = Deck()
deck.fill_deck()
deck.shuffle()

deck.print_deck()

game = Game()
board = Board()
evaluator = GameEvaluator()
gto_play = GTOEvaluator()

try:
    """Experimentation to check that I can at least display the cards"""
    game.start()
    game.flop(deck=deck.deck)
    print("Current Board: ")
    game.board.print_board()
    game.turn(deck=deck.deck)

    game.board.print_board()

    game.river(deck=deck.deck)

    game.board.print_board()

except:
    print("Please enter a valid number")

