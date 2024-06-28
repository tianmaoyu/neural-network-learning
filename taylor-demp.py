def Taylor_equation():
    def func(x):
        return x ** 2 - 7 * x + 11

    def derivation(x):
        return 2 * x - 7

    count = 0
    current_x = 5
    while abs(func(current_x)) > 1e-5 and count < 5000:
        count += 1
        current_x = current_x - func(current_x) / derivation(current_x)
        print(f'迭代次数count= {count},result={current_x}')


def GradientDescent():
    def func(x):
        return x ** 2 - 7 * x + 11

    def derivation(x):
        return 2 * x - 7

    count = 0
    learning_rate=0.01
    current_x = -5
    while abs(func(current_x)) > 1e-5 and count < 5000:
        count += 1
        current_x = current_x -  derivation(current_x) *learning_rate
        print(f'迭代次数count= {count},最小值={current_x}')

GradientDescent()
