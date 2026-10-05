# Expense Tracker - Installment 2
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

item1 = input("First expense? ")
amount1 = float(input("Amount? $"))
item2 = input("Second expense? ")
amount2 = float(input("Amount? $"))
total = amount1 + amount2
average = total / 2

print("-" * 40)
print("SUMMARY")
print(f" -{item1}:\t${amount1:.2f}")
print(f" -{item2}:\t${amount2:.2f}")
print(f"Total spent:\t${total:.2f}")
print(f"Average:\t${average:.2f}")
print("-" * 40)
print("Made by: Asher Leigh Z. Maguad | Installment 2")