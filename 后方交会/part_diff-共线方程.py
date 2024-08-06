import sympy as sp
from sympy import latex

from IPython.display import display, Math

# 定义符号
f, X, Y, Z, X_s, Y_s, Z_s = sp.symbols('f X Y Z X_s Y_s Z_s')
r11, r12, r13, r21, r22, r23, r31, r32, r33 = sp.symbols('r11 r12 r13 r21 r22 r23 r31 r32 r33')
# f = sp.Function('f')

# 定义函数 x 和 y
x = -f*(r11*(X-X_s) + r12*(Y-Y_s) + r13*(Z-Z_s)) / (r31*(X-X_s) + r32*(Y-Y_s) + r33*(Z-Z_s))
y = -f*(r21*(X-X_s) + r22*(Y-Y_s) + r23*(Z-Z_s)) / (r31*(X-X_s) + r32*(Y-Y_s) + r33*(Z-Z_s))

# 计算 x 和 y 关于 X_s 的偏导数
dx_dXs = sp.diff(x, X_s)
dy_dXs = sp.diff(y, X_s)

# # 打印结果
print("dx/dXs =", latex(dx_dXs))
print("dy/dXs =", latex(dy_dXs))

# # 将表达式转换为 LaTeX 格式
# latex_dx_dXs = sp.latex(dx_dXs)
# latex_dy_dXs = sp.latex(dy_dXs)
#
# display(Math(latex_dx_dXs))
# display(Math(latex_dy_dXs))