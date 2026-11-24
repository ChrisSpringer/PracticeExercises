# Christopher Springer
# 11/23/2026
# Practice Exercise W7M1 Bean & Brew: Crunching Sales Data with NumPy 

# Bean & Brew - Week 7, Module 1 
import numpy as np 
print('NumPy is ready!\n') 


#  Task 1.1: Loop through a 2D array 
# rows: Back Bay, Kendall Square | columns: Mon, Tue, Wed 
cups = np.array([[120, 135, 150], 
                 [98, 110, 104]]) 
for row in cups: 
    print(row) # 2 lines printed
for row in cups: 
    for value in row: 
        print(value) # 6 lines printed
print()

# Task 1.2: Join and stack the store data 
seaport = np.array([[143, 128, 161]]) 
all_stores = np.concatenate((cups, seaport))   # axis=0: add a row 
print(all_stores) 
thu_fri = np.array([[140, 172], [101, 95], [150, 166]]) 
week = np.concatenate((all_stores, thu_fri), axis=1)   # add columns 
print(week) 
mon = np.array([120, 98, 143]) 
tue = np.array([135, 110, 128]) 
print(np.hstack((mon, tue))) 
print(np.vstack((mon, tue))) 
print(np.stack((mon, tue), axis=1)) 
print()

# Task 1.3: Predict, then run: missing data(Nan vs None) 
seaport_week = np.array([143, 128, 161, np.nan, 166]) 
print(seaport_week) 
print(seaport_week.dtype) 
print(np.sum(seaport_week)) 
seaport_none = np.array([143, 128, 161, None, 166]) 
print(seaport_none.dtype) 
# print(seaport_none + 1) # None turns the array into an object(NoneType), this addition will cause a type error
print(seaport_week + 1)
print()

# Task 1.4: Split the week into parts 
days = np.array([140, 152, 138, 160, 171, 199, 185])   # Mon to Sun 
halves = np.array_split(days, 2) 
print(halves) 
print(halves[1]) 
by_store = np.array_split(week, 3) 
print(by_store[2])   # Seaport 
print()

# Task 1.5: Find the slow days with where() 
TARGET = 150 
print(np.where(days < TARGET)) 
print(np.where(days < TARGET, 'below', 'met')) 
print(np.where(days < TARGET, days + 15, days))   # promo boost 
print()

# Task 1.6: Sort and filter the sales 
print(np.sort(days)) 
print(days) 
codes = np.array(['95', '100', '9', '120']) 
print(np.sort(codes))   #['100', '120', '9', '95'] 
print(np.sort(week)) 
busy = days > 160 
print(busy) 
print(days[busy]) 
print()


# Task 2.1: Make repeatable random numbers 
np.random.seed(7) 
test_orders = np.random.randint(1, 6, size=(2, 5)) 
print(test_orders) 
tips = np.random.rand(2, 3) 
print(tips) 
print()


# Task 2.2: Predict, then run 
np.random.seed(7) 
sizes = ['small', 'medium', 'large'] 
#orders = np.random.choice(sizes, p=[0.3, 0.5, 0.3], size=10) # probabilities do not add up to 1.
orders = np.random.choice(sizes, p=[0.2, 0.5, 0.3], size=10) 
print(orders) 
print(orders[orders == 'large']) 
print(np.random.choice(sizes)) 
print()


# Task 2.3: Simulate wait times with normal() 
np.random.seed(7) 
waits = np.random.normal(loc=4, scale=1, size=1000) 
print(np.round(np.mean(waits), 2)) 
print(np.round(np.std(waits), 2)) 
within_1 = waits[np.absolute(waits - 4) < 1] 
print(len(within_1)) # 69.2%
within_2 = waits[np.absolute(waits - 4) < 2] 
print(len(within_2)) # 96.8%
print()


# Task 3.1: Shuffle the barista rota 
np.random.seed(7) 
baristas = np.array(['Ana', 'Ben', 'Cho', 'Dev', 'Eli']) 
print(np.random.permutation(baristas)) 
print(baristas) 
np.random.shuffle(baristas) 
print(baristas)
print()


# Task 3.2: Revenue and cost with arithmetic ufuncs 
mon_cups = np.array([120, 98, 143]) 
avg_price = np.array([4.50, 4.25, 4.75]) 
revenue = np.multiply(mon_cups, avg_price) 
print(revenue) 
cost = np.array([310, 260, 380]) 
print(np.subtract(revenue, cost))   # profit 
print(np.divmod(mon_cups, 25))      # (sleeves, leftover cups) 
print(np.absolute(np.array([-12, 5, -3]))) 
print()

# Task 3.3: Predict, then run: five ways to round
changes = np.array([-2.7, -0.5, 0.5, 1.5, 2.5, 3.46]) 
print(np.trunc(changes)) 
print(np.fix(changes)) 
print(np.floor(changes)) 
print(np.ceil(changes)) 
print(np.round(changes))      # 0, 1, 2 / 0, 2, 2 round goes to nearest EVEN number
print(np.round(changes, 1)) 
print()


# Task 3.4: Totals per store, per day and running totals 
print(week) 
print(np.sum(week))           # = 1973
print(np.sum(week, axis=1))   # per store = 3 
print(np.sum(week, axis=0))   # per day = 5
print(np.cumsum(days))        # = 1145
print()

# Task 3.5: Growth and day-to-day change 
growth = np.array([1.10, 1.05, 1.20]) 
print(np.round(np.prod(growth), 3)) 
print(np.round(np.cumprod(growth), 3)) 
print(np.diff(days)) 
print(np.diff(days, n=2)) 
print()

# Task 4.1: Compare store menus with set operations 
back_bay = np.array(['latte', 'mocha', 'latte', 'cold brew', 'chai']) 
kendall = np.array(['latte', 'matcha', 'chai', 'chai']) 
print(np.unique(back_bay)) 
print(np.union1d(back_bay, kendall)) 
print(np.intersect1d(back_bay, kendall)) 
print(np.setdiff1d(back_bay, kendall)) 


'''
1. In Task 3.4, np.sum(week, axis=0) returned 5 values and axis=1 returned 3. 
Explain why, using the words rows and columns. 
Using the axis parameter find the sum of elements along a specific axis. 
0 returns the columns, while 1 returns the rows.

2. Why is np.nan a better way to record Seaport’s missing Thursday than None or 0? 
What would go wrong in a weekly total with each one? 
NaN shows that there is a missing value, whereas None and 0 set the value to None and zero respectively.
NaN is stored as a float so mathematical operations can still be performed on arrays with no errors raised.
None chages the array to an object and mathematical operators cannot be run on NoneTypes.
0 can raise silentt errors in mathematical computations where NaN could catch them.

3. In Task 1.6, '9' sorted after '120'. Why? How would you get a proper numeric order? 
String are ordered by characters, and 1 comes before 9. 
Since the 1 in 120 and 9 share the same position(index), 120 is printed first. 
The numbers must be casted as ints before comparison to get a proper numeric order

4. Why is setting a seed useful when you build test data? 
Give one situation where NumPy’s pseudo random numbers would not be good enough (1.B.1). 
Setting a seed is useful for repeating results and testing code.
You would not want to use a seed where unpredictability matters, like passwords

5. Dana wants to know how many full sleeves of 25 cups to order for 143 cups. 
Which rounding or division tool from Part 3 would you use, and why not round()? 
I would use .ceil function since it gives a whole number that covers any remainders needed.
Round does not work here because it rounds to the nearest even number, 
which can cause silent or unnoticed errors.

'''