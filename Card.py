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