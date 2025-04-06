from image_cropping import get_center_crop
from Sharpness_metric import calculate_sharpness
import cv2


def record()






if __name__ == "__main__":
    image_path = r"D:\Desktop\visu_test\4-5\IMG_0006.jpg"
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"图像路径错误或无法读取：{image_path}")
    crop = get_center_crop(image)
    sharpness = calculate_sharpness(crop)
    cv2.imshow("Center Cropped Region", crop)
    print(f"图像锐度: {sharpness}")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
