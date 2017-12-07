# PART I
# Sets up a for loop where count is an emplty variable which tracks odd values as the code loops
for count in range(0, 1000):
    if count % 2 == 1:
        print count
    else:
        continue

# Part II
# Sets up a for loop where count is an emplty variable which tracks values
# divisable by 5 as the code loops

for count in range(5, 1000000):
    if count % 5 == 0:
        print count
    else:
        continue

# print the sum of all the values in the list: a = [1, 2, 5, 10, 255, 3]
a = [1, 2, 5, 10, 255, 3]
print sum(a)

# print the average of the values in the list: a = [1, 2, 5, 10, 255, 3]
a = [1, 2, 5, 10, 255, 3]
print sum(a) / len(a)
