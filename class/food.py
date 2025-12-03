
class Food:
    def __init__(self, myname, mytype, mycal):
        self.name = myname
        self.type = mytype
        self.calories = mycal

    def is_fruit(self):
        return self.type == "fruit"

    def __str__(self):
        return f"{self.name}, {self.type}, {self.calories}"


if __name__ == "__main__":
    from fridge import Fridge
    fridge = Fridge()

    apple = Food("apple", "fruit", 100)
    banana = Food("banana", "fruit", 150)
    carrot = Food("carrot", "vegetable", 50)

    fridge.add(apple)
    fridge.add(banana)
    fridge.add(carrot)
    fridge.add(Food("Cheddar", "cheese", 200))
    print(fridge.food_list)
    print("All cheese in fridge:")
    for cheese in fridge.find_cheese():
        print(cheese)
