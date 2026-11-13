# Christopher Springer
# 11/12/2026

name = input("Enter your name: ")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

avg = (num1 + num2 + num3) / 3

print(f'Hello {name}! The average of {num1}, {num2} and {num3} \
is : {avg:.2f}')