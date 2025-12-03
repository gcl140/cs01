# original_string = 123
# reversed_string = str(original_string)[::-1]
# print(reversed_string)  # Output: olleh
# print(reversed_string == str(321))  # Output: olleh



def solution(numbers):
    # TODO: implement solution here
    new = []
    n = len(numbers)
    for i in range(n):
        if numbers[i] >= 10:
            for j in range(i + 1, n):
                # print(i, j)
                if str(numbers[i])[:: -1] == str(numbers[j]):
                    # print("True")
                    print(i, j, "works")
                    new.append((numbers[i], numbers[j]))
        else:
            for j in range(i + 1, n):
                print("0" + (str(numbers[i])) + "iiiiii")
                print((str(numbers[j])) + "jjjjj")
                if numbers[i] == int(str(numbers[j])[:: -1]):
                    print((str(numbers[j])) + "kk")
                    # print("True")
                    new.append((numbers[i], numbers[j]))
    return new
    # pass
    
# numbers = [12, 21, 34, 56, 43, 65]
numbers = []
for i in range(0, 40):
    numbers.append(i)

print(len(solution(numbers)))
print(solution(numbers))
print(numbers)