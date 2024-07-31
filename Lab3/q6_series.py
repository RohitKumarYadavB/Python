# 6.Compute the sum up to n terms in the series 1 - 1/2 + 1/3 - 1/4 + 1/5 -... 1/n where n is a positive integer and input by user.
n = int(input("Enter the number of terms: "))
sums = 0
for i in range(1, n + 1):
    if i % 2:
        sums += 1 / i
    else:
        sums -= 1 / i

print(f"Result: {sums}")
