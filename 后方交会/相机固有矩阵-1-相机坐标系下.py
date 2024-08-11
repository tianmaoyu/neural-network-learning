import sympy as sp
from sympy import latex,simplify

from IPython.display import display, Math

# 定义符号 focal pixel width height
f, pixel, width, height, X, Y, Z, = sp.symbols('f pixel width height X Y Z ')

a1, a2, a3, b1, b2, b3, c1, c2, c3, Xs, Ys, Zs = sp.symbols('a1 a2 a3 b1 b2 b3 c1 c2 c3 Xs Ys Zs')

rotate_matrix = sp.Matrix([
    [a1, b1, c1, 0],
    [a2, b2, c2, 0],
    [a3, b3, c3, 0],
    [0, 0, 0, 1]
])
t_matrix = sp.Matrix([
    [1, 0, 0, Xs],
    [0, 1, 0, Ys],
    [0, 0, 1, Zs],
    [0, 0, 0, 1]
])
image_matrix = sp.Matrix([
    [1 / pixel, 0, 0, 0],
    [0, 1 / pixel, 0, width / (2 * pixel)],
    [0, 0, 1 / pixel, height / (2 * pixel)],
    [0, 0, 0, 1],
])

sensor_matrix = sp.Matrix([
    [-f, 0, 0, 0],
    [0, -f, 0, 0],
    [0, 0, -f, 0],
    [1, 0, 0, 0],
])
camera_init = sp.Matrix([
    [0, 1, 0, 0],
    [1, 0, 0, 0],
    [0, 0, -1, 0],
    [0, 0, 0, 1]
])

point = sp.Matrix([
    [X],
    [Y],
    [Z],
    [1]
])
# 把  点 映射到 相机坐标系下
k_matrix = image_matrix * sensor_matrix * (t_matrix * camera_init * rotate_matrix).inv() * point
# print(latex(k_matrix))

# 归一化 w轴，消掉 第4维
f_x = k_matrix[0] / k_matrix[3]
f_y = k_matrix[1] / k_matrix[3]
f_z = k_matrix[2] / k_matrix[3]

print("----"*10)
print(latex(simplify(f_x)))
print("----"*10)
print(latex(simplify(f_y)))
print("----"*10)
print(latex(simplify(f_z)))

print("----"*10)
display(latex(simplify(f_y)))

print("----"*10)
display(latex(simplify(f_z)))