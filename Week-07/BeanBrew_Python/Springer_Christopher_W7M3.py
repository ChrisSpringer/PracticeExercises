# Christopher Springer
# 11/25/2026
# Practice Exercise W7M3 Matplotlib

# Bean & Brew - Week 7, Module 3 
import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 
import os   # used in Task 2.9 
print('Matplotlib is ready!') 

# Task 1.1: Your first line graph 
xpoints = np.array([1, 7]) 
ypoints = np.array([2, 14]) 
plt.plot(xpoints, ypoints) 
plt.show() 
daily_cups = np.array([112, 98, 105, 120, 138, 162, 151]) 
plt.plot(daily_cups) 
plt.show()


# Task 1.2: Plot data from a DataFrame 
monthly = pd.DataFrame({ 
    'month': [1, 2, 3, 4, 5, 6], 
    'cups_sold': [3120, 2890, 3410, 3655, 3980, 4210]}) 
plt.title('Cups Sold, January to June') 
plt.xlabel('Month') 
plt.ylabel('Cups Sold') 
plt.plot(monthly['month'], monthly['cups_sold']) 
plt.show() 


# Task 1.3: Plot markers 
plt.plot(monthly['month'], monthly['cups_sold'], marker='o') 
plt.show() # Still has a line 'marker =' keeps the line
plt.plot(monthly['month'], monthly['cups_sold'], 'o') 
plt.show() # Just 'o' only shows the markers w/o line


# Task 1.4: Style the markers 
plt.plot(monthly['month'], monthly['cups_sold'], 
         marker='D', ms=10, mfc='gold', mec='saddlebrown') 
plt.show() 


# Task 1.5: The fmt shortcut 
plt.plot(monthly['month'], monthly['cups_sold'], 's--g') 
plt.show() 
# plt.plot(monthly['month'], monthly['cups_sold'], 'o:brown')   
# # error because 'brown' is not one of the value for the format

plt.plot(monthly['month'], monthly['cups_sold'], 'o:', color='brown') 
plt.show() 


# Task 1.6: Style the lines 
back_bay = np.array([1050, 960, 1120, 1190, 1280, 1330]) 
seaport = np.array([1010, 940, 1150, 1240, 1370, 1480]) 
plt.plot(monthly['month'], back_bay, lw=4, c='seagreen') 
plt.plot(monthly['month'], seaport, ls='--', marker='o', c='#D98E1F') 
plt.show() 


# Task 1.7: Set the figure size 
print(plt.rcParams['figure.figsize']) 
kendall = np.array([1060, 990, 1140, 1225, 1330, 1400]) 
plt.figure(figsize=(10, 4)) 
plt.plot(monthly['month'], back_bay, lw=4, c='seagreen') 
plt.plot(monthly['month'], seaport, ls='--', marker='o', c='#D98E1F') 
plt.plot(monthly['month'], kendall, c='steelblue') 
plt.show() 


# Task 2.1: Labels, fonts and a legend 
font1 = {'color': 'darkblue', 'size': 15} 
font2 = {'family': 'serif'} 
plt.title('Cups Sold by Store', fontdict=font1, loc='left') 
plt.xlabel('Month', fontdict=font2) 
plt.ylabel('Cups Sold', fontdict=font2) 
plt.plot(monthly['month'], back_bay, lw=4, c='seagreen', label='Back Bay') 
plt.plot(monthly['month'], seaport, ls='--', marker='o', c='#D98E1F', label='Seaport') 
plt.plot(monthly['month'], kendall, c='steelblue', label='Kendall Square') 
plt.legend() 
plt.show() 


# Task 2.2: Add a grid 
plt.title('Total Cups Sold per Month') 
plt.xlabel('Month') 
plt.ylabel('Cups Sold') 
plt.plot(monthly['month'], monthly['cups_sold'], marker='o') 
plt.grid(axis='y', color='gray', linestyle='--', linewidth=0.5) 
plt.show() 


