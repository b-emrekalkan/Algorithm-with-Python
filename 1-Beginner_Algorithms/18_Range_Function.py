
#! PROBLEM: Get two numbers from user. If the first of these numbers is greater than the second, order all the numbers between these numbers from largest to smallest, otherwise from smallest to largest.

# input >>> 20,15
# output >> 20,19,18,17,16,15

# input >>> 16,20
# output >> 16,17,18,19,20

#? SOLUTION:

#* list(range(10))      👉 [0,1,2,3,4,5,6,7,8,9]
#* list(range(1,10))    👉 [1,2,3,4,5,6,7,8,9]
#! list(range(20,15))   👉 []
#! list(range(20,15,-1))   👉 [20,19,18,17,16]

n1 = int(input("Enter a number: "))
n2 = int(input("Enter a number: "))

if n1 < n2:
    print(list(range(n1,n2+1)))
elif n1 > n2:
    print(list(range(n1,n2-1,-1)))
else:
    print("The numbers you entered are equal")