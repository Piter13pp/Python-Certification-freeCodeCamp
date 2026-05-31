#approach of using two previous values to calculate the required Fibonacci number
#from freeCodeCamp Lab: https://www.freecodecamp.org/learn/coding-interview-prep/algorithms-and-data-structures-algorithms/fibonacci-numbers
def fibonacci(n):
    sequence = [0, 1]
    if n <= 0:
        return 0
    if n == 1:
        return 1
    
    p2, p1 = 0, 1
    
    for _ in range(2, n + 1):
        curr = p1 + p2
        p2 = p1
        p1 = curr
    
    sequence.append(p1)    
    return p1

import math
#approach of using golden ratio to calculate the required Fibonacci number
#own idea of using different approach
def fibonacci_golden_ratio(n):
    x = (1 + math.sqrt(5)) / 2
    return round(pow(x, n) / math.sqrt(5))

#testing
n = 10
print(f"The {n}th Fibonacci number using two previous values approach: {fibonacci(n)}")
print(f"The {n}th Fibonacci number using golden ratio approach: {fibonacci_golden_ratio(n)}")