# Christopher Springer
# 11/24/2026
# Practice Exercise W7M2

# Bean & Brew - Week 7, Module 2 
import pandas as pd 
import numpy as np 
print('pandas is ready!') 


# Task 1.1: Drink prices as a Series 
price_list = [4.75, 4.25, 5.25] 
prices = pd.Series(price_list) 
print(prices) 
prices = pd.Series(price_list, index=['Latte', 'Cold Brew', 'Mocha']) 
print(prices) 
menu_dict = {'Chai': 4.50, 'Espresso': 3.00} 
more_prices = pd.Series(menu_dict) 
print(more_prices) 
print(prices['Mocha']) 
print()


# Task 1.2: Build the stock DataFrame 
stock_data = { 
    'drink': ['Latte', 'Cold Brew', 'Mocha'], 
    'cups_left': [120, 54, 98] 
    } 
stock = pd.DataFrame(stock_data) 
print(stock) 
print(stock.to_string()) 
arr = np.array([[120, 54, 98]]) 
print(pd.DataFrame(arr)) 
# pandas gives the columns names of 0, 1, and 2 as a default
print()


# Task 1.3: Insert a column and build sample data 
stock.insert(1, 'size', ['M', 'L', 'M']) 
print(stock) 
sample = pd.DataFrame(np.arange(6).reshape((3, 2)), 
                      index=['Back Bay', 'Kendall', 'Seaport'], 
                      columns=['Mon', 'Tue']) 
print(sample) 
print()


# Task 1.4: Rows by label and by position 
cups = pd.DataFrame({'Mon': [120, 98, 143], 'Tue': [135, 110, 128]}, 
                    index=['Back Bay', 'Kendall', 'Seaport']) 
print(cups) 
print(cups['Kendall':]) 
print(cups.loc['Seaport']) 
print(cups.loc[['Back Bay', 'Seaport']]) 
print(cups.iloc[0]) 
# print(cups.loc[0])   # error since there is no label named 0, 0 is used here as an index

cups.loc['Fenway'] = [88, 91]   # add a new store row 
print(cups) 
print()


# Task 1.5: Read the orders file 
orders = pd.read_csv('bb_orders.csv') 
print(orders) 
print(pd.options.display.max_rows) 
print()

# Task 1.6: Explore the orders 
print(orders.head(3)) 
print(orders.tail(2)) 
print(orders.describe()) # Line 7: -2 and 12: 50
orders.info() # price has fewer than 16 non null Values
print(orders['store'].value_counts()) # 2 different spellings of Kendall(Kendall Square, Kendall Sq)
print()


# Task 1.7: Turn text into real dates 
print(orders['order_date'].dtype) 
# print(orders['order_date'].dt.month)   # dt works on DateTime objects not strings

orders['order_date'] = pd.to_datetime(orders['order_date']) 
print(orders['order_date'].dtype) 
march = orders[orders['order_date'] >= '2026-03-01'] 
print(len(march)) # 6 rows after March 1 2026
print()


# Task 2.1: Remove what we don't need 
orders = orders.drop('notes', axis=1) 
print(orders.shape) 
print(orders.duplicated().sum()) # 1 duplicate row
result = orders.drop_duplicates(inplace=True) 
print(result)   # inplace= True stores the new DataFrame in the original variable and returns nothing
print(orders.shape) 
print(len(orders.dropna())) # it would keep 14 rows, dropping the mocha order with no price
print()


# Task 2.2: Filter rows 
big = orders[orders['qty'] >= 4] 
print(big) # qty 50 in row 12 is suspicious
back_bay = orders[orders['store'] == 'Back Bay'] 
print(len(back_bay)) 
bb_big = orders[(orders['store'] == 'Back Bay') & (orders['qty'] >= 2)] 
print(bb_big[['order_id', 'qty']]) 
print()


# Task 2.3: Replace values and fill the gap 
print(orders['store'].value_counts()) 
orders.replace({'store': {'Kendall Sq': 'Kendall Square'}}, inplace=True) 
print(orders['store'].value_counts()) 
orders['price'] = orders.price.fillna(5.25) 
print(orders.loc[8]) 
print()


# Task 2.4: Fix or drop bad data 
orders.loc[12, 'qty'] = 5          # Dana confirmed: 5, not 50 
for x in orders.index: 
    if orders.loc[x, 'qty'] <= 0:  # can't guess, so drop it 
        orders.drop(x, inplace=True) 
print(orders[['order_id', 'qty']].tail(4)) 
print(orders.shape) # 14 orders(rows) left
print()


