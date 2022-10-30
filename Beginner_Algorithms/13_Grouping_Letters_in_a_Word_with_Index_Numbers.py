

#! PROBLEM: Write a Python dictionary function that takes a string from the user and matches each character in the string with the index number.

# input : "BESacademy"

# output: {0: 'B', 1: 'E', 2: 'S', 3: 'a', 4: 'c', 5: 'a', 6: 'd', 7: 'e', 8: 'm', 9: 'y'}

#? SOLUTION-1:

#* Dictionaries are used to store data values in key:value pairs. A dictionary is a collection which is ordered, changeable and do not allow duplicates. Dictionaries are written with curly brackets ( {} ), and have keys and values: 👇

""" thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
} """

x = input("Enter a word: ")

dict_1 = {}

for i in range(len(x)):
    dict_1[i] = x[i]
print(dict_1)

#? SOLUTION-2:

#* The enumerate() function 👉 takes a collection (e.g. a tuple) and returns it as an enumerate object. The enumerate() function adds a counter as the key of the enumerate object.

#* Syntax >>> enumerate(iterable, start)
#* iterable =>	An iterable object
#* start    => A Number. Defining the start number of the enumerate object. Default 0

y = input("Enter a word: ")

print(dict(enumerate(y)))

#? Output 👆 {0: 'B', 1: 'E', 2: 'S', 3: 'a', 4: 'c', 5: 'a', 6: 'd', 7: 'e', 8: 'm', 9: 'y'}

print(dict(enumerate(y,1000)))

#? Output 👆 {1000: 'B', 1001: 'E', 1002: 'S', 1003: 'a', 1004: 'c', 1005: 'a', 1006: 'd', 1007: 'e', 1008: 'm', 1009: 'y'}