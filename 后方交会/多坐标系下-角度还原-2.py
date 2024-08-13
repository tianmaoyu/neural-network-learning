import sympy as sp

# 定义角度并转换为弧度  
yaw = sp.rad(145)
pitch = sp.rad(-47)
roll = sp.rad(-180)

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

# 计算总的旋转矩阵  
R_B = R_z * R_y * R_x

# 计算逆矩阵  
R_B_inv = R_B.inv()

# 初始向量（在B坐标系中的单位向量）  
v_initial = sp.Matrix([1, 0, 0])

# 转换到A坐标系  
v_A = R_B_inv * v_initial

# 打印在A坐标系中的方向分量  
print("在A坐标系中的方向分量: ", v_A)

# 计算新的欧拉角  
# 注意：在新的坐标系中计算欧拉角时，需要重新定义顺序  
# 这里我们假设新的坐标系使用的是与原始坐标系相同的欧拉角顺序（Z-Y-X）  

V_Ax, V_Ay, V_Az = v_A

# 计算新的欧拉角  
yaw_prime = sp.atan2(V_Ay, V_Ax)
pitch_prime = sp.asin(-V_Az)
roll_prime = sp.atan2(V_Az, V_Ay)  # 注意：这里的roll_prime可能不准确，需要根据具体情况调整  

# 转换为角度  
yaw_prime_deg = sp.deg(yaw_prime)
pitch_prime_deg = sp.deg(pitch_prime)
roll_prime_deg = sp.deg(roll_prime)

# 打印新的欧拉角  
print("新的偏航角（yaw'）: ", yaw_prime_deg.evalf())
print("新的俯仰角（pitch'）: ", pitch_prime_deg.evalf())
print("新的滚角（roll'）: ", roll_prime_deg.evalf())  
