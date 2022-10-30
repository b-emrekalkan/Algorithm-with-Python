
#! PROBLEM: Create an algorithm that finds BMI.

#? SOLUTION:

weight = int(input("Please enter your weight in kg:"))
height = int(input("Please enter your height in cm"))

result = round(weight / ((height / 100) ** 2),2)

if result < 18.5:
    body = "underweight"
elif result < 25:
    body = "normal"
elif result < 30:
    body = "overweight"
elif result < 35:
    body = "obese"
else:
    body = "extremely obese"
print(f"Your BMI is: {result} and your body type is: {body}")