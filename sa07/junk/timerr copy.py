from counter import Counter

class Timer:
    def __init__(self, hours, minutes, seconds):
        self.hours = Counter(24, hours)
        self.minutes = Counter(60, minutes)
        self.seconds = Counter(60, seconds)

    def tick(self):
        if self.seconds.tick():
            if self.minutes.tick():
                self.hours.tick()
                # if self.hours.tick():
        #             self.hours.value = self.hours.limit - 1
        #             self.minutes.value = self.minutes.limit - 1
        #             self.seconds.value = self.seconds.limit - 1
        #             return False
                
        # return True

    def is_zero(self):
        return self.hours.value == 0 and self.minutes.value == 0 and self.seconds.value == 0
        
    def __str__(self):
        return str(self.hours) + ":" + str(self.minutes) + ":" + str(self.seconds)