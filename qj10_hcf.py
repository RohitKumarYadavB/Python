#10 Write a python program to find HCF of two Numbers. 
def main():
    hcf = 0
    
    num1 = int(input("Enter the 1st number: "))
    num2 = int(input("Enter the 2nd number: "))
    
    for i in range(1, min(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            hcf = i
            
    print("HCF is:", hcf)

if __name__ == "__main__":
    main()
