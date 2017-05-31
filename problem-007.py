"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
goal = 10001
n = 1

num = 2
step = 2

def is_prime(x):
    if x <= 1:

        return False
    elif x <= 3:

        return True
    elif not x % 2 or not x % 3:
        return False
    i = 5
    while i*i <= x:
        if (x % i == 0 or x % (i + 2) == 0):
            return False
        i += 6
    return True

tmp = 0
while n < goal+1:
    if is_prime(num):
        tmp = num
        n += 1
    num += 1

print(tmp)
