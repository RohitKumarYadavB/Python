# 13. Write a Python program to print the first 6 terms of a geometric sequence starting with 2 and having a common ratio of 3.

a = 2
r = 3
print("Geometric Progression: ")
for i in range(6):
    print(a, end=" ")
    a *= r
