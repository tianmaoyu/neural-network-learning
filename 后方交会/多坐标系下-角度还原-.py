from sympy import symbols, Matrix

import  sympy as sp
yaw, pitch, roll = symbols('yaw pitch roll')

rotate_init = Matrix([
    [0, 1, 0],
    [1, 0, 0],
    [0, 0, -1]
])

# 定义旋转矩阵
R_z = sp.Matrix([
    [sp.cos(yaw), -sp.sin(yaw), 0],
    [sp.sin(yaw), sp.cos(yaw), 0],
    [0, 0, 1]
])
R_y = sp.Matrix([
    [sp.cos(pitch), 0, sp.sin(pitch)],
    [0, 1, 0],
    [-sp.sin(pitch), 0, sp.cos(pitch)]
])
R_x = sp.Matrix([
    [1, 0, 0],
    [0, sp.cos(roll), -sp.sin(roll)],
    [0, sp.sin(roll), sp.cos(roll)]
])

R = R_z * R_y * R_x

vector_init = sp.Matrix([1, 0, 0])

vector_b =  R * vector_init
vector_a = rotate_init.inv() * vector_b
ax,ay,az=vector_a

yaw_prime = sp.atan2(ay, ax)
pitch_prime = sp.asin(-az)
roll_prime = sp.atan2(az, ay)

# 转换为角度
yaw_prime_deg = sp.deg(yaw_prime)
pitch_prime_deg = sp.deg(pitch_prime)
roll_prime_deg = sp.deg(roll_prime)


yaw_value=145
pitch_value=-47
roll_value=-180
data={yaw:yaw_value, pitch:pitch_value,roll:roll_value}


# 打印新的欧拉角
print("新的偏航角（yaw'）: ", yaw_prime_deg.subs(data).evalf())
print("新的俯仰角（pitch'）: ", pitch_prime_deg.subs(data).evalf())
print("新的滚角（roll'）: ", roll_prime_deg.subs(data).evalf())