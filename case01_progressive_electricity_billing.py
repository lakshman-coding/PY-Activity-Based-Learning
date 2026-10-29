def energy_charge(units):
    if units <= 100:
        charge = units * 2
    elif units <= 300:
        charge = 100 * 2 + (units - 100) * 4
    else:
        charge = 100 * 2 + 200 * 4 + (units - 300) * 6
    return charge


def calculate_bill(units):
    fixed_charge = 100
    surcharge = 0
    rebate = 0

    bill = energy_charge(units) + fixed_charge

    if units > 500:
        surcharge = bill * 10 / 100
        bill = bill + surcharge

    if units < 100:
        rebate = 25
        bill = bill - rebate

    return bill


months = int(input("Enter number of months: "))
month_names = []
bills = []

for i in range(months):
    name = input("Enter month name: ")
    units = int(input("Enter units consumed: "))
    bill = calculate_bill(units)
    month_names.append(name)
    bills.append(bill)

print("\nMonthly Bills")
for i in range(months):
    print(month_names[i], ": Rs.", round(bills[i], 2))

for i in range(1, months):
    if bills[i - 1] != 0:
        increase = (bills[i] - bills[i - 1]) * 100 / bills[i - 1]
        if increase > 30:
            print("Unusual increase from", month_names[i - 1], "to", month_names[i])
