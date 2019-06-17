def foo(x):
    print("executing foo(%s)" % (x))


class A(object):
    def foo(self, x):
        print("executing foo(%s,%s)" % (self, x))

    @classmethod
    def class_foo(cls, x):
        print("executing class_foo(%s,%s)" % (cls, x))

    @staticmethod
    def static_foo(x):
        print("executing static_foo(%s)" % x)


a = A()
list = []
# a.class_foo("1")
# a.foo(1)
# a.static_foo(list)
# print("*" * 100)
#
# # 静态方法，类方法，实例方法
# A.class_foo("1")
# A.foo(a, "1")
# A.static_foo(list)


class Test(object):
    num_of_instance = 0

    def __init__(self, name):
        self.name = name
        Test.num_of_instance += 1


if __name__ == '__main__':
    print(Test.num_of_instance)  # 0
    t1 = Test('jack')
    print(Test.num_of_instance)
    t2 = Test('lucy')
    print(t1.name, t1.num_of_instance)
    print(t2.name, t2.num_of_instance)
