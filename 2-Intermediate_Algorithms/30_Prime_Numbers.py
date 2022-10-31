
#! Prime Numbers:

#? SOLUTION-1:

y = int(input("Enter a number greater than 1: "))

if y > 1:

    count = 0

    for i in range(2,y):
        if y % i == 0:
            count += 1
    if count == 0:
        print(y, " is a Prime Number.")
    else:
        print(y, " is not a Prime Number")
else:
    print("Check and enter a number greater than 1 !")


#? SOLUTION-2 (Prime Numbers in 2-50):

prime_numbers = []

for y in range(2,50):

    counts = 0

    for i in range(2,y):
        if y % i ==0:
            counts +=1

    if count == 0:
        prime_numbers.append(y)

print(prime_numbers)