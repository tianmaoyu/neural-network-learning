﻿import numpy as np
from sympy import symbols, sin, cos, Matrix, simplify, latex

# 图片坐标
# image_list = [[0, 0], [4000, 0], [4000, 3000], [0, 3000]]

# 传感器 坐标 --位置应该还有问题
sensor_list = [
    [-0.0032, -0.00240],
    [0.0032, -0.0024],
    [0.0032, 0.0024],
    [-0.0032, 0.0024],
]

# 地理坐标,
geocoord_list = [
    [12623944.7985182, 2532805.94713418, 0],
    [12624109.3610210, 2532918.20406684, 0],
    [12624130.5637318, 2532769.04330686, 0],
    [12624075.9391505, 2532731.78094242, 0],
]

geocoord_list =  [[12710893.3666384, 2582819.24037641,0],
                  [12710889.2628446, 2582732.21988944,0],
                  [12710823.9312955, 2582735.21774206,0],
                  [12710828.0428850, 2582822.40407370,0]
                  ]

# 旋转顺序 Z-Y-X,分别对应的角 yaw, pitch,roll 即:偏航,俯仰角,滚角
yaw, pitch, roll = symbols('yaw pitch roll')
# X,Y,Z: 地面坐标; Xs,Ys,Zs: 相机坐标; x,y:照片坐标
X, Y, Z, Xs, Ys, Zs, x, y = symbols('X Y Z Xs Ys Zs x y')

# 已经知道的变量 f:焦距
f = 0.0044
width = 4000
height = 3000
pixel = 1.6 / 1000_000

camera_init = Matrix([
    [0, 1, 0, 0],
    [1, 0, 0, 0],
    [0, 0, -1, 0],
    [0, 0, 0, 1]
])
rotate_z = Matrix([
    [cos(yaw), -sin(yaw), 0, 0],
    [sin(yaw), cos(yaw), 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
])
rotate_y = Matrix([
    [cos(pitch), 0, sin(pitch), 0],
    [0, 1, 0, 0],
    [-sin(pitch), 0, cos(pitch), 0],
    [0, 0, 0, 1],
])
rotate_x = Matrix([
    [1, 0, 0, 0],
    [0, cos(roll), -sin(roll), 0],
    [0, sin(roll), cos(roll), 0],
    [0, 0, 0, 1],
])

t_matrix_inv = Matrix([
    [1, 0, 0, -Xs],
    [0, 1, 0, -Ys],
    [0, 0, 1, -Zs],
    [0, 0, 0, 1]
])

image_matrix = Matrix([
    [1, 0, 0, 0],
    [0, 1 / pixel, 0, width / (2 * pixel)],
    [0, 0, 1 / pixel, height / (2 * pixel)],
    [0, 0, 0, 1],
])

senor_matrix = Matrix([
    [-f, 0, 0, 0],
    [0, -f, 0, 0],
    [0, 0, -f, 0],
    [1, 0, 0, 0],
])

point = Matrix([
    [X],
    [Y],
    [Z],
    [1]
])

# 按照公式可以写出：但是求不出来
# k_matrix =  senor_matrix * (t_matrix * camera_init * rotate_z * rotate_y * rotate_x).inv() * point
# 只能手动先处理  正交矩阵
matrix_inv = (rotate_z * rotate_y * rotate_x).T * camera_init.T * t_matrix_inv
k_matrix = senor_matrix * matrix_inv * point

# 归一化 w轴，消掉 第4维
f_x = simplify(k_matrix[0] / k_matrix[3])
function_x = simplify(k_matrix[1] / k_matrix[3])
function_y = simplify(k_matrix[2] / k_matrix[3])
# print(latex(f_x))
# print(latex(function_x))
# print(latex(function_y))
# # 传感器安装在 x 轴上，不是在 z 轴，
function_Matrix = Matrix([function_x, function_y])

# 给第一些 初始评估值
value_Xs = 12710893
value_Ys = 2582819
value_Zs = -100
value_yaw = 0
value_pitch = 0
value_roll = 0

times = 0

# 构建公式： Ax=L
A = np.zeros((8, 6))
L = np.zeros((8, 1))

while (times < 100):

    for i in range(4):
        value_X, value_Y, value_Z = geocoord_list[i]

        key_value = {X: value_X, Y: value_Y, Z: value_Z, Xs: value_Xs, Ys: value_Ys, Zs: value_Zs, yaw: value_yaw,
                     pitch: value_pitch, roll: value_roll}
        # 评估值
        approx_x = function_x.subs(key_value)
        approx_y = function_y.subs(key_value)
        # 残差-误差
        L[i * 2, 0] = approx_x - sensor_list[i][0]
        L[i * 2 + 1, 0] = approx_y - sensor_list[i][1]

        # 计算雅克比矩阵
        Jacobian = function_Matrix.jacobian([Xs, Ys, Zs, yaw, pitch, roll])
        Jacobian_number = Jacobian.subs(key_value)
        item = np.array(Jacobian_number.tolist(), dtype=np.float64)

        A[i * 2:i * 2 + 2, :] = item

    # 最小二乘  Ax=L ： x=(A.T*A).Inv *A.T *L
    # delta = np.linalg.inv(A.T @ A) @ A.T @ L
    delta, residuals, rank, singular = np.linalg.lstsq(A, L, rcond=None)

    # 迭代减少误差
    value_Xs -= delta[0][0]
    value_Ys -= delta[1][0]
    value_Zs -= delta[2][0]
    value_yaw -= delta[3][0]
    value_pitch -= delta[4][0]
    value_roll -= delta[5][0]
    times += 1

    data = {Xs: value_Xs, Ys: value_Ys, Zs: value_Zs, yaw: np.rad2deg(value_yaw), pitch: np.rad2deg(value_pitch),
            roll: np.rad2deg(value_roll)}

    print(f"times:{times} :data:{data}")
    print(f"-------" * 6)
    print(f"残差：L:{L.tolist()}")

    if (abs(delta[3]) < 1e-6) and (abs(delta[4]) < 1e-6) and (abs(delta[5]) < 1e-6):
        break

print(f"times {times}")
