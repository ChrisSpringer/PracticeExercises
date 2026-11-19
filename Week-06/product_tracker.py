# Christopher Springer
# 11/18/2026
# Practice Exercise 6.7 Product inventory tracker

class Product:

    # Class attribute
    store_name = 'StockSmart'

    # Constructor method
    def __init__(self, name, category, price, quantity, reorder_level = 0):
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity
        self.reorder_level = reorder_level

    # Methods
    def display_info(self):
        print(f'Store Name: {Product.store_name}')
        print(f'Name : {self.name}')
        print(f'Category: {self.category}')
        print(f'Price: ${self.price:,.2f}')
        print(f'Quantity: {self.quantity} units\n')

    def inventory_value(self):
        value = self.quantity * self.price
        print(f'Value: ${value:,.2f}\n')

    def apply_discount(self, pct):
        discounted_price = self.price - self.price * pct
        print(f'Discounted Price: ${discounted_price:,.2f}')

    def needs_reorder(self):
        if self.quantity <= self.reorder_level:
            return True
        
# Product 1 inputs from user
print('Product 1')
name1 = input('Enter Product Name: ')
category1 = input('Enter Category: ')
price1 = float(input('Enter price: $'))
quantity1 = int(input('Enter quantity: '))

# Product 2 inputs from user
print('Product 2')
name2 = input('Enter Product Name: ')
category2 = input('Enter Category: ')
price2 = float(input('Enter price: $'))
quantity2 = int(input('Enter quantity: '))

# Creating list from the products
product1 = Product(name1, category1, price1, quantity1)
product2 = Product(name2, category2, price2, quantity2)
list = [product1, product2]

# Display results using a for loop
for i in range(len(list)):
    print(f'Product {i} info:')
    list[i+1].display_info()
    list[i+1].inventory_value()

# Initial print statements before challenges
'''
print('Product 1 info')
product1.display_info()
product1.inventory_value()

print('Product 2 info')
product2.display_info()
product2.inventory_value()
'''