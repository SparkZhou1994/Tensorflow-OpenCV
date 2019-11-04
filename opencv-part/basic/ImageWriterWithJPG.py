# 图片写入
import cv2
img = cv2.imread('E:/wallpaper/1.jpg', 1) # 0 gray 1 color
cv2.imwrite('E:/wallpaper/1 - Copy.jpg',img,[cv2.IMWRITE_JPEG_QUALITY,50]) #IMWRITE_JPEG_QUALITY 0~100 0压缩大 图片质量差