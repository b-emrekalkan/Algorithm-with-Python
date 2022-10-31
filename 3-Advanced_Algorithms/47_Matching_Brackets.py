
#! Create an algorithm that, when given a string containing only the characters '(', ')', '{', '}', '[' and ']', confirms that the parentheses in the string are opened and closed in the correct order and with the same type of parentheses.


"""
s = "()"         👉 True
s = "()[]{}"     👉 True
s = "(]"         👉 False
s = "([)]"       👉 False
s = "{[]}"       👉 True
"""

#? SOLUTION-1:

#* The pop() method 👉 removes the element at the specified position.

#* Syntax >>> list.pop(pos)

#* pos >>> 	Optional. A number specifying the position of the element you want to remove, default value is -1, which returns the last item

def match(chect_list):
    brackets = []
    garbage = []

    for i in chect_list:
        if i in ["(","{","["]:
            brackets.append(i)
        elif i == ")" and len(brackets) != 0 and brackets[-1] == "(":
            brackets.pop()
        elif i == "]" and len(brackets) != 0 and brackets[-1] == "[":
            brackets.pop()
        elif i == "}" and len(brackets) != 0 and brackets[-1] == "{":
            brackets.pop()
        else:
            garbage.append(i)

    print(brackets == [] and  garbage == [])

match("{[]}")


#? SOLUTION-2:

def match1(check_list):
    s = "".join([i for i in check_list])
    while "()" in s or "{}" in s or "[]" in s:
        s = s.replace("()","").replace("[]","").replace("{}","")
    print(s == "")

match1(["(",")","[","]"])