# 8. Write a program to compute cosine of x. The user should supply x and a positive integer n.We compute the cosine of x using the series and the computation should use all terms in the
# series up through the term involving xn cos x = 1 - x2/2! + x4/4! - x6/6! ....
n = int(input("Enter number: "))
x = int(input("Enter value of 'X': "))

if n == 1:
    print(f"Result: {1.0}")
else:
    res = 1
    i = 2
    p = 2
    flag = 0
    while i <= n:
        if flag:
            res += (x * i) / p
        else:
            res -= (x * i) / p
        flag = 1 - flag
        p *= (i + 1) * (i + 2)
        i += 2

    print(f"Result: {res}")
