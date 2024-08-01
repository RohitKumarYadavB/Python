#7  Write a python program to calculate the sum of natural numbers up to a certain range
def main():
    sum = 0
    range_val = int(input("Enter the range: "))
    
    for i in range(1, range_val + 1):
        sum += i
    
    print(f"Sum of all natural numbers up to {range_val} is: {sum}")

if __name__ == "__main__":
    main()