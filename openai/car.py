# python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.is_running = False

    def start(self):
        if not self.is_running:
            self.is_running = True
            print(f"The {self.year} {self.make} {self.model} is now running.")
        else:
            print(f"The {self.year} {self.make} {self.model} is already running.")

    def stop(self):
        if self.is_running:
            self.is_running = False
            print(f"The {self.year} {self.make} {self.model} has been stopped.")
        else:
            print(f"The {self.year} {self.make} {self.model} is already stopped.")

    def display_info(self):
        print(f"Car Info: {self.year} {self.make} {self.model}")

# Example usage
my_car = Car("Toyota", "Camry", 2020)
my_car.display_info()
my_car.start()
my_car.stop()