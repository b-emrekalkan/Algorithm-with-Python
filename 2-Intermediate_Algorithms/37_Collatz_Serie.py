
#! Get an integer from the user to create a Collatz Series. Create an algorithm that returns the series and the largest integer of the series.

# Collatz sequence is defined corresponding to n as the numbers formed by the following operations : If n is even, then n = n / 2. If n is odd, then n = 3*n + 1. Repeat above steps, until it becomes 1.

#? SOLUTION:


num = int(input("Please enter a positive number: "))

num_list = []

while num != 1:
    if num % 2 == 0:
        num = num / 2
    elif num % 2 == 1:
        num = num * 3 + 1
    num_list.append(num)
    print(num)

print(f"Maximum number is: {max(num_list)}")