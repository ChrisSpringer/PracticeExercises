# Christopher Springer
# 11/12/2026

name = input("Enter your name: ")
score = eval(input("Enter your score: "))

if score >= 90:
    rating = "Outstanding"
elif score >= 80:
    rating = "Exceeds Expectations"
elif score >= 70:
    rating = "Meets Expectations"
elif score >= 60:
    rating = "Below Expectations"
else:
    rating = "Unsatisfactory"    

print()
print(f"Employee Name: {name}")
print(f"Performance Score: {score}")
print(f"Performance Category: {rating}")