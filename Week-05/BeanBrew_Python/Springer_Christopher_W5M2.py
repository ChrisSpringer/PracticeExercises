# Christopher Springer
# 11/10/2026
# Practice Exercise 2

# Bean & Brew - Week 5, Module 2: Register math
print('Register script ready')

# Task 1.1: Ring up an order
# 1. Define
latte_price = 4.95
muffin_price = 3.50
lattes = 2
muffins = 1

# 2. Calculate
subtotal = latte_price * lattes + muffin_price * muffins

# 3. Display
print(subtotal) # 13.4

# Task 1.2: Turn minutes into hours
shift_minutes = 536
print(shift_minutes / 60)   # 8.9333333333333334 actual division
print(shift_minutes // 60)  # 8     amount of hours
print(shift_minutes % 60)   # 56    remaining minutes
print(2 ** 3)               # 8

# Task 1.3: Predict, then run
price = 5.00
discount = 1.00
cups = 3
total_a = price - discount * cups   # returns 2.0
total_b = (price - discount) * cups # returns 12.0 correct answer
print(total_a, total_b)


# Task 2.1: Order supplies
import math

cups_needed = 530
sleeve_size = 50
print(cups_needed / sleeve_size)             # 10.6
print(math.ceil(cups_needed / sleeve_size))  # 11
print(math.floor(cups_needed / sleeve_size)) # 10
print(math.trunc(-2.7), math.floor(-2.7)) # -2 -3 trunc takes off decimals
# ceil function returns correct number since you need to account for the decimal
# you cannot have 0.6 of a cup, so an extra cup would take care of the remainder

# Task 2.2: Add tax and round
TAX_RATE = 0.0625
tax = subtotal * TAX_RATE
print(tax)                      # 0.8375
print(round(tax, 2))            # 0.84
print(round(3.0, 2))            # 3.0
print(format(3.0, '.2f'))       # 3.00
print(type(format(tax, '.2f'))) # <class 'str'>

# Task 2.3: Keep a running total
till = 200
till += 13.40
till += 4.50
till -= 20
print(till)             # 197.9

cups_left = 530
cups_left -= 96
print(cups_left)        # 434
cups_left //= 50
print(cups_left)        # 8

# Task 3.1: Predict, then run
# I thought it was a tyoe error because of the data types, 
# but forgot the operator just repeats the value multiple times
print(5 * '5')      # 55555
print(5 * 5)        # 25
print(int('5') * 5) # 25
print(int(4.99))    # 4

# Task 3.2: Print a receipt
customer = 'Maria'
print(f'Thank you, {customer}!')            # Thank you, Maria!
print(f'Subtotal:   ${subtotal:.2f}')       # $13.40
print(f'Tax:        ${tax:.2f}')            # $0.84
print(f'Total:      ${subtotal + tax:.2f}') # $14.24

# Task 4.1: Bag the beans
BAG_GRAMS = 340
BAG_PRICE = 14.99
beans_g = 25 * 1000
bags = beans_g // BAG_GRAMS
leftover_g = beans_g % BAG_GRAMS
value = bags * BAG_PRICE
print(f'{bags} bags, {leftover_g} g left over, worth ${value:.2f}')
# 73 bags, 180 g left over, worth $1094.27


#   1. In Task 1.3, explain in your own words why total_a was wrong. 
#   How would you rewrite it so nobody could misread it? 
#   total_a was wrong because it did not account for the precedence of operators
#   operators work like PEMDAS from left to right, so the wrong expression was completed first.

#   2. When would you use math.ceil() instead of round()? Give a Bean & Brew example of each. 
#   math.ceil() always rounds up, whereas round() rounds to the nearest decimal.
#   math.ceil() can be used when finding out how many cup orders 
#   you would need to accomodate a certain amount of people
#   math.round() can be used when calculating monetary values

#   3. Why is it a good idea to round with :.2f when you print, 
#   rather than rounding the variable itself? 
#   Round does not return trailing zeroes. So a result of round(3.0, 4) still returns 3
#   While the :.2f does the same rounding but it adds on the etra decimals if necessary

#   4. 5 * '5' didn't cause an error. 
#   Why is a silent wrong answer more dangerous than an error message? 
#   A silent wrong answer is more dangerous because it still runs
#   If you are not careful, the mistake could go unnoticed.
#   Especially if the result is not displayed and is instead used in an expression,
#   it can ruin calculations behind the scenes and the programmer would not know where the
#   problem stemmed from.