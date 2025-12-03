
def solution(numbers):
    # TODO: implement solution here
    new = []
    n = len(numbers)
    for i in range(n):
        if numbers[i] >= 10:
            for j in range(0 , i):
                if str(numbers[i])[:: -1] == str(numbers[j]):
                    new.append((numbers[i], numbers[j]))
            for j in range(i , n):
                if str(numbers[i])[:: -1] == str(numbers[j]):
                    new.append((numbers[i], numbers[j]))
                    # new.append("ukoko")
                    # print((numbers[j], numbers[i]), "yjis")
        else:
            for j in range(0 , i):
                if numbers[i] == int(str(numbers[j])[:: -1]):
                    new.append((numbers[i], numbers[j]))
            for j in range(i , n):
                if numbers[i] == int(str(numbers[j])[:: -1]):
                    new.append((numbers[i], numbers[j]))
            # print("dsadsad")

    return new
    
# numbers = [12, 21, 34, 43, 56, 65]
numbers = []
for i in range(0, 101):
    numbers.append(i)

print(len(solution(numbers)))
print(solution(numbers))
# print(numbers)


# [(12, 21), (21, 12), (34, 43), (43, 34), (56, 65), (65, 56)]

# [(12, 21), (21, 12), (34, 43), (43, 34), (56, 65), (65, 56)]

# [(12, 21), (21, 12), (34, 43), (56, 65), (43, 34), (65, 56)]


# [(21, 12), (21, 12), (43, 34), (65, 56), (43, 34), (65, 56)]