import numpy as np
from Deck import Deck

class Player:
    def __init__(self):
        self.hand = []
    
    def show(self):
        for card in self.hand:
            print(card)
