# 自省，
def test():
    a = [1, 2, 3]
    b = {'a': 1, 'b': 2, 'c': 3}
    c = True
    print(type(a), type(b), type(c))  # <type 'list'> <type 'dict'> <type 'bool'>
    print(isinstance(a, list))  # True

    pass


def fun():
    L = [x * x for x in range(10)]
    print(L)
    M = (x * x for x in range(10))
    for x in M:
        # print(x)
        print(M.__next__())
    pass


def print_everything(*args):
    for count, thing in enumerate(args):
        print('{0}. {1}'.format(count, thing))


def table_things(**kwargs):
    for name, value in kwargs.items():
        print('{0} = {1}'.format(name, value))


def print_three_things(a, b, c):
    print('a = {0}, b = {1}, c = {2}'.format(a, b, c))


if __name__ == '__main__':
    # test()
    fun()
    # print_everything('apple', 'banana', 'cabbage')
    # table_things(apple='fruit', cabbage='vegetable')
    # print_three_things(*['faq', 'idiot', 'virgin'])

    pass
