import math

a = 1
b = -3
c = 2

D = b**2 - 4*a*c

if D < 0:
    print("No real solution")
else:
    x1 = (-b + math.sqrt(D)) / (2*a)
    x2 = (-b - math.sqrt(D)) / (2*a)
    print("Solutions:", x1, x2)
