import numpy as np
from Poker import Player, Deck, Game,GameEvaluator, GTOEvaluator, Board, Dealer
"""Deck Methods"""
deck = Deck()
deck.fill_deck()
deck.shuffle()

"""deck.print_deck()"""

player1 = Player()
player2 = Player()

dealer = Dealer()

game = Game()
board = Board()
evaluator = GameEvaluator()
gto_play = GTOEvaluator()

try:
    """Experimentation to check that I can at least display the cards"""
    game.start()

    dealer.deal(deck.deck, player1=player1, player2=player2)
    print("Your Hand:")
    player1.show()
    print()
    #player2.show() hidden hand

    game.flop(deck=deck.deck)
    print("Current Board: ")
    game.board.print_board()
    game.turn(deck=deck.deck)

    game.board.print_board()

    game.river(deck=deck.deck)

    game.board.print_board()

    player2.show()

except:
    print("Please enter a valid number")

