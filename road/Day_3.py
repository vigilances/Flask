"""
__new__和__init__的区别

   1. __new__是一个静态方法,而__init__是一个实例方法.
   2. __new__方法会返回一个创建的实例,而__init__什么都不返回.
   3. 只有在__new__返回一个cls的实例时后面的__init__才能被调用.
   4. 当创建一个新实例时调用__new__,初始化一个实例时用__init__.

"""


def fun():
    pass

if __name__ == '__main__':
    fun()
    pass