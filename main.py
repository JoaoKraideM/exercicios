import math

def bhaskara(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        return "No real roots"
    elif delta == 0:
        x = -b / (2*a)
        return f"One root: {x}"
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return f"Two roots: {x1} and {x2}"

def main():
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    result = bhaskara(a, b, c)
    print(result)

if __name__ == "__main__":
    main()