# try this either as a .py file or in the python shell
import turtle
# the distance we want the pointer to travel each time
DIST = 15
for x in range(0, 20):
    print "x", x
    for y in range(1, 4):
        print "y", y
        # turn the pointer 90 degrees to the right
        turtle.fillcolor("blue")
        turtle.fill("True")
        turtle.right(120)
        # advance according to set distance
        turtle.forward(DIST)
    # add to set distance
    DIST += 10
