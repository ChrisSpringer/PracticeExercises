# Bean & Brew - Week 5, Module 1
print('Python is ready!')

# Task 1.1: Say hello
print('Welcome to Bean & Brew Coffee Co.!')
print("Today's special: Caramel Latte")
print('Stores:', 3)

# Task 1.2: Store the store's facts in variables
store_name = 'Back Bay'
open_hour = 7
latte_price = 4.95
is_open = True
manager = None
MAX_SEATS = 40

print(store_name, open_hour, latte_price, is_open, manager, MAX_SEATS)

# Task 1.3: Comment your code
# Author: Christopher Springer
print('Comments are ignored by Python') # this note is not printed

# Task 1.4: Check the data types
print(type(store_name))    # str
print(type(open_hour))     # int
print(type(latte_price))   # float
print(type(is_open))       # Boolean
print(type(manager))       # NoneType
print(type('7'))           # str

# Task 1.5: Predict, then run - Error because we are trying to concatenate two different data types
cups_sold = 120
# print('Cups sold today: ' + cups_sold) # broken: commented out 
# TypeError: can only concatenate str (not "int") to str 

print('Cups sold today: ' + str(cups_sold)) # Cups sold today: 120
print(cups_sold + cups_sold) # 240
print('120' + '120') # 120120

# Task 2.1: Predict, then run
# print(store_nme) # Error will occur due to wrong naming
#NameError: name 'store_nme' is not defined. Did you mean: 'store_name'? 
print(store_name)

# Task 2.2 (a): Predict, then run - Python is looking for a closed bracket so an error will occur
# SyntaxError: '(' was never closed 
print('Back Bay opens at', open_hour)

# Task 2.2 (b): Predict, then run - the indentation will cause an error
print('Line one')
print('Line two')

# Task 2.3: Predict, then run - data type casting error
# qty = int('twelve') ValueError: invalid literal for int() with base 10: 'twelve'
qty = int('12')
print(qty + 1)

# Task 3.1 (a)
# class = 'VIP' SyntaxError: invalid syntax variable named with keyword
# 2nd_store = 'Kendall Square' SyntaxError: invalid decimal literal variable started with number
customer_class = 'VIP'
store_2 = 'Kendall Square'
print(customer_class, store_2)

# Reflection Questions
# 1. In Task 2.2 nothing printed at all, but in Task 1.5 everything above the error printed. Explain the difference. 
# The syntax and indentation errors in 2.2 are found before the script runs, so nothing is printed.
# The errors in 1.5 are found once python reaches that part of the script, so everything above gets printed

# 2. Why is reading the last line of a traceback first a good habit? What does the rest of the traceback tell you? 
# The last line of a traceback tells you the error that was encountered to let you know what went wrong.
# The rest of the traceback tells you the code that caused it and where the error was found (file and line number)

# 3. '7' and 7 look almost the same. Give one example of something you can do with one but not the other. 
# You can concatenate '7' with other strings making a longer string. An int cannot be concatenated with other strings ('I want' + '7')
# The int 7 can have mathematical operations performed on it whereas '7' cannot. (7 + 12)

# 4. Name the five error types from Student Guide 1.A.9 and give a one-line cause for each. 
# TypeError - Trying to add or concatenate a string and a number without casting
# NameError - Using a variable brfore it's defined, or a typo in a variable name
# SyntaxError - Missing colon, unclosed bracket, or typo in a keyword
# IndentationError - Extra or missing spaces at the start of a line
# ValueError - int('twelve') - text can't be converted to an integer