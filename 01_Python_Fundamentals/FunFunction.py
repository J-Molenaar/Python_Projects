def odd_even(num1, num2):
    for i in range(num1, num2 + 1):
        if i % 2 == 1:
            print "Number is ", i, ". This is an odd number."
        else:
            print "Number is ", i, ". This is an even number."


odd_even(1, 10)


def multiply(arr, num):
    for x in range(len(arr)):
        arr[x] *= num
    return arr


a = [2, 4, 10, 16]
b = multiply(a, 5)
print b


def hacker(mult):
    for item in range(len(mult)):
        temparr = []
        for x in range(0, mult[item]):
            temparr.append(1)
        mult[item] = temparr
    return mult


print hacker(b)
