# 2.: Write a python program to calculate factorial of 12. 
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
result=factorial(12)
print(f"The factorial of 12 is {result}")