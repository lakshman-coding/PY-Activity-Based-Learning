students = int(input("Enter number of students: "))
subjects = int(input("Enter number of subjects: "))
marks = []
names = []

for i in range(students):
    name = input("Enter student name: ")
    names.append(name)
    row = []
    for j in range(subjects):
        mark = int(input("Enter mark: "))
        row.append(mark)
    marks.append(row)

student_totals = []
top_index = 0

for i in range(students):
    total = 0
    for j in range(subjects):
        total = total + marks[i][j]
    student_totals.append(total)
    average = total / subjects
    print(names[i], "Total:", total, "Average:", round(average, 2))

    if student_totals[i] > student_totals[top_index]:
        top_index = i

print("Top student:", names[top_index])

for j in range(subjects):
    subject_total = 0
    for i in range(students):
        subject_total = subject_total + marks[i][j]
    subject_average = subject_total / students
    print("Subject", j + 1, "average:", round(subject_average, 2))
    if subject_average < 50:
        print("Subject", j + 1, "has low average performance")
