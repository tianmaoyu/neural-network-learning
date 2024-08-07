import cv2
import numpy as np

source_list = np.array([[0, 0], [4000, 0], [0, 3000], [4000, 3000]])
target_list = np.array([[-3451, -2199], [7451, -2199], [191, 5199], [3809, 5199]])

homography_matrix, var = cv2.findHomography(source_list, target_list)
img = cv2.imread('pixel_to_gen_img/3.jpeg')
source_height, source_width = img.shape[:2]

# 取得透射矩阵 中的 第三列的 平移 量，x,y- (由于透射变换第三行第三列最后一个是 1，如果不为1 理论上对应缩放)
t_x = homography_matrix[0, 2]
t_y = homography_matrix[1, 2]

target_max = np.max(target_list, axis=0)
target_min = np.min(target_list, axis=0)
target_width = target_max[0] - target_min[0]
target_height = target_max[1] - target_min[1]

# 创建平移矩阵
trans_matrix = np.array([
    [1, 0, abs(t_x)],
    [0, 1, abs(t_y)],
    [0, 0, 1]
])
matrix = trans_matrix @ homography_matrix
dst = cv2.warpPerspective(img, matrix, (target_width, target_height))
cv2.imwrite('pixel_to_gen_img/3-Homography.jpeg', dst)
