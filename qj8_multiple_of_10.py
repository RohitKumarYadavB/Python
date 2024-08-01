#8 Write a python program to print all multiple of 10 between a given interval. 
def main():
    start = int(input("Enter the starting interval: "))
    end = int(input("Enter the ending interval: "))
    
    print(f"Multiples of 10 between {start} and {end}:")
    
    first_multiple = start if start % 10 == 0 else (start // 10 + 1) * 10
    
    for i in range(first_multiple, end + 1, 10):
        print(i)

if __name__ == "__main__":
    main()
