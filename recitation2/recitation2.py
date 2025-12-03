def check_factors(m, n, p):
    if m > n:
        i = n
        while i < m:
            if p % i == 0:
                print(i)
            i += 1
    else:
        i = m
        while i < n:
            if p % i == 0:
                print(i)
                # print(" is a factor of")
            i += 1

check_factors(10, 5, 200)

def check_factors_multipes(m, n):
    if n >= m:
        i = m
        while i <= n:
            if n % i == 0 and i % m == 0:
                print(i)
            i += 1

check_factors_multipes(5, 35)