# Task 2.3: Bar charts 
store_rev = pd.DataFrame({ 
    'store': ['Back Bay', 'Kendall Square', 'Seaport'], 
    'revenue': [38.75, 39.00, 60.25]}) 
plt.title('Online Revenue by Store, Q1 ($)') 
plt.bar(store_rev['store'], store_rev['revenue'], color='mediumpurple', width=0.6) 
plt.show() 
drinks = ['Chai', 'Cold Brew', 'Espresso', 'Latte', 'Mocha'] 
# cups = [4, 6, 2, 12] 
# plt.barh(drinks, cups)   
# cups only has 4 values, but there are 5 drinks, so it does not know what to set the last one to
# each values mmust correspond to a match in the list.

cups = [4, 6, 2, 12, 6] 
plt.title('Online Cups Sold by Drink, Q1') 
plt.barh(drinks, cups, color='seagreen', height=0.5) 
plt.show()


# Task 2.4: Scatter chart 
temps = np.array([48, 52, 55, 61, 64, 68, 72, 75, 79, 84]) 
cold_brew = np.array([22, 25, 31, 38, 41, 50, 57, 60, 68, 74]) 
latte = np.array([88, 84, 80, 74, 70, 66, 61, 55, 52, 47]) 
plt.scatter(temps, cold_brew, c='teal', label='Cold Brew') 
plt.scatter(temps, latte, c='chocolate', label='Latte') 
plt.title('Daily Cups Sold vs Temperature') 
plt.xlabel('Temperature (°F)') 
plt.ylabel('Cups Sold') 
plt.legend() 
plt.show() 
# The teal(Cold Brew) sells more(increases) as temp goes up and 
# the chocolate(Latte) sells more when temp is cooler(desreasing slope).


# Task 2.5: Colour the dots with a colour map 
busy = np.array([35, 40, 38, 52, 55, 61, 70, 78, 86, 95]) 
plt.scatter(temps, cold_brew, c=busy, cmap='viridis') 
plt.colorbar() 
plt.title('Cold Brew vs Temperature (colour = % seats taken)') 
plt.xlabel('Temperature (°F)') 
plt.ylabel('Cold Brew Cups') 
plt.show() 


# Task 2.6: Histogram of wait times 
np.random.seed(7) 
waits = np.random.normal(loc=4, scale=1, size=1000) 
print(np.round(np.mean(waits), 2)) 
plt.figure(figsize=(10, 6)) 
plt.hist(waits, bins=15, color='skyblue', edgecolor='black') 
plt.title('Wait Times for 1,000 Simulated Orders') 
plt.xlabel('Wait (minutes)') 
plt.ylabel('Number of Orders') 
plt.grid(axis='y', alpha=0.75) 
plt.show() 


# Task 2.7: Pie chart of drink sales 
explode = [0, 0, 0, 0.1, 0] 
plt.figure(figsize=(8, 5)) 
plt.pie(cups, startangle=90, explode=explode, autopct='%1.0f%%') 
plt.title('Share of Online Cups by Drink, Q1') 
plt.legend(drinks, title='Drink', loc='center left', bbox_to_anchor=(1, 0.5)) 
plt.show() 


# Task 2.8: Subplots 
fig, axes = plt.subplots(1, 2, figsize=(12, 5)) 
axes[0].bar(store_rev['store'], store_rev['revenue'], color='mediumpurple') 
axes[0].set_title('Online Revenue by Store ($)') 
axes[1].pie(cups, labels=drinks, startangle=90) 
axes[1].set_title('Share of Cups by Drink') 
#axes[2].plot(monthly['month'], monthly['cups_sold'])   #error because there are only 2 axes: (0,1).
plt.show()


# Task 2.9: Save a figure 
plt.title('Online Revenue by Store, Q1') 
plt.xlabel('Store') 
plt.ylabel('Revenue ($)') 
plt.bar(store_rev['store'], store_rev['revenue'], color='mediumpurple', width=0.6) 
plt.savefig('bb_store_revenue.png', dpi=150) 
print(os.path.exists('bb_store_revenue.png')) 
plt.show() 


