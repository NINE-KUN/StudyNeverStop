# 绘制简单的折线图
import matplotlib.pyplot as plt


def plot_test(squares,input_values):
    """
    :param squares:
    :return:
    """
    plt.style.use('bmh')
    fig, ax = plt.subplots()  # subplots可在一张图片中绘制一个或多个图表 fig表示整张图片 ax表示图片中的各个图表
    ax.plot(squares)

    plt.show()


if __name__ == '__main__':
    input_values = [1, 2, 3, 4, 5]
    squares = [1, 4, 9, 16, 25]
    plot_test(squares,input_values)
