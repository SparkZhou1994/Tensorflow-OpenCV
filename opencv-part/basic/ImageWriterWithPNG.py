# PNG 无损压缩 透明度属性
import cv2
img = cv2.imread('E:/wallpaper/1.jpg', 1) # 0 gray 1 color
cv2.imwrite('E:/wallpaper/1 - Copy.png',img,[cv2.IMWRITE_PNG_COMPRESSION,50]) #IMWRITE_PNG_COMPRESSION 0~9 0压缩小

# Course 2-9
# 1 像素
# 2 RGB
# 3 颜色深度 8bit 0-255
# 4 w h 640*480
# 5 1.14M = 720*547*3*8 bit /8 (B)
# 6 RGB alpha
# 7 RGB bgr