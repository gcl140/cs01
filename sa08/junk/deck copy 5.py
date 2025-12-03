# File: deck.py
# Author: Gift Christian
# Date: October 27, 2025
# Course: CS 1 - Introduction to Programming and Computation-02 By Professor Balkcom
# Description: This file contains the Deck class which represents a standard deck of playing cards.

from card import Card       # Import the Card class from card.py
from random import randint  # Import randint function for shuffling

class Deck:
    def __init__(self, dealt=[]):   # Initialize the Deck class with an optional dealt parameter
        self.deck = [] + dealt  # Create a deck list, optionally starting with dealt cards


    def add_standard_cards(self):               # Method to add standard 52 playing cards to the deck in a specific order
        for i in range(1, 14):                  # Loop through card values from 1 to 13
            self.deck.append(str(Card(i, 1)))   # Add clubs to the deck
            self.deck.append(str(Card(i, 2)))   # Add spades to the deck
            self.deck.append(str(Card(i, 3)))   # Add diamonds to the deck
            self.deck.append(str(Card(i, 4)))   # Add hearts to the deck


    def shuffle(self):                          # Method to shuffle the deck randomly
        for i in range(len(self.deck)):         # Loop through each card in the deck
            num = randint(0, 51)                # Generate a random index to swap with from 0 to 51 where total cards are 52
            temp = self.deck[num]               # Store the card at the random index temporarily
            self.deck[num] = self.deck[i]       # Swap the card at the random index with the current card
            self.deck[i] = temp                 # Place the temporarily stored card in the current position
        return self.deck                        # Return the shuffled deck


    def deal(self, how_many):                    # Method to deal a specified number of cards from the deck
        dealt = []                               # Initialize an empty list to hold dealt cards
        i = 0
        while i < how_many:                      # Loop to deal the specified number of cards
            dealt.append(self.deck.pop())        # Remove the last card from the deck and add it to the dealt list
            i += 1
        return Deck(dealt)                       # Return a new Deck object containing the dealt cards


    def card_list(self):                         # Method to return a list of cards currently in the deck
        a_card_list = []                         # Initialize an empty list to hold the cards
        for i in range(len(self.deck)):          # Loop through each card in the deck
            a_card_list.append(self.deck[i])     # Add each card to the a_card_list
        return a_card_list                       # Return the list of cards in the deck


    def __str__(self):                           # String representation of the Deck class
        return str(self.deck)                    # Return the string representation of the deck list