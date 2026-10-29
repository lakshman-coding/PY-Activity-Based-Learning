def tax_rate(category):
    if category == "food":
        return 5
    elif category == "clothing":
        return 12
    elif category == "electronics":
        return 18
    else:
        return 0


number = int(input("Enter number of products: "))
subtotal = 0
all_tax = 0
names = []
amounts = []

for i in range(number):
    name = input("Enter product name: ")
    category = input("Enter category (food/clothing/electronics): ")
    price = float(input("Enter unit price: "))
    quantity = int(input("Enter quantity: "))

    amount = price * quantity
    tax = amount * tax_rate(category) / 100
    subtotal = subtotal + amount
    all_tax = all_tax + tax
    names.append(name)
    amounts.append(amount + tax)

if subtotal >= 5000:
    discount = subtotal * 10 / 100
else:
    discount = 0

if discount > 1000:
    discount = 1000

final_amount = subtotal + all_tax - discount

print("\nITEMIZED INVOICE")
for i in range(number):
    print(names[i], ": Rs.", round(amounts[i], 2))
print("Subtotal: Rs.", round(subtotal, 2))
print("Tax: Rs.", round(all_tax, 2))
print("Discount: Rs.", round(discount, 2))
print("Final Amount: Rs.", round(final_amount, 2))
