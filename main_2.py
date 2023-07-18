import math

a = int(input("Enter coefficient a: "))
b = int(input("Enter coefficient b: "))
c = int(input("Enter coefficient c: "))

D = b ** 2 - 4 * a * c

if D > 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print("The equation has two distinct real roots:")
    print("x1 =", x1)
    print("x2 =", x2)
elif D == 0:
    x = -b / (2 * a)
    print("The equation has one real root:")
    print("x =", x)
else:
    real_part = -b / (2 * a)
    imaginary_part = math.sqrt(-D) / (2 * a)
    print("The equation has two complex roots:")
    print("x1 =", real_part, "+", imaginary_part, "i")
    print("x2 =", real_part, "-", imaginary_part, "i")