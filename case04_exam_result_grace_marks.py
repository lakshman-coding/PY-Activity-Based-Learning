number = int(input("Enter number of subjects: "))
maximum = int(input("Enter maximum mark for each subject: "))
subjects = []
final_marks = []
total = 0
passed_all = True

for i in range(number):
    subject = input("Enter subject name: ")
    mark = int(input("Enter mark: "))
    final_mark = mark
    grace = 0

    if mark >= 40:
        print("Passed without grace marks")
    elif mark >= 35:
        grace = 40 - mark
        if grace <= 5:
            final_mark = mark + grace
            print("Grace marks used:", grace)
        else:
            passed_all = False
    else:
        passed_all = False

    if final_mark > maximum:
        final_mark = maximum

    if final_mark < 40:
        passed_all = False

    subjects.append(subject)
    final_marks.append(final_mark)
    total = total + final_mark

percentage = total * 100 / (number * maximum)

if passed_all == False:
    classification = "FAIL"
elif percentage >= 75:
    classification = "DISTINCTION"
elif percentage >= 60:
    classification = "FIRST CLASS"
elif percentage >= 50:
    classification = "SECOND CLASS"
else:
    classification = "PASS"

print("\nRESULT")
for i in range(number):
    print(subjects[i], ":", final_marks[i])
print("Total:", total)
print("Percentage:", round(percentage, 2))
print("Classification:", classification)
