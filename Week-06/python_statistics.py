# Christopher Springer
# 11/17/2026
# Practice Exercise 6.3 Python Statistics

import statistics

# Task 1: Display the dataset
days = [ 
    'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 
    'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday' 
]

sales = [1250, 1480, 1100, 1650, 1850, 
         1420, 1700, 1300, 2100, 1950] 

print('DAILY SALES REPORT')
print('-' * 15)
for i in range(len(days)):
    print(f'{days[i]}: ${sales[i]:,.2f}')

# Task 2: Calculate Descriptive Statistics
mean = statistics.mean(sales)
median = statistics.median(sales)
mode = statistics.mode(sales)
standard_deviation = statistics.stdev(sales)
total_sales = sum(sales)
lowest_sale = min(sales)
highest_sale = max(sales)

print(f'\nMean: ${mean:,.2f}')
print(f'Median: ${median:,.2f}')
print(f'Mode: ${mode:,.2f}')
print(f'Standard Deviation: ${standard_deviation:.2f}')
print(f'Total Sales: ${total_sales:,.2f}')
print(f'Lowest Sale: ${lowest_sale:,.2f}')
print(f'Highest Sale: ${highest_sale:,.2f}\n')

# Task 3: Evaluate Sales Performance
for i in range(len(days)):
    if sales[i] >= 1800:
        print(f'{days[i]}: ${sales[i]:,.2f} - Excellent')
    elif sales[i] >= 1500:
        print(f'{days[i]}: ${sales[i]:,.2f} - Good')
    elif sales[i] >= 1200:
        print(f'{days[i]}: ${sales[i]:,.2f} - Average')
    else:
        print(f'{days[i]}: ${sales[i]:,.2f} - Needs Improvement')

# Task 4: Count Sales Perfomance Categories
count_e = 0
count_g = 0
count_a = 0
count_ni = 0
for i in range(len(days)):
    if sales[i] >= 1800:
        count_e += 1
    elif sales[i] >= 1500:
        count_g += 1
    elif sales[i] >= 1200:
        count_a += 1
    else:
        count_ni += 1
print(f'\nNumber of Excellent sales days: {count_e}\n\
Number of Good sales days: {count_g}\n\
Number of Average sales days: {count_a}\n\
Number of Needs Improvement sales days: {count_ni}\n')

# Task 5: Identify Days That Meet the Sales Target
count_over_1500 = 0
for i in range(len(days)):
    if sales[i] >= 1500:
        print(f'{days[i]}: ${sales[i]:,.2f}')
        count_over_1500 += 1
print(f'There were {count_over_1500} days that exceeded the sales target\n')

# Task 6: Generate a Final Analysis
match mean:
    case mean if mean >= 1700:
        print('Sales performance is excellent.')
    case mean if mean >= 1500:
        print('Sales performance is good.')
    case mean if mean < 1500:
        print('Sales performance is excellent.')

'''
1. Why is the mean useful when analyzing daily sales? 
The mean is useful to see how well the business is running overall.
It shows what we can expect from on a daily basis.

2. What is the difference between the mean and median? 
They both show an average of how a typical sales day should go, but the 
mean can be skewed by outliers and cannot represent the average on its own.

3. Why might the standard deviation be useful to a business?
The standard deviation shows how spread the results are. If they are all
around the same number, it shows consistency. Whereas data that is 
completely spread out shows unreliability.

4. Which day generated the highest sales? 
Thursday, 2nd week generated the highest sales at $2,100

5. How many days achieved the company’s $1,500 sales target? 
There were 5 days that achieved the company's $1,500 sales target.

6. Which sales performance category had the most days? 
There were more Average sales days than any other performance category.

7. If the company wants to increase its average daily sales to $1,700, 
what changes might it consider? 
They should try to sell more on Mondays and Wednesdays, 
since the output is typically low on those days

'''

# Challenge 1: FInd Above Average Sales
print('These days were greater than the calculated average:')
for i in range(len(sales)):
    if sales[i] > mean:
        print(f'{days[i]}: ${sales[i]:,.2f}')

# Challenge 2: Calculate Percentage of Target Achievement
percentage = 0
count_days_exceeded = 0
for i in range(len(sales)):
    if sales[i] > mean:
        count_days_exceeded += 1
percentage = ((count_days_exceeded / len(days)) * 100)
print(f'The percentage of days that met or exceeded the target is {percentage}%')

# Challenge 3: Find the Highest Sales Day
highest_sale = max(sales)
position = sales.index(highest_sale)
print(f'{days[position]} has the highest sale with ${sales[position]:,.2f}')