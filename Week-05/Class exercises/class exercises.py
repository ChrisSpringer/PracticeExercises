# Christopher Springer
# 11/10/2026

student_one = 'Moses Jura'
student_two = 'Ardita Mrapshtija'

# print(f"My two classmates are {student_one}, and {student_two}.")

item1 = 25.75
item2 = 45.67
item3 = 45.75
item4 = 55.67
item5 = 45.60

total = item1 + item2 + item3 + item4 + item5
# print(f"Sub-Total =  {total}")

sales_tax = 0.07
tax_price = total * sales_tax
# print(f"      Tax =   {tax_price:.2f} ")

total += tax_price

# print(f"Total Cost = {total:.2f}")


meal_cost = float(input('Enter the cost of the meal: $'))
tip = meal_cost * 0.20
tax = meal_cost * 0.0825
total_cost = meal_cost + tip + tax

print("\n----- Meal Cost Breakdown -----")
print(f'Meal Cost:      ${meal_cost:7,.2f}')
print(f'Tip (20%):      ${tip:7,.2f}')
print(f'Tax (8.25%):    ${tax:7,.2f}')
print('-' * 30)
print(f'Total Cost:     ${total_cost:7,.2f}')