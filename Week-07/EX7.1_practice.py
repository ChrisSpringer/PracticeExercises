# Christopher Springer
# 11/23/2026
# Practice Exercise 7.1 Processing NumPy Arrays Using For Loops

# Task 1: Import NumPy and Create the Sales Array
import numpy as np

sales_data = np.array([
    [[1200, 1500, 1800], 
     [1400, 1600, 1900]],

    [[2000, 2200, 2500], 
     [2100, 2300, 2600]]
])

# Task 2: Display the sales array
print(sales_data)
print(sales_data.ndim)
print(sales_data.shape)

# Task 3: Process the array using np.nditer()
for sale in np.nditer(sales_data):
    print(sale)

# Task 4: Process the Array Using Three Nested For Loops 
for layer in sales_data:
    for row in layer:
        for column in row:
            print(column)

# Task 5: Calculate Total Sales
total_sales = 0
for sale in np.nditer(sales_data):
    total_sales += sale
print(f'Total Sales:    ${total_sales:,.2f}')

# Task 6: Calculate Average Sales
count = 0 
for sale in np.nditer(sales_data):
    count += 1
average = total_sales / count
print(f'Average Sale:   ${average:,.2f}')

# Task 7: Identify the Highest Sales Amount 
highest_sale = 0
for sale in np.nditer(sales_data):
    if sale > highest_sale:
        highest_sale = sale
print(f'Highest Sale:   ${highest_sale:,.2f}')
