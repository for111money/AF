import cv2
import numpy as np
import time
import random#测试用

def get_center_crop(image, crop_width=300, crop_height=300):
    """截取图像中心区域"""
    h, w = image.shape[:2]
    x1 = w // 2 - crop_width // 2
    y1 = h // 2 - crop_height // 2
    x2 = x1 + crop_width
    y2 = y1 + crop_height
    return image[y1:y2, x1:x2]

def calculate_sharpness(image):
    """计算锐度（拉普拉斯方差）"""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    laplacian = cv2.Laplacian(gray, cv2.CV_64F)
    return laplacian.var()



if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    data_dirt = {}
    for i in range(10):
        if not cap.isOpened():
            raise RuntimeError("无法打开摄像头")
        ret, frame = cap.read()
        if not ret:
            print("无法读取视频帧")
            time.sleep(1)
            continue
        cropped = get_center_crop(frame)
        sharpness = calculate_sharpness(cropped)
        print(f"当前帧锐度: {sharpness:.2f}")
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        Encoder_value = random.random()
        data_dirt[i] = {'image': cropped,
                        'features': [sharpness, Encoder_value, timestamp]}
        cv2.imshow("Center Cropped Region", cropped)
        key = cv2.waitKey(2000)   # 延时2s
    max_sharpness = max(data_dirt, key=lambda k: data_dirt[k]['features'][0])
    print(f"最清晰图像的锐度是:{data_dirt[max_sharpness]['features'][0]:.2f}")
    cv2.imshow("Center Cropped Region", data_dirt[max_sharpness]['image'])
    key = cv2.waitKey(5000)  # 延时2s

    for key in data_dirt.keys():
        print(f"锐度值{data_dirt[key]['features'][0]:.2f}")
    cv2.destroyAllWindows()

    '''
            while True:
                ret, frame = cap.read()
                if not ret:
                    print("无法读取视频帧")
                    break

                cropped = get_center_crop(frame)
                sharpness = calculate_sharpness(cropped)

                cv2.imshow("Center Cropped Region", cropped)
                print(f"当前帧锐度: {sharpness:.2f}", end='\r')  # 覆盖输出

                key = cv2.waitKey(1) & 0xFF
                if key == ord('s'):
                    timestamp = time.strftime("%Y%m%d_%H%M%S")
                    saved_images[timestamp] = cropped.copy()
                    print(f"\n已保存当前帧到字典，键名为：{timestamp}")
                elif key == ord('q'):
                    break
        '''
