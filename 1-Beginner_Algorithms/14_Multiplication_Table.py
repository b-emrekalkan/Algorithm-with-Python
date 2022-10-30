
#! PROBLEM: The multiplication table.

#? SOLUTION:

a = int(input("Enter a number: "))

for i in range(11): # 👈 0,1,2,3,4,5,6,7,8,9,10
    print(f"{a} x {i} = {a* i}")
    # print("{} x {} = ".format(a,i), a * i)

# Output for "5" 👇
    """
    5 x 0 = 0
    5 x 1 = 5
    5 x 2 = 10
    5 x 3 = 15
    5 x 4 = 20
    5 x 5 = 25
    5 x 6 = 30
    5 x 7 = 35
    5 x 8 = 40
    5 x 9 = 45
    5 x 10 = 50
    """
