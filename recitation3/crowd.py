from face import Face
from cs1lib import *
from random import randint

class Crowd:
    def __init__(self, n):
        self.face = []
        if n >= 1:
            for i in range(n):
                self.face.append(Face(randint(20, 380), randint(20, 380), randint(1, 100)))

    def lookat(self, mx, my):
        for i in range(len(self.face)):
            self.face[i].lookat(mx, my)

    def draw(self):
        for i in range(len(self.face)):
            self.face[i].draw()

    def __str__(self):
        return str(self.face)

if __name__ == "__main__":
    f = Crowd(5)
    print(f)