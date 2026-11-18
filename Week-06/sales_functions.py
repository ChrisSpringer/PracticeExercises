# Christopher Springer
# 11/17/2026
# Practice Exercise 6.4

# Part 1: Creating lists
employees = ['John', 'Sarah', 'Michael', 'Jennifer', 'David'] 
sales = [5200, 6800, 4500, 7200, 5800] 

# Task 1: Calculate total sales
def calculate_total(sale_list):
    total = 0
    for i in range(len(sale_list)):
        total += sale_list[i]
    return total
total_sales = calculate_total(sales)
print(f'Total Monthly Sales: ${total_sales:,.2f}\n')

# Task 2: Calculate average sales
def calculate_average(total, number_of_employees):
    avg = total / number_of_employees
    return avg
average = calculate_average(calculate_total(sales), len(employees))
print(f'Average Sales per Employee: ${average:,.2f}\n')

# Task 3: Determine sales performance
def evaluate_performance(sale):
    if sale >= 7000:
        performance = 'Excellent'
    elif sale >= 6000:
        performance = 'Good'
    elif sale >= 5000:
        performance = 'Average'
    else:
        performance = 'Needs Improvement'
    return performance
print('EMPLOYEE SALES PERFORMANCE')
print('-' * 20)
for s in range(len(sales)):
    performance = evaluate_performance(sales[s])
    print(f'{employees[s]}: ${sales[s]:,.2f} - {performance}')

# Task 4: Find the highest sales amount
def find_highest_sales(sales_list):
    highest_sales_amount = 0
    for sale in range(len(sales_list)):
        if sales[sale] > highest_sales_amount:
            highest_sales_amount = sales_list[sale]
    return highest_sales_amount
highest_amount = find_highest_sales(sales)
print(f'\nHighest Sales Amount: ${highest_amount:,.2f}\n')

# Task 5: Calculate employee commission && Challenge 1: Sales Bonus
def calculate_commission(amount):
    rate = 0.05
    if amount >= 7000:
        rate = 0.10
    return amount * rate
commission = calculate_commission(5200)
print(f"John's Commission: ${commission:,.2f}\n")

# Task 6: Generate an employee sales report
print('EMPLOYEE SALES SUMMARY')
print('-' * 60)
print('Employee     Sales       Performance             Commission')
print('-' * 60)
for i in range(len(employees)):
    performance = evaluate_performance(sales[i])
    commission = calculate_commission(sales[i])
    print(f'{employees[i]:<12}${sales[i]:<7,.2f}     \
{performance:<20}    ${commission:<10,.2f}')

'''
1. What is a user-defined function in Python? 
A block of code that the user creates that is reuseable 
and saves time coding the same thing.

2. What is the difference between a parameter and an argument? 
A parameter is given in the definition of a function
while arguments are inputs passed when calling said function.

3. What is the purpose of the return statement? 
return statements give a desired value when a function is called.

4. What is the difference between print() and return? 
print() displays the output to the user whereas return
sends a value through the function that may not be displayed.

5. Why is it beneficial to divide a large program into smaller functions? 
It is beneficial for readability and to minimize errors.

6. In the code below, identify the function name, the parameters, and the arguments. 
def calculate_commission(amount, rate): 
return amount * rate 
commission = calculate_commission(5200, 0.05)
function name = calculate_commision
parameters = amount, rate
arguments = 5200, 0.05

'''
# Challenge 2: Count employees above average
def above_average(sale_list,average_sales):
    num_above_average = 0
    for i in range(len(sale_list)):
        if sale_list[i] > average_sales:
            num_above_average += 1
    return num_above_average
print(f'\nEmployees Above Average: \
{above_average(sales,average)}\n')

# Challenge 3: Calculate annual sales
def calculate_annual_sales(montly_sale):
    m_sale = montly_sale * 12
    return m_sale

for i in range(len(sales)):
    annual_sale = calculate_annual_sales(sales[i])
    print(f'{employees[i]}: ${annual_sale:,.2f}')