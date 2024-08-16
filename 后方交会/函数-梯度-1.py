

import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt

# 损失函数
def residual(params, x, y):
    a, b, c = params
    return y - (a * np.exp(b * x) + c)
# 误差函数
def cost_function(params, x, y):
    return 0.5 * np.sum(residual(params, x, y)**2)
#梯度信息
def grad_cost_function(params, x, y):
    a, b, c = params
    r = residual(params, x, y)
    grad_a = -np.sum(r * np.exp(b * x))
    grad_b = -np.sum(r * a * x * np.exp(b * x))
    grad_c = -np.sum(r)
    return np.array([grad_a, grad_b, grad_c])

# 样本，
x_data = np.linspace(0, 3, 50)
y_data = 3 * np.exp(-1 * x_data) + 0.1 + 0.1 * np.random.randn(x_data.size)
#a,b,c 初始值
initial_guess = [1, -1, 1]
result = minimize(cost_function, initial_guess, args=(x_data, y_data),
                  method='L-BFGS-B', jac=grad_cost_function)

optimal_params = result.x
print("Optimal parameters: ", optimal_params)
plt.figure()
plt.scatter(x_data, y_data, label='Data')
plt.plot(x_data, optimal_params[0] * np.exp(optimal_params[1] * x_data) + optimal_params[2], 'r-', label='Fit')
plt.legend()
plt.show()


