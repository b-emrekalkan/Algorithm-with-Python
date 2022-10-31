
#! Given a list of points on the analytical plane, a center point, and an integer k, find the k points closest to the center point.

"""
Example:

>> Given the list of points [(1,3), (5,2), (2,4)]
>> Center point (4,1)
>> k = 2
>> output 👉 [(5,2), (1,3)]
"""

#? SOLUTION:

def nearest_points(list1, cen, k):
    result = []

    for i in list1:
        a = ((i[0] - cen[0]) ** 2 + (i[1] - cen[1]) ** 2) ** 0.5
        result.append([a, i])

    return [v for k,v in sorted(result)[:k]]

print(nearest_points([(1,3), (5,2), (2,4)], (4,1), 2 ))