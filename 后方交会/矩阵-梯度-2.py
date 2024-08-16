import numpy as np

def loss_function(theta, X, y):
    predictions = X @ theta
    residuals = y - predictions
    return 0.5 * np.linalg.norm(residuals) ** 2

def gradient(theta, X, y):
    predictions = X @ theta
    residuals = y - predictions
    return -X.T @ residuals

# 构造 X 矩阵的函数
def construct_X(x, b):
    exp_term = np.exp(b * x)
    ones = np.ones_like(x)
    return np.column_stack((exp_term, x, ones))

# 示例数据
x = np.linspace(0, 3, 50)
y = 3 * np.exp(-1 * x) + 0.1 + 0.1 * np.random.randn(x.size)
b_guess = -1  # 初始猜测 b 的值

# 构造 X 矩阵
X = construct_X(x, b_guess)

# 初始猜测 a, b, c 的值
theta_guess = np.array([1, b_guess, 1])

# 计算损失函数和梯度
loss = loss_function(theta_guess, X, y)
gradient_val = gradient(theta_guess, X, y)

print("Initial Loss:", loss)
print("Gradient:", gradient_val)