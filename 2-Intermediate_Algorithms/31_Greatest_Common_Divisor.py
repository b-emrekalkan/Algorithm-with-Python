
#! Write a Python program to compute the Greatest Common Divisor of two positive intergers:

# 12 >> (1,2,3,4,6,12)
# 16 >> (1,2,4,8,16)
#! The Greatest Common Divisor for 12 and 16 is => 4


#? SOLUTION:

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

i = 1

while (i <= num1 and i <= num2):
    if (num1 % i == 0 and num2 % i == 0):
        gcd = i
    i += 1
print(f"GCD of {num1} and {num2} is {gcd}")
