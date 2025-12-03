from food import Food

class Fridge:
    def __init__(self):
        self.food_list = [] 

    def add(self, fooditem):
        self.food_list.append(fooditem)

    def find_fruit(self):
        return self.find_by_type("fruit")
    
    def find_cheese(self):
        return self.find_by_type("cheese")

    def find_by_type(self, t):
        l = []
        # fruit_list = []
        for food in self.food_list:
            # if food.is_fruit():
            if food.type == t:
                l.append(food)
        return l

        # return fruit_list

    # def __str__(self):
    #     return f"Fridge with {len(self.food_list)} items are " + ", ".join(str(f) for f in self.food_list)

# fr = Fridge()