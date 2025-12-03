from card import Card
from random import randint

class Deck:
    def __init__(self, dealt=None):
        self.clubs = []
        self.spades = []
        self.diamonds = []
        self.hearts = []
        if dealt == None:
            self.deck = []
        else:
            self.deck = [] + dealt


    def add_standard_cards(self):
        for i in range(1, 14):
            self.clubs.append(str(Card(i, 1)))
            self.spades.append(str(Card(i, 2)))
            self.diamonds.append(str(Card(i, 3)))
            self.hearts.append(str(Card(i, 4)))
        self.deck = self.clubs + self.spades + self.diamonds + self.hearts


    def shuffle(self):
        for i in range(len(self.deck)):
            num = randint(0, 51)
            temp = self.deck[num]
            self.deck[num] = self.deck[i]
            self.deck[i] = temp
        return self.deck

    
    def deal(self, how_many):
        dealt = []
        i = 0
        while i < how_many:
            dealt.append(self.deck.pop())
            i += 1
        return Deck(dealt)

    def card_list(self):
        a_card_list = []
        for i in range(len(self.deck)):
            a_card_list.append(self.deck[i])
        return a_card_list
    
    def __str__(self):
        return str(self.deck)

if __name__ == "__main__":
    deck = Deck()
    deck.add_standard_cards()
    print(type(deck.deal(4)))
    print(type([0, 1, 2]))
    for card in deck.deal(5).card_list():
        print(card)