# # Part I - Stars
x = [4, 6, 1, 3, 5, 7, 25]


def mult(arr):
    for i in arr:
        while i < len(arr):
            print ('*' * i)


print draw_stars(x)


# Part II - Stars and Letters
y = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]


def stars_letters(arr):
    for i in range(0, len(arr)):
        if type(arr[i]) == int:
            print ('*' * arr[i])
        elif type(arr[i]) == str:
            print (arr[i][0].lower() * len(arr[i]))
        i += 1


print stars_letters(y)
