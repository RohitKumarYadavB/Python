# 7.Write a program to compute sin x for given x. The user should supply x and a positive integern. We compute the sine of x using the series and the computation should use all terms in the
#series up through the term involving xn sin x = x - x3/3! + x5/5! - x7/7! + x9/9! ........
n = int(input("Enter number: "))
x = int(input("Enter value of 'X': "))

res = 0
i = 1
p = 1
flag = 0
while i <= n:
    if flag:
        res -= (x * i) / p
    else:
        res += (x * i) / p
    flag = 1 - flag
    p *= (i + 1) * (i + 2)
    i += 2

print(f"Result: {res}")