# Task 3.1: Q1 online orders dashboard (challenge) 
orders = pd.read_csv('bb_orders.csv') 
orders = orders.drop('notes', axis=1).drop_duplicates() 
orders = orders.replace({'store': {'Kendall Sq': 'Kendall Square'}}) 
orders['price'] = orders['price'].fillna(5.25) 
orders.loc[12, 'qty'] = 5 
orders = orders[orders['qty'] > 0] 
orders['revenue'] = orders['qty'] * orders['price'] 
orders['month'] = pd.to_datetime(orders['order_date']).dt.to_period('M') 
print(orders.shape, orders['revenue'].sum()) 
 
by_month = orders.groupby('month')['revenue'].sum() 
by_store = orders.groupby('store')['revenue'].sum() 
by_drink = orders.groupby('drink')['qty'].sum() 
fig, axes = plt.subplots(2, 2, figsize=(12, 8)) 
axes[0, 0].plot(by_month.index.astype(str), by_month.values, marker='o', c='seagreen') 
axes[0, 0].set_title('Revenue by Month ($)') 
axes[0, 1].bar(by_store.index, by_store.values, color='mediumpurple') 
axes[0, 1].set_title('Revenue by Store ($)') 
axes[1, 0].pie(by_drink.values, labels=by_drink.index, startangle=90) 
axes[1, 0].set_title('Cups by Drink') 
axes[1, 1].hist(orders['revenue'], bins=5, color='skyblue', edgecolor='black') 
axes[1, 1].set_title('Order Size ($)') 
plt.tight_layout() 
plt.savefig('bb_q1_dashboard.png', dpi=150) 
plt.show() 


'''
1. In Task 1.1 you plotted daily_cups without x values. Why did the x-axis start at 0, and what 
would you change so the days are numbered 1 to 7? 
Matplotlib automatically generated the x values starting at 0 when its only provided y values.
To start at 1 and end at 7, you must provide that range in the dataset

2. In Task 1.5, why did 'o:brown' fail while 'o:' with color='brown' worked? When is the fmt 
shortcut handy, and when are keyword arguments clearer? 
'o:brown' fails because brown is not a color name in the fmt shortcut. It reads the 'o' then ':'
then 'b' but then continues to read 'r' and assumes red but causes a ValueError since a color was already defined
fmt packs color, marker, and line in one short string, so its useful if you know the shortcut names.
If you want to use a full color name, or a color thats not included in the shortcut list
use the keyword arguments instead.

3. Look at the charts from Tasks 2.3, 2.4 and 2.7. For each one, say which of Dana’s questions it 
answers and why that chart type suits it. Why would a pie chart of the monthly cups from Task 1.2 
be a poor choice? 
The bar chart in 2.3 answers the comparison of the stores online revenue. 
It shows total revenue for each store.
The sideways bar chart in 2.4 answers 'which drinks make up our sales' showing how many total of 
each drink sold among all stores.
The pie chart answers 'what share of online cups does each drink make up? Pull out the Latte 
slice, it’s our star.' This is a suitable chart, since it shows how much each drink contributes to the total share
while also highlighting the specific section Dana is interested in by pulling it out of the graph.
A pie chart in Task 1.2 would be a poor choice since it displays cups sold monthly instead of cups sold per drink.
Dana wanted the share of each cups not how many cups were sold from January to June.

4. In Task 2.6, change bins=15 to bins=5 and then to bins=60, and run each. How does the story 
the histogram tells change? Put it back to 15 afterwards. 
The more bins there are, the finer detail there is. When there is only 5, the grouping is more general
and harder to analyze specific details. 60 has a lot more information and spread.

5. Rule 4 says save before you show. What would bb_store_revenue.png contain if plt.savefig() 
came after plt.show() in Task 2.9, and why? 
Matplotlib removes the figure after it displays it, so savefig() would save an empty or blank image.
Saving it before showing it ensures that the figure is stored somewhere before it is removed

'''