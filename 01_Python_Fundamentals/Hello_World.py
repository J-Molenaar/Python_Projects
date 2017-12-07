print "Hello World"

# define a function that says hello to the name provided
# this starts a new block


def say_hello(name):
    # these lines are indented therefore part of the function
    if name:
        print 'Hello, ' + name + 'from inside the function'
    else:
        print 'No name'


# now we're unindented and have ended the previous block
print 'Outside of the function'

# EXAMPLE 2 - PRINTING STRING W/ VARIALBES
first_name = "Zen"
last_name = "Coder"
print "My name is {} {}".format(first_name, last_name)

name = "Jessica"
print "Hello", name
Hello Jessica

print "Hello" + name
HelloJessica


last = "Molenaar"
print "My name is {} {}".format(name, last)
My name is Jessica Molenaar

# EXAMPLE 3 - USING [:] TO PRINT PORTIONS OF A LIST/ARRAY
x = [99, 4, 2, 5, -3]
print x[:]
# the output would be [99,4,2,5,-3]
print x[1:]
# the output would be [4,2,5,-3];
print x[:4]
# the output would be [99,4,2,5]
print x[2:4]
# the output would be [2,5];
