import cv2

def get_center_crop(image, crop_width=300, crop_height=300):
    """截取图像中心区域"""
    h, w = image.shape[:2]
    x1 = w // 2 - crop_width // 2
    y1 = h // 2 - crop_height // 2
    x2 = x1 + crop_width
    y2 = y1 + crop_height
    return image[y1:y2, x1:x2]

if __name__ =="__main__":
    # 加载原始图像
    image_path = r"D:\Desktop\visu_test\4-5\IMG_0006.jpg"
    image = cv2.imread(image_path)

    if image is None:
        raise FileNotFoundError("图像无法读取，请检查路径是否正确。")
    crop_width = 1400
    crop_height = 800
    # 截取中心区域
    crop = get_center_crop(image, crop_width, crop_height)

    # 在原图上画出截取框（绿色边框）
    h, w = image.shape[:2]
    x1 = w // 2 - crop_width//2
    y1 = h // 2 - crop_height//2
    x2 = x1 + crop_width
    y2 = y1 + crop_height
    image_with_box = image.copy()
    cv2.rectangle(image_with_box, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # 显示结果
    cv2.imshow("Original Image with Center Crop", image_with_box)
    cv2.imshow("Center Cropped Region", crop)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


