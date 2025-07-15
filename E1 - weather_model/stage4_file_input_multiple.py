import math

def solve(a, b, c):
    D = b**2 - 4*a*c
    if D < 0:
        return "No real solution"
    else:
        x1 = (-b + math.sqrt(D)) / (2*a)
        x2 = (-b - math.sqrt(D)) / (2*a)
        return f"{x1:.2f}, {x2:.2f}"

with open("input.txt", "r") as file:
    for i, line in enumerate(file):
        a, b, c = map(float, line.strip().split())
        result = solve(a, b, c)
        print(f"Equation {i+1}:", result)
