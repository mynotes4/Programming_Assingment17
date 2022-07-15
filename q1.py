"""
Question1. Create a function that takes three arguments a, b, c and returns the sum of the
numbers that are evenly divided by c from the range a, b inclusive.
Examples
evenly_divisible(1, 10, 20) ➞ 0
# No number between 1 and 10 can be evenly divided by 2
evenly_divisible(1, 10, 2) ➞ 30
# 2 + 4 + 6 + 8 + 10 = 30
"""

def evenly_divisible(a,b,c):
    s = 0
    for i in range(a,b+1):
        if i % c == 0:
            s = s + i
    return s

a = int(input("Enter no 1 "))
b = int(input("Enter no 1 "))
c = int(input("Enter no 1 "))
s = evenly_divisible(a,b,c)
print("evenly_divisible(" ,a,",",b,",",c,") ➞ " ,s)