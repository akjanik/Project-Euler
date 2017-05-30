"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""
import itertools
a, b = range(999, 99, -1), range(999, 99, -1)

largest = 0
pairs = []

for i in a:
    for j in b:
        num = i*j

        # speed up by not checking smaller numbers
        if num <= largest:
            break
        c = str(num)
        if c[:len(c)//2] ==  c[len(c)//2:][::-1] and num > largest:
            largest = num
            pairs.append((i,j))
            print(largest, i, j)

print(largest)
print(pairs)
