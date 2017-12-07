import random
print "Staring program"
heads = 0
tails = 0
for i in range(0, 5000):
    random_num = random.randint(0, 1)
    if random_num == 0:
        heads += 1
        print "Attempt", i, "Throwing a coin... It's a heads! ... Got", heads, "so far and", tails, "so far."
    else:
        tails += 1
        print "Attempt", i, "Throwing a coin... It's a tails! ... Got", tails, "so far and", heads, "so far."
print "End of the program. Bye!"
