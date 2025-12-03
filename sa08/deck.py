# File: deck.py
# Author: Gift Christian
# Date: October 27, 2025
# Course: CS 1 - Introduction to Programming and Computation-02 By Professor Balkcom
# Description: This file contains the Deck class which represents a standard deck of playing cards.

from card import Card       # Import the Card class from card.py
from random import randint  # Import randint function for shuffling

class Deck:
    def __init__(self):         # Initialize the Deck class with an optional dealt parameter
        self.card_list = []     # Create a deck list, optionally starting with dealt cards


    def add_standard_cards(self):                    # Method to add standard 52 playing cards to the deck in a specific order
        for i in range(1, 14):                       # Loop through card values from 1 to 13
            self.card_list.append(str(Card(i, 1)))   # Add clubs to the deck
            self.card_list.append(str(Card(i, 2)))   # Add spades to the deck
            self.card_list.append(str(Card(i, 3)))   # Add diamonds to the deck
            self.card_list.append(str(Card(i, 4)))   # Add hearts to the deck


    def shuffle(self):                                  # Method to shuffle the deck randomly
        for i in range(len(self.card_list)):            # Loop through each card in the deck
            num = randint(0, 51)                        # Generate a random index to swap with from 0 to 51 where total cards are 52
            temp = self.card_list[num]                  # Store the card at the random index temporarily
            self.card_list[num] = self.card_list[i]     # Swap the card at the random index with the current card
            self.card_list[i] = temp                    # Place the temporarily stored card in the current position
        return self.card_list                           # Return the shuffled deck


    def deal(self, how_many):                                # Method to deal a specified number of cards from the deck
        dealt = Deck()                                       # Initialize an empty list to hold dealt cards
        i = 0
        while i < how_many:                                  # Loop to deal the specified number of cards
            dealt.card_list.append(self.card_list.pop())     # Remove the last card from the deck and add it to the dealt list
            i += 1
        return dealt                                         # Return a new Deck object containing the dealt cards


    def __str__(self):                                # String representation of the Deck class
        return str(self.card_list)                    # Return the string representation of the deck list