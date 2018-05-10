# COPYRIGHT 2018 BY LARRY TSENG

import random


class Deck(object):

    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 't', 'j', 'q', 'k', 'a']
    suits = ['s', 'h', 'd', 'c']

    def __init__(self):
        self.deck = []
        for suit in self.suits:
            for rank in reversed(self.ranks):
                self.deck.append(rank + suit)

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self, numCards):
        card = self.deck[:numCards]
        self.deck = self.deck[numCards:]

        return card


random.seed(1)
mydeck = Deck()
print mydeck.deal(5)  # "should be ['as', 'ks', 'qs', 'js', 'ts']"
mydeck.shuffle()
print mydeck.deal(5)  # "should be ['3h', 'th', '7s', 'qc', '5c']"
print mydeck.deal(2)  # "should be ['5h', '9h']"
