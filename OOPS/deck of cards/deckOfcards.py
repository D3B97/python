from random import shuffle

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f"{self.value} of {self.suit}"


class Deck:
    def __init__(self):
        self.suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = []
        for suit in self.suits:
            for value in self.values:
                self.cards.append(Card(value, suit))

    def count(self):
        return len(self.cards)

    def _deal(self, num):
        count = self.count()
        actual = min([count, num])
        print(f"Going to remove {actual} cards")
        if count == 0:
            raise ValueError ("All cards have been dealt")
        cards = self.cards[-actual : ]
        self.cards = self.cards[:-actual]
        return cards

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, hand_size):
        return self._deal(hand_size)

    def shuffle(self):
        if len(self.cards) < 52:
            raise ValueError("Can shuffle only when deck has 52 cards")

c = Deck()
print(c.cards)

print(c.count())

print(c._deal(10))

print(c.count())