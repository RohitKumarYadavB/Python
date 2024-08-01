#5 : Admission to a professional course is subject to the following conditions: 
# (a)	marks in Mathematics >= 60 	 	 	(c) marks in Chemistry >=40  
# (b)	marks in Physics >=50   	 	 	(d) Total in all 3 subjects >=200 
#	  	 	 	 	 	 	 	(Or) Total in Maths & Physics>=150 
# Given the marks in the 3 subjects of n (user input) students, write a program to process the applications to list the eligible candidates 

def is_eligible(marks):
    total = marks[0] + marks[1] + marks[2]
    return (marks[0] >= 60 and marks[1] >= 50 and marks[2] >= 40 and total >= 200) or (marks[0] + marks[1] >= 150)

def main():
    n = int(input("Enter the number of students: "))
    marks = []

    for i in range(n):
        print(f"Enter the marks of student no. {i + 1}")
        maths = int(input("Maths: "))
        physics = int(input("Physics: "))
        chemistry = int(input("Chemistry: "))
        marks.append([maths, physics, chemistry])

    print("The eligible candidates are:")
    for i in range(n):
        if is_eligible(marks[i]):
            print(f"Student: {i + 1}")

if __name__ == "__main__":
    main()
