
def solution(numbers):
    # TODO: implement solution here
    new = []
    n = len(numbers)
    for i in range(n):
        if numbers[i] >= 10:
            for j in range(0 , n):
                if str(numbers[i])[:: -1] == str(numbers[j]):
                    new.append((numbers[i], numbers[j]))
        else:
            for j in range(0 , n):
                if numbers[i] == int(str(numbers[j])[:: -1]):
                    new.append((numbers[i], numbers[j]))
    return new
    
numbers = [12, 21, 34, 56, 43, 65]
# numbers = []
# for i in range(0, 101):
    # numbers.append(i)

# print(len(solution(numbers)))
print(solution(numbers))
# print(numbers)