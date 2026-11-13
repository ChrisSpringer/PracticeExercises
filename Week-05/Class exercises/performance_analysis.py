# Christopher Springer
# 11/12/2026

name = input("Enter employee name: ")
score = int(input("Enter performance score: "))

if score >= 80:
    result ="Excellent Performance"
else:
    result = "Needs Improvement"

print(f"Employee Name: {name}")
print(f"Performance Score: {score}")
print(f"Performance Category: {result}")