#!/usr/bin/env python3


class UnMethodDemo(object):
    """My documentation for MethodDemo"""
    def __init__(self, arg):
        super(MethodDemo, self).__init__()
        self.arg = arg
class MethodDemo():
    a = 1

    @classmethod
    def classM(cls):
        print("Class Method. cls.a = ", cls.a)
        return "boring"

    @staticmethod
    def staticM():
        print("Static Method")
        return "surprise"

moo = MethodDemo()

print ("foo",moo.a,"hey hey")
print (MethodDemo.classM())


print ("staticm",moo.staticM())
print ("classm",moo.classM())