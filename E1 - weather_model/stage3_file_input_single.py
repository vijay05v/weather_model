import math

with open("input.txt", "r") as file:
    line = file.readline()
    a, b, c = map(float, line.strip().split())

D = b**2 - 4*a*c

if D < 0:
    print("No real solution")
else:
    x1 = (-b + math.sqrt(D)) / (2*a)
    x2 = (-b - math.sqrt(D)) / (2*a)
    print("Solutions:", x1, x2)
