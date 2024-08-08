import numpy as np
import sympy
from sympy import latex, symbols, sin, cos, Matrix

# data 图片坐标(还原到)，地理坐标 单位 m
f = 0.15324
_Zs = 6129.6
data_image_list = [
    [-0.08615, -0.06899],
    [-0.0534, 0.08221],
    [-0.01478, -0.07663],
    [0.01046, 0.06443]
]
data_ground_list = [
    [36589.41, 25273.32, 2195.17],
    [37631.08, 31324.51, 728.69],
    [39100.97, 24934.98, 2386.5],
    [40426.54, 30319.81, 757.31]
]

# 旋转顺序 Z-Y-X,分别对应的角 yaw, pitch,roll 即:偏航,俯仰角,滚角
yaw, pitch, roll = symbols('yaw pitch roll')

rotate_z = Matrix([
    [cos(yaw), -sin(yaw), 0],
    [sin(yaw), cos(yaw), 0],
    [0, 0, 1]
])
rotate_y = Matrix([
    [cos(pitch), 0, sin(pitch)],
    [0, 1, 0],
    [-sin(pitch), 0, cos(pitch)]
])
rotate_x = Matrix([
    [1, 0, 0],
    [0, cos(roll), -sin(roll)],
    [0, sin(roll), cos(roll)]
])
rotate_matrix = rotate_z * rotate_y * rotate_x

# 旋转矩阵 个各元素
a1 = rotate_matrix[0, 0]
a2 = rotate_matrix[0, 1]
a3 = rotate_matrix[0, 2]

b1 = rotate_matrix[1, 0]
b2 = rotate_matrix[1, 1]
b3 = rotate_matrix[1, 2]

c1 = rotate_matrix[2, 0]
c2 = rotate_matrix[2, 1]
c3 = rotate_matrix[2, 2]
# X,Y,Z: 地面坐标; Xs,Ys,Zs: 相机坐标; x,y:照片坐标
X, Y, Z, Xs, Ys, Zs, x, y = symbols('X Y Z Xs Ys Zs x y')

# 共线方程
function_x = -f * (a1 * (X - Xs) + b1 * (Y - Ys) + c1 * (Z - Zs)) / (a3 * (X - Xs) + b3 * (Y - Ys) + c3 * (Z - Zs))
function_y = -f * (a2 * (X - Xs) + b2 * (Y - Ys) + c2 * (Z - Zs)) / (a3 * (X - Xs) + b3 * (Y - Ys) + c3 * (Z - Zs))

# 求偏导
a_11 = sympy.diff(function_x, Xs)
a_12 = sympy.diff(function_x, Ys)
a_13 = sympy.diff(function_x, Zs)
a_14 = sympy.diff(function_x, yaw)
a_15 = sympy.diff(function_x, pitch)
a_16 = sympy.diff(function_x, roll)

a_21 = sympy.diff(function_y, Xs)
a_22 = sympy.diff(function_y, Ys)
a_23 = sympy.diff(function_y, Zs)
a_24 = sympy.diff(function_y, yaw)
a_25 = sympy.diff(function_y, pitch)
a_26 = sympy.diff(function_y, roll)

value_Xs = 0
value_Ys = 0
value_Zs = 0
value_yaw = 0
value_pitch = 0
value_roll = 0
times = 0
A = np.zeros((8, 6))
L = np.zeros((8, 1))
while (times < 1000):

    for i in range(4):
        value_X, value_Y, value_Z = data_ground_list[i]

        key_value = {
            X: value_X,
            Y: value_Y,
            Z: value_Z,
            Xs: value_Xs,
            Ys: value_Ys,
            Zs: 6129.6,
            yaw:value_yaw,
            pitch:value_pitch,
            roll:value_roll,
        }

        approx_x = function_x.subs(key_value)
        approx_y = function_y.subs(key_value)

        L[i * 2, 0] = data_image_list[i][0] - approx_x
        L[i * 2 + 1, 0] = data_image_list[i][1] - approx_y

        A[i * 2, 0] = a_11.subs(key_value)
        A[i * 2, 1] = a_12.subs(key_value)
        A[i * 2, 2] = a_13.subs(key_value)
        A[i * 2, 3] = a_14.subs(key_value)
        A[i * 2, 4] = a_15.subs(key_value)
        A[i * 2, 5] = a_16.subs(key_value)

        A[i * 2 + 1, 0] = a_21.subs(key_value)
        A[i * 2 + 1, 1] = a_22.subs(key_value)
        A[i * 2 + 1, 2] = a_23.subs(key_value)
        A[i * 2 + 1, 3] = a_24.subs(key_value)
        A[i * 2 + 1, 4] = a_25.subs(key_value)
        A[i * 2 + 1, 5] = a_26.subs(key_value)

    # 最小二乘
    # delta = np.linalg.inv(A.T @ A) @ A.T @ L

    delta, residuals, rank, singular = np.linalg.lstsq(A, L, rcond=None)

    # 迭代减少误差
    value_Xs += delta[0][0]
    value_Ys += delta[1][0]
    value_Zs += delta[2][0]
    value_yaw += delta[3][0]
    value_pitch += delta[4][0]
    value_roll += delta[5][0]
    times += 1
    data={
        Xs:value_Xs,
        Ys:value_Ys,
        Zs:value_Zs,
        yaw:value_yaw,
        pitch:value_pitch,
        roll:value_roll
    }
    print(f"times:{times} :data:{data}")
    if (abs(delta[3]) < 1e-6) and (abs(delta[4]) < 1e-6) and (abs(delta[5]) < 1e-6):
        break

print(f"times:{times}")
