# fill in students grades
# vector for names
# matrix for grades
#everyhing starting with # is a comment, for reference

print("Student registration system")
print()

#   using a for loop to register students names
number_students = int(input("how many students are there?"))
students=list()
for student in range(number_students):
    name = input("Introduce student's name: ")
    students.append(name)

#   using a for loop to register subject names
number_subjects=int(input("How many subjects are there? "))
subjects=list()
for student in range(number_subjects):
    name = input("Introduce subject's name: ")
    subjects.append(name)


#   using while loop to register students' names
students = list()
add_students = True
while add_students:
    #ask for student name
    name = input("Introduce student's name: ")
    #add student name into students list() using function .append()
    students.append(name)
    #   ask for while's control variable if it will continue or not
    add_students=input("Type 'yes' to add more students, ENTER to exit students name register system ")

#   using while loop to register subjects' names
subjects=list()
subject = True
while subject:
    #   ask for subject name
    name = input("Introduce subjects's name: ")
    #   ask name into subjects list()
    subjects.append(name)
    #   ask for while's control variable if it will continue or not
    subject=input("Type 'yes' to add more subjects, ENTER to exit subject name register system ")


#   add each grade into each subject, and then the grades list into each student
#   create the empty matrix
class_grades=list()
for student in students:
    #   create empty grades list(), each iteration of the students [for] the list() is recreated
    student_grades = list()
    print("Student name: ",student)

    #   subjects [for] used to add each grade
    for subject in subjects:
        print("Register grades for ",subject,":", end=' ')

        #   get grade from the user
        grade=float(input(""))

        #   add grade into the student_grades list()
        student_grades.append(grade)

    #   add grades list() into the class grades list() (matrix)
    class_grades.append(student_grades)

#   add each students' grade into each subject, and then the grades list into each subject
#   create the empty matrix
class_grades=list()
for subject in subjects:
    #   create empty grades list, each iteration of the subjects [for] the list() is recreated
    subject_grades = list()
    print("Subject name: ",subject)
    for student in students:
        print("Register grades for ",student,":", end=' ')

        #   get grade from the user
        grade=float(input(""))

        #   add grade into the subject_grades list()
        subject_grades.append(grade)

    #   add grades list() into the class grades list() (matrix)
    class_grades.append(subject_grades)

class1 = [subjects,students,class_grades]
print(class1)

print(class1[0])
for i in len(students):
    print(class1[1][i],class1[2][i])