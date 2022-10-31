
#! Armstrong Number:

""" Example:
153 >> 1 ** 3 + 5** 3 + 3 ** 3 = 153
"""

#? SOLUTION-1:

num = input("Enter a number: ")

len_num = len(num)

sum_ = 0

for i in num:
    sum_ += int(i) ** len_num
if sum_ == int(num):
    print(num, " is an Armstrong Number.")
else:
    print(num, " is not an Armstrong Number.")


#? SOLUTION-2:

arms = []

for z in range(10,1001):
    num = str(z)
    toplam = 0

    x = len(num)

    for i in num:
        toplam += int(i)** x

        if int(num) == toplam:
            arms.append(num)

print(arms)