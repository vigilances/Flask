from random import randrange, randint, sample


def qixingcai():
    list = []
    for _ in range(7):
        selected_balls = randint(0, 9)
        list.append(selected_balls)
    return list


def pailiesan():
    list = []
    for _ in range(3):
        selected_balls = randint(0, 9)
        list.append(selected_balls)
    return list


def main():
    print("七星彩：" + str(qixingcai()))
    print("排列三：" + str(pailiesan()))


if __name__ == '__main__':
    main()
