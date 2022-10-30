
#! PROBLEM: Write a program that takes a country's name and its area as arguments and returns the area of the country's proportion of the total world's landmass.
# The total world's landmass is 148,940,000 (km ** 2)

#? SOLUTION:

country = input("Enter country name")
area = input("Enter the area of the country")
earth = 148940000

#* The round() function 👉 returns a floating point number that is a rounded version of the specified number, with the specified number of decimals. The default number of decimals is 0, meaning that the function will return the nearest integer 👇

percentile = round((int(area) / earth) * 100,2)

print(f"{country} is {percentile}% of the total world's landmass")
