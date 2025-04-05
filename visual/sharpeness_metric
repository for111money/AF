import cv2
import numpy as np


def calculate_sharpness_in(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # 读取灰度图像
    laplacian = cv2.Laplacian(image, cv2.CV_64F)  # 计算拉普拉斯梯度
    sharpness = laplacian.var()  # 计算方差
    return sharpness

def calculate_sharpness(croped_image):
    gray = cv2.cvtColor(croped_image, cv2.COLOR_BGR2GRAY)
    laplacian = cv2.Laplacian(gray, cv2.CV_64F)
    return laplacian.var()


if __name__ == "__main__":
    image_path = r"D:\Desktop\visu_test\4-5\IMG_0006.jpg"  # 替换为你的图像路径
    sharpness = calculate_sharpness_in(image_path)
    print(f"图像锐度: {sharpness}")
