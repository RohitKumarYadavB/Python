#6 : Write a python program to find all roots of a quadratic equation >>Source Code: 
import cmath

def main():
    print("Enter the quadratic equation (ax^2 + bx + c):")
    a = float(input("Enter the value of a: "))
    b = float(input("Enter the value of b: "))
    c = float(input("Enter the value of c: "))
    
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
        root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
        print("Roots are real and different")
        print("Root 1:", root1.real)
        print("Root 2:", root2.real)
    elif discriminant == 0:
        root = -b / (2 * a)
        print("Roots are real and the same")
        print("Root:", root)
    else:
        real_part = -b / (2 * a)
        imaginary_part = cmath.sqrt(discriminant) / (2 * a)
        print("Roots are complex and different")
        print("Root 1:", real_part + imaginary_part)
        print("Root 2:", real_part - imaginary_part)

if __name__ == "__main__":
    main()