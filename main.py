import numpy as np
from Poker import Card, Player, Deck

"""Deck Methods"""
deck = Deck()
deck.fill_deck()
deck.shuffle()

try:
    player_list = []
    num_players = int(input("Input the number of players (1-5)"))
    for player in range(num_players):
        player_list.append(Player)
        pass

except:
    print("Please enter a valid number")

