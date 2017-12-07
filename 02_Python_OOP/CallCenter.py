from datetime import datetime
from datetime import time
import string
import random


class Call(object):
    def __init__(self, number, reason):
        self.name = ""
        self.phone_num = number
        self.reason = reason
        self.date = datetime.now().strftime("%b %d %Y %H:%M:%S")
        self.datetime = datetime.now()
        self.id = self.id_generator()

    def id_generator(self):
        return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(6))

    def dispAt(self):
        print self.name
        print self.phone_num
        print self.reason
        print self.date
        print self.id
        return self

class Center(object):
    def __init__(self):
        pass
    def list(self):
        print call_list
        return self
    def qsize(self):
        print len(call_list)
        return self
    def addcall(self, un, name, number, time, reason):
        Call(un, name, number, time, reason)
        return self
    def removecall(self):
        del call_list[0]
        return self
    def info(self):
        for i in call_list:
            print i['name'], i["number"]
        print len(call_list)
# class CallCenter(object):
#     def
#
#     def add(self):
#
#
#     def remove(self):
#         del arr[0]


person1 = Call("555-1234", "Tech support")
print "Who are you"
person1.name = raw_input()
person1.dispAt()
