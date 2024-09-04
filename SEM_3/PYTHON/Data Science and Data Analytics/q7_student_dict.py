student = {
 'first_name': 'Vishal',
 'last_name': 'Parui',
 'gender': 'Male',
 'age': 23,
 'marital_status': 'Single',
 'skills': ['React Js', 'Web Development'],
 'country': 'India',
 'city': 'Howrah',
 'address': '62/3/1 Tanti Para Lane'
}
length_of_student_dict = len(student)
print("Length of the student dictionary:", length_of_student_dict)
skills = student['skills']
print("Skills:", skills)
print("Data type of skills:", type(skills))
student['skills'].extend(['Cloud Computing', 'Backend Development'])
print("Modified skills:", student['skills'])
keys_list = list(student.keys())
print("Dictionary keys:", keys_list)
values_list = list(student.values())
print("Dictionary values:", values_list)
student_items = list(student.items())
print("List of tuples (items):", student_items)
del student['marital_status']
print("Dictionary after deleting 'marital_status':", student)
del student
try:
 print(student)
except NameError:
 print("The student dictionary has been deleted.")
