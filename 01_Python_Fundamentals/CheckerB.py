for x in range(0, 9):
    if x % 2 == 1:
        print "* * * * "
        x += 1
    else:
        print " * * * *"
        x += 1

# alternative method
for i in range(0, 9):
    print ("* * * *")
    print (" * * * *")
