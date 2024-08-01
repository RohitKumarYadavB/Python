# 14. Print the series upto N terms: 1,2,6,24,120,720 …
n = int(input("Enter Number of Terms: "))

a = 1
for i in range(1, n + 1):
    a *= i
    print(a, end=" ")
