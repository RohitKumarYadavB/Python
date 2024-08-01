#9 : Write a python program to generate multiplication table. 
def main():
    num = int(input("Enter the number: "))
    
    for i in range(1, 11):
        print(f"{num} * {i} = {num * i}")

if __name__ == "__main__":
    main()