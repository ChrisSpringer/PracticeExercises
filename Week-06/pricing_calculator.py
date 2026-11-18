# Christopher Springer
# 11/17/2026
# Practice Exercise 6.5 Product Pricing Calculator

product_name = input('Enter Product Name: ')
category = input('Enter Category: ')
original_price = float(input('Enter Original Price: $'))
discount = float(input('Enter discount percent: '))
tax_rate = float(input('Enter tax rate: '))
quantity = int(input('Enter quantity purchased: '))

apply_discount = lambda price, disc:price * (1- disc / 100)
apply_tax = lambda price, tax:price * (1 + tax / 100)
apply_both = lambda price,disc, tax: apply_tax(apply_discount(price, disc), tax)
final_price = lambda price, disc, tax: (price * (1 - disc) / 100)  * (1 + tax / 100)
bulk_discount = lambda price, qty: price * 0.90 if qty >= 10 else price

bulk_price = bulk_discount(original_price, quantity)
discounted_price = apply_discount(original_price, discount)
savings = original_price - discounted_price
tax_price = apply_tax(discounted_price, tax_rate)

total_price = apply_both(original_price, discount, tax_rate)




print('===== PriceIQ - Product Pricing Report =====')
print(f'Product   : {product_name}')
print(f'Category  : {category}')
print('-' * 30)
print(f'Original price      : ${original_price:<7.2f}')
print(f'Discount ({discount:.0f}%)      : -${savings:<7.2f}')
print(f'Price after disc    : ${discounted_price:<7.2f}')
print(f'Tax ({tax_rate:.0f}%)            : +${tax_price - discounted_price:<7.2f}')
print('-' * 30)
print(f'Final Price         : ${total_price:<7.2f}')
print('=' * 30)



prices = [210, 345, 90, 569.99, 120.50]
discounted = list(map(lambda price: float(f'{apply_discount(price,20):.2f}'), prices))
print(discounted)

filtered = list(filter(lambda price: apply_both(price,20,8) < 100, prices))
print(filtered)

lst = [('candy', 50), ('fruits', 320), ('tables', 245)]
sorted_list = sorted(lst, key = lambda item: item[1])
print(sorted_list)