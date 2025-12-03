from math import sqrt
# if one number is an integer factor of another number
# print( 7 * ((6.02e23 + 1) - (6.02e23)))


def is_factor(num, factor):
    return num % factor == 0


# print(is_factor(10, 3))

the_number = 10000
possible_factor = 5
EPS = 1e-6

# if the_number % possible_factor == 0:
#     print("divisible")
# else:
#     print("indivisible")
# if the_number % possible_factor != 0:
#     print("indivisible")

# print ("the remainder is " + str(the_number % possible_factor))

#can check prime numbers
def count_factors(the_number):
    factor_count = 2
    possible_factor = 2
    while possible_factor <= sqrt(the_number) + EPS:
        if is_factor(the_number, possible_factor):
            print("divisible: " + str(possible_factor))
            other = the_number // possible_factor
            print("divisible: " + str(other))
            factor_count += 2
        possible_factor += 1

    if sqrt(the_number) * sqrt(the_number) == the_number:
        factor_count -= 1
    return factor_count

print(count_factors(23))
# print ("the remainder is " + str(the_number % possible_factor))

#if factors are greater than 3 then abort, no need to finish the whole thing
def is_prime(the_number):
    possible_factor = 2
    while possible_factor <= sqrt(the_number) + EPS:
        if is_factor(the_number, possible_factor):
            return False
        possible_factor += 1
    return True

print(count_factors(23))
print(is_prime(23))

prime = 2
MAX_PRIME = 100
while prime < MAX_PRIME:
    if is_prime(prime):
        print(prime)
    prime += 1


pi = 3.14
def circumf(r):
    global pi #... im going to change the pi into the next line
    pi = 4
    return 2 * pi * r

def area(r):
    return pi * r * r

print(area(4))