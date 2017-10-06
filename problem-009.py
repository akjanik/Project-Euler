n = 1000

# very simple brute force solution
def solution(n):
    for a in range(1, n):
        for b in range (1,n-1):
            c = n - a - b
            if a**2 + b**2 == c**2:
                return(a*b*c)

print(solution(n))
