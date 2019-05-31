import matplotlib.pyplot as plt


def data_visualisation():
    squares = [1, 4, 9, 16, 25]
    plt.plot(squares, linewidth=5)
    #  设置图表标题，并给坐标轴加上标签
    plt.title("Square Numbers", fontsize=24)
    plt.xlabel("Value", fontsize=14)
    plt.ylabel("Square of Value", fontsize=14)
    #  设置刻度标记的大小
    plt.tick_params(axis='both', labelsize=14)
    plt.show()
    pass


if __name__ == '__main__':
    data_visualisation()
