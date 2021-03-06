"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""


import math
import time


limit = 2000000

t0 = time.time()
# initial listof13
primes = [2]

# find all prime numbers below 2 000 000 (not included upper bound)
for number in range(3, 2000000, 2):
    if all(number % i != 0 for i in range(2, int(math.sqrt(number)) + 1)):
       primes.append(number)

# sum up. Takes a while as it is a naive approach
sol = sum(primes)
t1 = time.time()
total = t1 - t0
print("Naive solution: {} in time: {}".format(sol, total))

# The sieve of Eratosthenes
t0 = time.time()
crosslimit = int(math.sqrt(limit))
sieve = [False]*limit

for n in range(4, limit, 2):
    sieve[n] = True

for n in range(3, crosslimit, 2):
    if not sieve[n]:
        for m in range(n*n, limit, 2*n):
            sieve[m] = True

solution_era = 0
for n in range(2, limit):
    if not sieve[n]:
        solution_era += n

t1 = time.time()
total = t1-t0
print("Sieve solution: {} in time: {}".format(solution_era, total))


# Improved sieve
t0 = time.time()
sievebound = int((limit - 1)/2)
sieve  = [False]*sievebound
crosslimit = int( ( math.floor(math.sqrt(limit)) - 1 ) / 2)

for i in range(1, crosslimit):
    if not sieve[i]:
        for j in range(2*i*(i+1), sievebound, 2*i+1):
            sieve[j] = True

solution_improved_sieve = 2
for i in range(1, sievebound):
    if not sieve[i]:
        solution_improved_sieve += (2*i+1)

t1 = time.time()
total = t1-t0
print("Improved sieve solution: {} in time: {}".format(solution_improved_sieve, total))
