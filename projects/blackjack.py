"""Object-Oriented Blackjack Game."""

import random

suits = ("♠", "♥", "♦", "♣")
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


class Card:
    def __init__(self, rank: str, suit: str):
        """Generates a card object."""
        self.rank = rank
        self.suit = suit
        self.value = values[self.rank]
    
    def __str__(self):
        """String representation of card object."""
        return f'{self.rank} of {self.suit}'


class Deck: 
    def __init__(self):
        """Generates a new deck of 52 cards."""
        self.deck: list[Card] = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(rank, suit))

    def __str__(self):
        """Prints out contents of deck."""
        deck_composition: str = ''
        for card in self.deck:
            deck_composition += f'\n {card.__str__()}'
        return deck_composition

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        one_card: Card = self.deck.pop()
        return one_card


class Hand:
    def __init__(self):
        """Tracks the total value of a hand and the number of Aces present."""
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card: Card):
        self.cards.append(card)
        self.value += card.value
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_aces(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
    
            