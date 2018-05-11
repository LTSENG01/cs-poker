# COPYRIGHT 2018 BY LARRY TSENG
# A Python class for generating a deck of cards, shuffling, and dealing.

import random


class Deck(object):

    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 't', 'j', 'q', 'k', 'a']
    suits = ['s', 'h', 'd', 'c']

    def __init__(self):
        """
        Generates a deck of cards in reverse order (as, ks, qs...)
        """
        self.deck = []
        for suit in self.suits:
            for rank in reversed(self.ranks):   # Iterates starting from the end
                self.deck.append(rank + suit)

    def shuffle(self):
        """
        Shuffles the deck using the random library
        """
        random.shuffle(self.deck)

    def deal(self, numCards):
        # type: (int) -> list
        """
        Deals a specified number of cards from the deck
        :param numCards: the number of cards to draw from the deck
        :return: a list of drawn cards
        """
        card = self.deck[:numCards]     # 0 to numCards-1
        self.deck = self.deck[numCards:]    # numCards to end

        return card


# TEST CASES
# random.seed(1)
# mydeck = Deck()
# print mydeck.deal(5)  # "should be ['as', 'ks', 'qs', 'js', 'ts']"
# mydeck.shuffle()
# print mydeck.deal(5)  # "should be ['3h', 'th', '7s', 'qc', '5c']"
# print mydeck.deal(2)  # "should be ['5h', '9h']"
