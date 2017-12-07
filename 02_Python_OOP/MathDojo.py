
class MathDojo(object):
    def __init__(self):
        self.value = 0

    def add(self, *args):
        for arg in args:
            if isinstance(arg, (list, tuple)):  # Part 3 revised for tuples
                # if type(arg) is list or type(arg) is tuple: (This is alternative code)
                for num in arg:
                    self.value += num
            else:
                self.value += arg
        return self

    def subtract(self, *args):
        for arg in args:
            if isinstance(arg, (list, tuple)):
                # if type(arg) is list or type(arg) is tuple: (This is alternative code)
                for num in arg:
                    self.value -= num
            else:
                self.value -= arg
        return self

    def result(self):
        print self.value


part1 = MathDojo
part1().add(2).add(2, 5).subtract(3, 2).result()

part2 = MathDojo
part2().add([1], 3, 4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2, 3], [1.1, 2.3]).result()
