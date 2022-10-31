
#! Anagram words refer to strings that have the same letters but are arranged differently. Group anagrams in a given string. The order ofyour output doesn't matter.

# Input     : ("eat","tea","tan","eat","nat","bat")

# Output    : (("eat","eat","tea"), ("nat","tan"),("bat"))

#? SOLUTION:

#* The values() method returns a view object. The view object contains the values of the dictionary, as a list. The view object will reflect any changes done to the dictionary, see example below.

#* Syntax >>> dictionary.values()


list1 = ["hi", "hello", "bye", "helol", "abc", "cab", "bac", "silenced", "licensed", "declines"]

result = {}

for item in list1:
    x = "".join(sorted(item)) # aet

    if x not in result:
        result[x] = [item]
    else:
        result[x].append(item)

print(list(result.values()))