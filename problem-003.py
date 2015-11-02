
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

def find_prime_factors(z):
    ret = []
    n = 5
    while n*n <= z:
        if is_prime(n):
            if z % n == 0:
                ret.append(n)
        n += 1
    return ret

print find_prime_factors(600851475143)
