"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

#Brute force
a = 2520
step = 20
cond = True
while cond:
    a += step
    for i in range(20,0, -1):
        if a % i:
            break
            cond = True
        else:
            if i == 2:
                cond = False
                print (a)
