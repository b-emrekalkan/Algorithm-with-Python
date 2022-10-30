
#! Build an algorithm that detects amicable numbers.

""" Example:
220 >> [1,2,4,5,10,11,20,44,55,110] >> sum divisors = 284
284 >> [1,2,3,71,142] >> sum divisors = 220

=> 220 and 284 are Amicable Numbers <= """


#? SOLUTION-1:

x = int(input("Please enter a number: "))

sum_i = 0

for i in range(1, x):
    if x % i == 0:
        sum_i += i

sum_j = 0

for j in range(1, sum_i):
    if sum_i % j == 0:
        sum_j += j

if x == sum_j:
    print(f"{x} and {sum_j} are Amicable Numbers.")
else:
    print(f"{x} is a lonely number.")


#? SOLUTION-2:

#* The sum() function 👉 calculates the total of all numerical values in an iterable. sum() works with both integers and floating-point numbers. The sum() function has an optional parameter to add a number to the total. alculating the sum of a list is a common operation in Python. 👇

y = int(input("Please enter a number: "))

sum_ii = sum([i for i in range(1,y) if y % i == 0])

sum_jj = sum([j for j in range(1,sum_ii) if sum_ii % j == 0])

if y == sum_jj:
    print(f"{y} and {sum_jj} are Amicable Numbers.")
else:
    print(f"{y} is a lonely number.")