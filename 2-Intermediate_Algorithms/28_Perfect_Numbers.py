
#! Try to find out if a number you get from the user is Perfect. A number is called a "Perfect Number" if the sum of its divisors is equal to itself.

# 6 is a Perfect Number >>> (1 + 2 + 3 = 6)

#? SOLUTION-1:

num = int(input("Enter a number: "))

divisors = []

for i in range(1, num):
    if num % i == 0:
        divisors.append(i)
print(sum(divisors))


#? SOLUTION-2:

if num == sum([i if num % i == 0 else 0 for i in range(1,num)]):
    print(f"{num} is a Perfect Number.")
else:
    print(f"{num} is not a Perfect Number.")