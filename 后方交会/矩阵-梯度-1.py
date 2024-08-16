import numpy as np
import matplotlib.pyplot as plt

# 生成示例数据
np.random.seed(0)
x_data = np.linspace(0, 1, 100)
a_true = 2.0
b_true = 1.5
c_true = 0.5
y_data = a_true * np.exp(b_true * x_data) + c_true + np.random.normal(scale=0.1, size=x_data.shape)


# 定义SVD分解求解函数
def solve_linear_system_via_svd(A, y):
    U, S, Vt = np.linalg.svd(A, full_matrices=False)
    S_inv = np.diag(1 / S)
    A_pseudo_inv = Vt.T @ S_inv @ U.T
    return A_pseudo_inv @ y


# 初始猜测
b = 1.0

# 迭代优化 b
for iteration in range(100):
    # 构建线性系统
    A = np.column_stack((np.exp(b * x_data), np.ones_like(x_data)))
    params = solve_linear_system_via_svd(A, y_data)

    a, c = params

    # 计算更新后的 b
    y_pred = a * np.exp(b * x_data) + c
    error = y_data - y_pred
    grad_b = -2 * np.sum(error * a * x_data * np.exp(b * x_data))
    learning_rate = 0.001
    b -= learning_rate * grad_b

print(f"Estimated parameters: a={a}, b={b}, c={c}")

# 可视化
plt.figure()
plt.scatter(x_data, y_data, label='Data')
plt.plot(x_data, a * np.exp(b * x_data) + c, 'r-', label='Fit')
plt.legend()
plt.show()
