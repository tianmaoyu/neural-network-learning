import numpy as np

# 一元 二次方程
def GradientDescent():
    def func(x):
        return x ** 2 - 7 * x + 11

    def derivation(x):
        return 2 * x - 7

    count = 0
    learning_rate = 0.01
    current_x = -5
    while count < 5000:
        count += 1
        current_x = current_x - derivation(current_x) * learning_rate
        print(f'迭代次数count= {count},最小值={current_x}')


# 二元 二次方程 想x^2+y^2=f(x,y)
def GradientDescent_2():
    def derivationx(x):
        return 2 * x
    def derivationy(y):
        return 2 * y

    count = 0
    learning_rate = 0.01
    current_x = 5
    current_y = 5
    while count < 500:
        count += 1
        current_x = current_x - derivationx(current_x) * learning_rate
        current_y = current_y - derivationy(current_y) * learning_rate
        print(f'迭代次数count= {count},current_x={current_x} current_y={current_y}')

# 拟合线性回归模型
def GradientDescent_3():
    # 假设的数据集
    X = np.array([1, 2, 3, 4, 5])
    Y = np.array([2, 3, 5, 7, 11])

    # 初始化参数
    a = 0
    b = 0
    alpha = 0.01
    iterations = 1000

    # 梯度下降
    for _ in range(iterations):
        da = -2 * np.sum(X * (Y - (a * X + b)))
        db = -2 * np.sum(Y - (a * X + b))
        a -= alpha * da
        b -= alpha * db

    print(f"拟合直线方程为: y = {a:.2f}x + {b:.2f}")

GradientDescent_3()