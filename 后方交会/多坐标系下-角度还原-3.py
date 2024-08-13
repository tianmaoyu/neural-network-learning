import numpy as np


def rotation_matrix(yaw, pitch, roll):
    Rz = np.array([
        [np.cos(yaw), -np.sin(yaw), 0],
        [np.sin(yaw), np.cos(yaw), 0],
        [0, 0, 1]
    ])
    Ry = np.array([
        [np.cos(pitch), 0, np.sin(pitch)],
        [0, 1, 0],
        [-np.sin(pitch), 0, np.cos(pitch)]
    ])
    Rx = np.array([
        [1, 0, 0],
        [0, np.cos(roll), -np.sin(roll)],
        [0, np.sin(roll), np.cos(roll)]
    ])
    return Rz @ Ry @ Rx


yaw_B, pitch_B, roll_B = np.deg2rad([145, -47, -180])
yaw_A, pitch_A, roll_A = np.deg2rad([-35, -47, 0])

R_B = rotation_matrix(yaw_B, pitch_B, roll_B)
R_A = rotation_matrix(yaw_A, pitch_A, roll_A)

R_B_inv = np.linalg.inv(R_B)
R_BA = R_A @ R_B_inv

print(R_BA)
