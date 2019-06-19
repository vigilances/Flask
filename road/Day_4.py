# filter method
import copy
from functools import reduce


def test():
    a = [1, 2, 3, 4, 5, 6, 7]
    b = filter(lambda x: x > 5, a)
    print(type(b))
    pass


def test1():
    a = map(lambda x: x * 2, [1, 2, 3])
    print(list(a))


def test2():
    print(reduce(lambda x, y: x * y, range(1, 5)))


"""
= 、copy and deepcopy

deepcopy: 完全复制一个新对象，改变原有对象，不影响拷贝对象

copy： 1.对象中无复杂子对象，原来对象改变，不影响拷贝对象
       2.对象中有复杂子对象，原来对象改变（改变复杂子对象），会影响拷贝对象
       
=： 类似于引用传递

"""


def test3():
    a = [1, 2, 3, 4, ['a', 'b']]  # 原始对象
    b = a  # 赋值，传对象的引用
    c = copy.copy(a)  # 对象拷贝，浅拷贝
    d = copy.deepcopy(a)  # 对象拷贝，深拷贝
    a.append(5)  # 修改对象a
    a[4].append('c')  # 修改对象a中的['a', 'b']数组对象

    # [1,2,3,4['a','b','c'],5]
    print('a = ', a)
    # [1,2,3,4['a','b','c'],5]
    print('b = ', b)
    # [1, 2, 3, 4, ['a', 'b', 'c']]
    print('c = ', c)
    # [1, 2, 3, 4, ['a', 'b']]
    print('d = ', d)
    print(a is b, a is c, a is d)


"""
python 3 用 range代替了xrange，内部是生成器,减少内存消耗。
"""


def test4():
    for i in range(1, 10):
        print(i)


"""
 Cookie和Session
          
            Cookie 	                                                Session

储存位置 	客户端                                                 	服务器端
目的 	    跟踪会话，也可以保存用户偏好设置或者保存用户名密码等 	跟踪会话
安全性 	    不安全 	                                                安全

"""


def test5():
    pass


if __name__ == '__main__':
    # test()
    # test1()
    # test2()
    # test3()
    # test4()
    pass
