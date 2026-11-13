# Christopher Springer
# 11/13/2026

# Create known variables
day = 1

monday = 1200
tuesday = 1500
wednesday = 1100
thursday = 1800
friday = 1400

total_sales = 0

# Create the while loop that runs 5 times, 
# checking each day to add respective sales
'''
while day <= 5:
    if day == 1:
        total_sales += monday
    elif day == 2:
        total_sales += tuesday
    elif day == 3:
        total_sales += wednesday
    elif day == 4:
        total_sales += thursday
    else:
        total_sales += friday
    day += 1
'''

for i in range(1,6):
    if day == 1:
        total_sales += monday
    elif day == 2:
        total_sales += tuesday
    elif day == 3:
        total_sales += wednesday
    elif day == 4:
        total_sales += thursday
    else:
        total_sales += friday
    day += 1

# Calculate average sales
avg_sales = total_sales / 5

# Display results
print(f"Total Sales: ${total_sales:,.2f}")
print(f'Average Daily Sales: ${avg_sales:,.2f}')