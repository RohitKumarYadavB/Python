# 12. Write a program in Python that prompts the user to input a number and prints its multiplication table.
n = int(input("Enter Number: "))

for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")
