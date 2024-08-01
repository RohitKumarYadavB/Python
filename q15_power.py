# 15. Write a Python program that prompts the user to enter a base number and an exponent,
# and then calculates the power of the base to the exponent. The program should not use the
# exponentiation operator (**) or the math.pow() function.
b = int(input("Enter Base: "))
copy = b
e = int(input("Enter Exponent: "))
temp = e

if e == 0:
    result = 1
else:
    result = 1
    while e > 0:
        result *= b
        e -= 1

print(f"{copy} to the Power of {temp} is: {result}")
