def lcm(a, b):
    if a % b:
        return lcm(a, a % b)
    else:
        return b


a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
if a < b:
    a, b = b, a
print(f"LCM of {a} and {b} is: {a*b//lcm(a,b)}")
