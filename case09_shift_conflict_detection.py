number = int(input("Enter number of shifts: "))
shifts = []

for i in range(number):
    name = input("Enter employee name: ")
    day = input("Enter day: ")
    start = int(input("Enter starting hour: "))
    end = int(input("Enter ending hour: "))
    shift = (name, day, start, end)
    shifts.append(shift)

found_conflict = False

for i in range(number):
    name1, day1, start1, end1 = shifts[i]
    for j in range(i + 1, number):
        name2, day2, start2, end2 = shifts[j]

        if name1 == name2 and day1 == day2:
            if start1 < end2 and start2 < end1:
                print("Conflict:", name1, "on", day1)
                print("Shift 1:", start1, "to", end1)
                print("Shift 2:", start2, "to", end2)
                found_conflict = True

if found_conflict == False:
    print("No shift conflicts found")
