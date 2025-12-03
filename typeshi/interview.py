def checkpalindrome(stringi):
    i = 0
    j = len(stringi) - 1
    while i < j:
        if stringi[i] != stringi[j]:
            return False
        i += 1
        j -= 1
    return True


# print(checkpalindrome("racecaar"))


def adjacent_elements_product(numbers):
    # max_product = numbers[0] * numbers[1]
    max_product = 0
    for i in range(len(numbers) - 1) : # end just before last index
            j = numbers[i + 1]            
            if numbers[i] * j > max_product:
                max_product = numbers[i] * j
    return max_product
    

def any_elements_product(numbers):
    max_product = numbers[0] * numbers[1]
    for i in range(len(numbers) - 1) : # end just before last index
            for j in range(i + 1, len(numbers)):         
                if numbers[i] * numbers[j] > max_product:
                    max_product = numbers[i] * numbers[j]
    return max_product
    



# print(adjacent_elements_product([3, 6, -2, -5, 7, 3]))
# print(any_elements_product([3, 6, -2, -5, 7, 3]))

def makearrayconsecutive(lists):
    #  difference = 
    new_list = []
    min_number = lists[0]
    for i in range(len(lists) - 1):
          for j in range(i + 1, len(lists)):
            if lists[j] < min_number:
                print(lists[i])
                print(lists[j])
                min_number = lists[j]
                print(min_number)

    print(min_number)

# makearrayconsecutive([3, 6, -2, -5, 7, 3])
# print(makearrayconsecutive([3, 6, -2, -5, 7, 3]))


def makearrayconsecutive(lists):
    new_list = []
    i = 0

    while i < len(lists):
        min_number = lists[0]
        for i in range(len(lists) - 1):
            for j in range(i + 1, len(lists)):
                if lists[j] < min_number:
                    min_number = lists[j]
        remover =  min_number

        print(remover)
        print(lists)
        new_list.append(remover)
        print(new_list)
        lists.remove(remover)
        print(lists)
        print(new_list[len(new_list) - 1])

    difference = new_list[len(new_list) -1 ] - new_list[0] - len(new_list) + 1
    return print(f"number of statues missing is {difference}") 

# makearrayconsecutive([3, 6, -2, -5, 9, 3])
makearrayconsecutive([3,2])