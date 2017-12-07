import random
print "Scores and Grades"
for i in range(0, 10):
    random_num = random.randint(60, 100)
    if random_num > 89:
        print "Score:", random_num, "; Your grade is A"
    elif random_num > 79 and random_num < 90:
        print "Score:", random_num, "; Your grade is B"
    elif random_num > 69 and random_num < 80:
        print "Score:", random_num, "; Your grade is C"
    elif random_num > 59 and random_num < 70:
        print "Score:", random_num, "; Your grade is D"
print "End of the program. Bye!"
