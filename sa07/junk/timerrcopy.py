from counter import Counter

class Timer:
    def __init__(self, hours, minutes, seconds):
        self.hours = Counter(24, hours)
        self.minutes = Counter(60, minutes)
        self.seconds = Counter(60, seconds)

    def tick(self):
        self.seconds.value -= 1
        if self.seconds.value < 0:
            self.seconds.value = self.seconds.limit - 1
            self.minutes.value -= 1

            if self.minutes.value < 0:
                self.minutes.value = self.minutes.limit - 1
                self.hours.value -= 1

                if self.hours.value < 0:
                    self.hours.value = self.hours.limit - 1
                    self.minutes.value = self.minutes.limit - 1
                    self.seconds.value = self.seconds.limit - 1
                    return False
                
        return True

    def is_zero(self):
        if self.hours.value == 0 and self.minutes.value == 0 and self.seconds.value == 0:
            return True
        
    def __str__(self):
        return str(self.hours) + ":" + str(self.minutes) + ":" + str(self.seconds)