
#! PROBLEM: Create an algorithm that asks the employee for weekly working hours and hourly wage information and ultimately calculates the employee's weekly salary.
# Note >> Work over 40 hours per week is paid 1.5 times the wage

#? SOLUTION:

#* The int() function 👉 converts the specified value into an integer number. 👇

work_hours = int(input("Please enter your weekly working hour:"))

hourly_wage = int(input("Please enter your hourly wage:"))

if work_hours > 40:
    weekly_wage = (work_hours - 40) * (1.5 * hourly_wage) + 40 * hourly_wage
else:
    weekly_wage = work_hours * hourly_wage
print(f"Your weekly wage is {weekly_wage}")