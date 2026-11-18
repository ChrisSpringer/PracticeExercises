# Name: Christopher Springer
# Date: 11/16/2026
# Description: Practice Exercise Income Tax Calculator
  
# TODO 2: Define the constants 
# TAX_RATE = 20%
# STANDARD_DEDUCTION = $10,000 
# DEPENDENT_DEDUCTION = $2,000 per dependent

TAX_RATE = 0.20
STANDARD_DEDUCTION = 10000
DEPENDENT_DEDUCTION = 2000
  
# TODO 3: Display the program title and a divider line 
print("INCOME TAX CALCULATOR")
print('-' * 40)

  
# TODO 4: Prompt for gross annual income and convert it to a float 
gross_annual_income = float(input('Enter gross annual income: '))

# TODO 5: Prompt for the number of dependents and convert it to an int 
num_dependents = int(input('Enter number of dependents: '))  

# TODO 6: Calculate the dependent deductions and the total deductions 
dependent_deductions = DEPENDENT_DEDUCTION * num_dependents
total_deductions = STANDARD_DEDUCTION + dependent_deductions

# TODO 7: Calculate the taxable income 
taxable_income = gross_annual_income - total_deductions

# TODO 8: Calculate the estimated income tax 
estimated_income_tax = taxable_income * TAX_RATE

# TODO 9: Display the income tax summary 
# Show: gross income, standard deduction, dependent deductions, 
# total deductions, taxable income, tax rate, and estimated income tax. 
# Use f-strings and format monetary values with .2f
print('\nIncome Tax Summary')
print('-' * 40)
print(f'Gross Income:{'':>15} ${gross_annual_income:,.2f}')
print(f'Standard Deduction:{'':>9} ${STANDARD_DEDUCTION:,.2f}')
print(f'Dependent Deductions:{'':>8} ${dependent_deductions:,.2f}')
print(f'Total Deductions:{'':>11} ${total_deductions:,.2f}')
print(f'Taxable Income:{'':>12} ${taxable_income:,.2f}')
print(f'Tax Rate:{'':>24} {TAX_RATE * 100}%')
print(f'Estimated Income Tax:{'':>7} ${estimated_income_tax:,.2f}')

'''
1. Why must gross income be converted to a float data type? 
When dealing with money, it is better to deal with a float data type for precision

2. Why is the number of dependents converted to an int data type? 
There can not be half of a person, so it must be a whole number

3. What is the purpose of the .2f format specifier in an f-string? 
It formats the float to 2 decimal places, to ensure the currency is reflected correctly

4. Which arithmetic operators did you use in this program, and where? 
I used (+) to add the deductions together for total deductions
I used (-) to subtract the deductibles from the gross income for the taxable income
I used (*) to populate the dividers and to calculate the tax rate.

5. How would you modify the program to prevent taxable income from becoming negative?
I would use an if statement to catch if the income ended up being negative.
(If gross annual income < total deductions then do nothing or print a message accordingly) 
'''