# Task 2.5: Retrieve and add columns 
print(orders['qty'].sum()) # 30 items sold
print(orders.qty.max()) # 5 max number of cups sold in any store
orders['revenue'] = orders['qty'] * orders['price'] 
print(orders[['drink', 'qty', 'price', 'revenue']].head()) 
print()


# Task 3.1: Basic aggregations 
rev = orders['revenue'] 
print(rev.sum())            # 138.0
print(rev.count())          # 14
print(round(rev.mean(), 2)) # 9.86
print(rev.median())         # 9.25
print(rev.min(), rev.max()) # 4.25, 21.25
print(orders.aggregate({'qty': ['sum', 'mean'], 
                        'revenue': ['sum', 'max']})) 
print()


# Task 3.2: Group by store and by drink 
store_rev = orders.groupby('store')['revenue'].sum()
print(store_rev) 
drink_qty = orders.groupby(['drink'])[['qty']].sum() 
print(drink_qty) 
print(orders.groupby('store')['qty'].mean().round(2)) 
print()


# Task 3.3: Sort the results 
print(store_rev.sort_values(ascending=False)) 
top = orders.sort_values('revenue', ascending=False) 
print(top[['order_id', 'store', 'revenue']].head(3)) 
print(drink_qty.sort_index(ascending=False)) 
print()


# Task 3.4: Rank stores and drinks 
print(store_rev.rank(ascending=False)) 
drink_qty['rank'] = drink_qty['qty'].rank(ascending=False) 
print(drink_qty) # 2 received a value of 2.5, an average of their ranks.
# rank assigns a place to each value with out moving the values, 
# sort does the same while moving them
print()

# Task 3.5: Merge in the cost of each drink 
menu = pd.DataFrame({ 
    'drink': ['Chai', 'Cold Brew', 'Espresso', 'Latte', 'Mocha'], 
    'cost': [1.40, 1.10, 0.90, 1.60, 1.90]}) 
drink_cost = pd.merge(menu, drink_qty[['qty']], on=['drink']) 
drink_cost['total_cost'] = drink_cost['qty'] * drink_cost['cost'] 
print(drink_cost) 
detail = pd.merge(orders, menu, on=['drink']) 
print(detail.shape) # 14 rows because it shows rows per order
print()


# Task 3.6: Sales by month 
orders['month'] = orders['order_date'].dt.month 
orders['weekday'] = orders['order_date'].dt.day_name() 
print(orders[['order_date', 'month', 'weekday']].head(3)) 
orders['order_month'] = orders['order_date'].dt.to_period('M') 
monthly_sales = orders.groupby('order_month')['revenue'].sum() 
print(monthly_sales) 
print()


# Task 4.1: Store-by-month report (challenge) 
report = pd.pivot_table(orders, values='revenue', index='store', 
                        columns='order_month', aggfunc='sum', 
                        fill_value=0) 
print(report) 
report.to_csv('bb_store_month.csv') 
print(pd.read_csv('bb_store_month.csv')) 


'''
1. In Task 1.4, why did cups.loc[0] fail when cups.iloc[0] worked? 
After Task 2.4 dropped row 7, which one would you use to get “the 8th row”, and why? 
cups.loc[0] failed because it looks for columns with that name. The columns already had names at that point 
cups.iloc[0] works because the first position is always 0
I would use loc[] to get the 8th row, since now the rows have changed positions, but not labels.
loc[] looks rows up by label not by position like iloc[]

2. In Task 2.1, result printed None. Explain what inplace=True does, 
and what would go wrong if you wrote orders = orders.drop_duplicates(inplace=True). 
inplace= True changes the object itself based on the function and returns nothing
Since it returns None, you would be reassigning orders to a Nonetype

3. In Task 2.4 we fixed one quantity and dropped another. 
When is it right to fix a bad value, and when is it better to drop the record? 
It is right to fix a value when you know what the mistake is and can be fixed.
If a correction is unknown or can't be safely guessed, 
it is better to drop the record to keep the records clean.

4. Rule 4 says clean before you count. Using the numbers from Tasks 1.5 and 3.2, 
describe how Seaport’s revenue would have been wrong if you had skipped Part 2. 
Seaport has a typo for one of their quantities. It was 5 and not 50.
Therefore, the revenue would have been extremely overestimated when multiplying it with the price.

5. Why is to_period('M') a better way to group by month than .dt.month when the data covers 
more than one year? 
.dt.month gives just a number, so it encompasses every year instead of just individual ones.
Also it would return too many rows depending on how the data was structured.
to_period('M') groups by month and year instead of by order,
making the data easier to read and analyze.

'''