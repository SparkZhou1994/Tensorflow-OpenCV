# 2-18
# matplotlib
import numpy as np
import matplotlib.pyplot as plt
# 折线图
x = np.array([1,2,3,4,5,6,7,8])
y = np.array([3,5,7,6,2,6,10,15])
plt.plot(x,y,'r',lw =2) # lw 折线宽度
plt.show()
# 柱状图
x = np.array([1,2,3,4,5,6,7,8])
y = np.array([13,25,17,36,21,16,10,15])
plt.bar(x,y,0.5,alpha=1,color='b')
plt.show()