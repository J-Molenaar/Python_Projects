# String -https://docs.python.org/2.6/library/string.html#string.find
#capitalize, upper, lower, count, find, index, split, join, replace, format

our_str = "jessica"
print our_str.capitalize()

print our_str.upper()
print our_str.lower()
print our_str.count("s")
print our_str.find("a")  # finds the lowest index value or -1 (or Failure) if there is none
print our_str.index("m")  # finds the lowest index value or an error if there is none
print our_str.index("s")
print our_str.rfind("s")  # finds the highest index value
print our_str.split()
our_str = "jessica monster"
print our_str.split(",")
print list(our_str)  # this is a function not a string method
# print our_str.list() #This is not a function and is BROKEN
l = list(our_str)
x = ""
print l
print x.join(l)  # must have two variables to make this work. ex use: list names on new line
print our_str.replace("s", "th")  # lisp generator
x = 1
y = 2
print "{}+{}=3".format(x, y)


# List - https://www.tutorialspoint.com/python/python_lists.htm
# len, max, min, index, append, pop, remove, insert, sort, reverse,
# (optional) extend, (optional) list
our_ls = [1, 4, "dog", 3, "baggel", 2]
print len(our_ls)
print min(our_ls)
# if list contains strings, it will use the ascii value of the first
# letter's ascii value in the string
print max(our_ls)
our_ls.sort()
print "list :", our_ls
print our_ls.index("dog")
print our_ls.append("cat")
print our_ls
print our_ls.pop()
print our_ls
print our_ls.remove("dog")
print our_ls
print our_ls.insert(2, "cat")
print our_ls
print our_ls.sort()
print our_ls
print our_ls.reverse()
print our_ls
# prints ['m', 'y', ' ', 'd', 'o', 'g', ' ', 'i', 's', ' ', 's', 'm', 'a', 'l', 'l']
print list("my dog is small")
print list(our_ls)  # prints ['dog', 'cat', 'baggel', 4, 3, 2, 1]

# USING .REMOVE or DEL to remove a specific type of element in an array/list
for i in range(len(myList) - 1, -1, -1):  # MUST work from end of array, decrement, and stop @-1 to capture 0
    if type(myList[i]) == int:
        myList.remove(myList[i])
    print len(myList)
print myList

myList = [1, 1, ‘abc’, 2, 2, ‘def’, 3, 3, ‘ghi’, 4, ‘jkl’, 5]
print myList
# range(start, end, increment)
for i in range(len(myList) - 1, -1, -1):
    if type(myList[i]) == int:
        del myList[i]
    print len(myList)

print myList
