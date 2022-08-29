# -*- coding: utf-8 -*-

# 去除微博右下角水印（截取）
import cv2
import os
import numpy as np


def do_remove(img, h_start, h_end, w_start, w_end):
    # 开始操作
    return img[h_start:h_end, w_start:w_end]


def remove_water_mark(image_name, image_root, save_root):
    if '.gif' in image_name or '.DS_Store' in image_name:
        return
    # print(os.path.join(image_root, image_name))
    img = cv2.imread(os.path.join(image_root, image_name))
    height, width = img.shape[0:2]
    # 计算操作区域
    # 右下角
    h_start = 0
    h_end = int(height - height * 0.07)
    w_start = 0
    w_end = width
    # img = do_remove(img, h_start, h_end, w_start, w_end)
    img = img[h_start:h_end, w_start:w_end]
    cv2.imshow("image", img)

    # 保存图片
    filename = os.path.join(save_root, image_name)
    cv2.imwrite(filename, img)


# 遍历文件
file_root = ""
img_files = []
for root, dirs, files in os.walk(r"D:\test_image"):
    file_root = root  # 当前目录路径
    img_files = files  # 当前路径下所有非目录子文件

for img_name in img_files:
    remove_water_mark(img_name, file_root, r"D:\weibo")

