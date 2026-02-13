#vector for subjects 
subjects_name = ["German","Math","Chemistry", "History"]
#add students
more_students = "yes"
students_names = list()
while more_students == "yes":
    #ask for student name
    name = input("student name: ")

    #add name into list variable for students names
    students_names.append(name)

    #ask if more students are to be added
    more_students=input("Are you adding more students yes/no? ")

#add grades for each student 
class_list = list() #this is the matrix
for student in students_names:
    print(student)
    grades_list=list () #add here grades for each subject, a list is students grades for all subjects
    for subject in subjects_name:
        print(subject)
        grade=int(input("add grade for subject"))
        grades_list.append(grade)
    class_list.append(grades_list)

print(class_list)
counter = 0
for row in class_list:
    print(students_names[counter],row)
    counter+=1