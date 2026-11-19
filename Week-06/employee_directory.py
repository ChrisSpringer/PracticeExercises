# Christopher Springer
# 11/18/2026
# Practice Exercise 6.8 Employee Directory System

# Create Employee class
class Employee:
    company = 'MetaData' # class attribute
    employee_count = 0
    # Constructor method
    def __init__(self, name, department, salary, start_year = 2026):
        self.name = name
        self.department = department
        self.salary = salary
        self.start_year = start_year
        Employee.employee_count += 1

    # Methods
    def display_info(self):
        print(f'Company    : {Employee.company}')
        print(f'Name:      : {self.name}')
        print(f'Department : {self.department}')
        print(f'Salary     : ${self.salary:,.2f}')
        print('-' * 30)

    def annual_bonus(self):
        bonus = self.salary * .1
        print(f'Annual Bonus for {self.name}: ${bonus:,.2f}')
        print('-' * 30)

    def promote(self, amount):
        self.salary += amount
        print(f'{self.name} Updated Salary: {self.salary:,.2f}')
        print('-' * 30)

    def years_of_service(self):
        years_worked = 2026 - self.start_year
        print(f'{self.name} has worked here for {years_worked} years')

# Collect information 
# Employee 1 inputs from user
print('=== Employee 1 ===')
name1 = input('Enter Employee Name: ')
department1 = input('Enter Department: ')
salary1 = float(input('Enter salary: $'))
year1 = int(input('Enter start year: '))

# Employee 2 inputs from user
print('=== Employee 2 ===')
name2 = input('Enter Employee Name: ')
department2 = input('Enter Department: ')
salary2 = float(input('Enter salary: $'))
year2 = int(input('Enter start year: '))

print()
# Creating the Employees
employee1 = Employee(name1, department1, salary1, year1)
employee2 = Employee(name2, department2, salary2, year2)

'''
# Calling the methods / challenge 4
employee1.display_info()
employee1.annual_bonus()
employee2.display_info()
employee2.annual_bonus()
'''

# Challenge 5
print(f'Number of Employees at {Employee.company}: {Employee.employee_count}')

# Challenge 6
employee1.promote(2500)

# Challenge 7
list = [employee1, employee2]
# Display results using a for loop
for i in range(len(list)):
    print(f'Employee {i+1} info:')
    list[i].display_info()
    list[i].annual_bonus()

employee1.years_of_service()
employee2.years_of_service()