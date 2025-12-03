from card import Card
from random import randint

class Deck:
    def __init__(self):
        self.clubs = []
        self.spades = []
        self.diamonds = []
        self.hearts = []
        self.deck = []


    def add_standard_cards(self):
        for i in range(1, 14):
            self.clubs.append(str(Card(i, 1)))
            self.spades.append(str(Card(i, 2)))
            self.diamonds.append(str(Card(i, 3)))
            self.hearts.append(str(Card(i, 4)))

        self.deck = self.clubs + self.spades + self.diamonds + self.hearts
        # self.deck = [self.clubs , self.spades , self.diamonds , self.hearts]

    def swap(glist, r, c, rr, cc):
        temp = glist[r][c]
        glist[r][c] = glist[rr][cc]
        glist[rr][cc] = temp

    def shuffle(self):
        # for item in range(len(self.deck)):
        #     if self.deck[item] ==
        new = self.deck
        
        for i in range(len(new)):
            # for j in range(len(self.deck[i])):
            num = randint(0, 52)
            temp = i
            i = num
            num = temp
            
            
            
        pass
    
    def __str__(self):
        # return str(self.clubs) + str(self.spades) + str(self.diamonds) + str(self.hearts)
        # return str(self.clubs) + str(self.spades) + str(self.diamonds) + str(self.hearts)
        return str(self.deck)
    

if __name__ == "__main__":
    deck = Deck()
    deck.add_standard_cards()
    print(deck)