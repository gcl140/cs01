from card import Card
from random import randint

class Deck:
    def __init__(self, dealt=[]):
        self.clubs = []
        self.spades = []
        self.diamonds = []
        self.hearts = []
        self.deck = [] + dealt


    def add_standard_cards(self):
        for i in range(1, 14):
            self.clubs.append(str(Card(i, 1)))
            self.spades.append(str(Card(i, 2)))
            self.diamonds.append(str(Card(i, 3)))
            self.hearts.append(str(Card(i, 4)))

        self.deck = self.clubs + self.spades + self.diamonds + self.hearts


    def shuffle(self):
        new = self.deck
        for i in range(len(new)):
            num = randint(0, 51)
            temp = new[num]
            new[num] = new[i]
            new[i] = temp
        return new

    
    def deal(self, n):
        dealt = []
        what = self.shuffle()
        i = 0
        while i < n:
            dealt.append(what.pop())
            i += 1
        card_list = Deck(dealt)
        return card_list

    def card_list(self):
        return self.deal()
    
    def __str__(self):
        return str(self.deck)
    

if __name__ == "__main__":
    deck = Deck()
    deck.add_standard_cards()
    # print(deck)
    print(deck.deal(4))