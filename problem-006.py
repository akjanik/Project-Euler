"""
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

n = 100
sum_squares = 0
for i in range(n+1):
    sum_squares += i**2

sum_100 = sum(range(n+1))
squares_sum = sum_100**2
print(squares_sum - sum_squares)
