from math import sqrt

def solution(numbers):
    # TODO: implement this function
    n = len(numbers)
    pairs = []
    for i in range(n):
        pairs.append((numbers[i], round(sqrt(numbers[i] * numbers[len(numbers) - 1 - i]) , 2)))
        
    return pairs
        

umbers = []
for i in range(0, 101):
    umbers.append(i)

print(umbers)
    
    
print(solution(umbers))