import numpy as np
import matplotlib.pyplot as plt

# 生成示例数据
np.random.seed(0)
x_data = np.linspace(0, 1, 100)
a_true = 2.0
b_true = 1.5
c_true = 0.5
y_data = a_true * np.exp(b_true * x_data) + c_true + np.random.normal(scale=0.1, size=x_data.shape)

# 初始化参数
a = np.random.rand()
b = np.random.rand()
c = np.random.rand()
learning_rate = 0.0001
num_iterations = 10000

# 梯度下降
for _ in range(num_iterations):
    y_pred = a * np.exp(b * x_data) + c
    error = y_data - y_pred

    grad_a = -2 * np.sum(error * np.exp(b * x_data))
    grad_b = -2 * np.sum(error * a * x_data * np.exp(b * x_data))
    grad_c = -2 * np.sum(error)

    a -= learning_rate * grad_a
    b -= learning_rate * grad_b
    c -= learning_rate * grad_c
    print(f"Estimated parameters: a={a}, b={b}, c={c}")

print(f"Estimated parameters: a={a}, b={b}, c={c}")

# 可视化
plt.figure()
plt.scatter(x_data, y_data, label='Data')
plt.plot(x_data, a * np.exp(b * x_data) + c, 'r-', label='Fit')
plt.legend()
plt.show()
