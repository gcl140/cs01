def a(r):
    x = 5
    y = 2
    return 2 * r

def b():
    x = 2
    z = 9
    return z + a(7)

def c(m, n):
    p = b() + a(m) + n
    return p

x = c(2. 3)

