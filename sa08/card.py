# File: card.py
# Author: Gift Christian
# Date: October 27, 2025
# Course: CS 1 - Introduction to Programming and Computation-02 By Professor Balkcom
# Description: This file contains the Card class which represents a playing card.

class Card:
    def __init__(self, qty, suit):      # Initialize the Card class with quantity and suit
        if qty == 11:
            self.count = "Jack"         # Assign "Jack" for quantity 11
        elif qty == 12:
            self.count = "Queen"        # Assign "Queen" for quantity 12
        elif qty == 13:
            self.count = "King"         # Assign "King" for quantity 13
        else:
            self.count = qty            # Assign numeric value for other quantities
        if suit == 1:
            self.suite = "clubs"        # Assign "clubs" for suit 1
        elif suit == 2:
            self.suite = "spades"       # Assign "spades" for suit 2
        elif suit == 3:
            self.suite = "diamonds"     # Assign "diamonds" for suit 3
        elif suit == 4:
            self.suite = "hearts"       # Assign "hearts" for suit 4    
        else:
            self.suite = "unknown/ joker"   # Assign "unknown/ joker" for invalid suit values
    
    def __str__(self):
        return str(self.count) + " of " + self.suite    # String representation of the Card class
        