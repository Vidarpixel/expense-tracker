# Expense Tracker - Installment 3
# Author: Asher Leigh Z. Maguad
# A expense tracker project.

print("=" * 40)
print("\t     EXPENSE TRACKER")
print("\tKnow where your money goes.")
print("=" * 40)

print("\nMAIN MENU")
print(" [1] Add an expense\t\t(coming soon)")
print(" [2] View all expenses\t\t(coming soon)")
print(" [3] Show total spent\t\t(coming soon)")
print(" [4] Exit\t\t\t(coming soon)")

name = input("\nWhat's your name? ")
print(f"Welcome, {name}! Let's log two expenses.\n")

subtotal = 0
item1 = input("First expense? ")
amount1 = float(input("Amount? $"))
subtotal += amount1
item2 = input("Second expense? ")
amount2 = float(input("Amount? $"))
subtotal += amount2
average = subtotal / 2
tax_percent = float(input("Tax rate %? ")) / 100
tax = subtotal * tax_percent
total = subtotal + tax
budget = float(input("Your budget? $"))
over_budget = bool(budget < total)
left = budget - total

print("-" * 40)
print("SUMMARY")
print(f" - {item1}:\t${amount1:.2f}")
print(f" - {item2}:\t${amount2:.2f}")
print(f"Subtotal:\t${subtotal:.2f}")
print(f"Average:\t${average:.2f}")
print(f"Tax ({int(tax_percent * 100)}%):\t${tax:.2f}")
print(f"Grandtotal:\t${total:.2f}")
print(f"Over budget?:\t{over_budget}")
print(f"Left in budget:\t${left}")
print("-" * 40)
print("Made by: Asher Leigh Z. Maguad | Installment 3")