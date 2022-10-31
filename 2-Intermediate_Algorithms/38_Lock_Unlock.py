
#! There are number of lockers "n" and number of students "n" in the school.

#! The principal asks the first students to go to every locker and open it. Then he has the second student go to every second locker and close it.

#! The third goes to every third locker and, if it is closed, he opens it, and if it is open, he closes it. The fourth studend does this to every fourth locker, and so on. After the process is completed with the "n"th student, how many lockers are open?


#? SOLUTION:

def locker(x):
    locker = [0 for i in range(x)]

    for i in range(x):
        for j in range(i, x, i+1):
            if locker[j] == 0:
                locker[j] = 1
            elif locker[j] == 1:
                locker[j] = 0

    return locker.count(1)

print(locker(7)) # 👉 2