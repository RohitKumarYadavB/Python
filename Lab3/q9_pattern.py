# 9. Print the pattern upto N Lines:

# .
#/_\

#  .
# / \
#/___\

#   .
#  / \
# /   \
#/_____\

#N=2 N=3 N=4


n = int(input("Enter number of rows: "))
for i in range(n):
    spaces = " " * (n - i - 1)
    if i == 0:
        print(spaces + ".")
    elif i == n - 1:
        print("/" + "_" * (2 * i - 1) + "\\")
    else:
        print(spaces + "/" + " " * (2 * i - 1) + "\\")
