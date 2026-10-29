def calculate_deduction(gross):
    if gross <= 30000:
        deduction = gross * 5 / 100
    elif gross <= 50000:
        deduction = 30000 * 5 / 100
        deduction = deduction + (gross - 30000) * 10 / 100
    else:
        deduction = 30000 * 5 / 100
        deduction = deduction + 20000 * 10 / 100
        deduction = deduction + (gross - 50000) * 15 / 100
    return deduction


name = input("Enter employee name: ")
basic = float(input("Enter basic pay: "))
allowance = float(input("Enter allowances: "))
overtime_hours = float(input("Enter overtime hours: "))
overtime_rate = float(input("Enter overtime rate per hour: "))
incentive = float(input("Enter incentive: "))

overtime_pay = overtime_hours * overtime_rate
gross = basic + allowance + overtime_pay + incentive
deduction = calculate_deduction(gross)
net = gross - deduction

print("\nSALARY STATEMENT")
print("Employee:", name)
print("Basic Pay:", round(basic, 2))
print("Allowances:", round(allowance, 2))
print("Overtime Pay:", round(overtime_pay, 2))
print("Incentive:", round(incentive, 2))
print("Gross Salary:", round(gross, 2))
print("Deduction:", round(deduction, 2))
print("Net Salary:", round(net, 2))
