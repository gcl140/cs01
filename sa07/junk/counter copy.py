class Counter:
    def __init__(self, limit, initial=0, min_digits = 1):
        self.limit = limit
        self.min_digits = min_digits
        if 0 <= initial <= limit - 1:
            self.value = initial
        else:
            print("Error: Initial Value is out of range")
            self.value = limit - 1

    def tick(self):
        self.value -= 1
        if self.value < 0:
            self.value = self.limit - 1
            return True
        return False
            
    def get_value(self):
        return int(self.value)
    
    def __str__(self):
        value = str(self.value)
        if len(value) < self.min_digits:
            zeros_needed = self.min_digits - len(value)
            return zeros_needed * "0" + value
        else:
            return str(self.value)
        
    
        

        # if len(str(self.counter_value)) < self.min_digits:
        #     start = ""
        #     for i in range(self.min_digits - len(str(self.counter_value))):
        #         start = start + str(0)
        #     return start + str(self.counter_value)
