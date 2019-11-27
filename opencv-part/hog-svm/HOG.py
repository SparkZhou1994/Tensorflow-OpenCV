# 1.模块划分 2.梯度 方向 模板 3.bin 投影 4.每个模块hog
# 1.模块划分 image > win > block > cell
# win 64*128
# block 16*16 step 8*8 count((64-16)/8+1)*((128-16)/8+1) = 105
# cell 8*8 count 4
# 梯度 大小 f 方向 angle bin和方向有关 0-360度/40度 = 9 cell 包含9 bin
# 维度 hog向量 维度 = block个数*cell个数*bin个数
# 2.梯度
# 特征模板 [1,0,-1] [[1],[0],[-1]]
# a = p1*1+p2*0+p3*(-1) 相邻像素差
# b = 上下像素差
# f = 根号下(a方+b方)
# angle = arctan(a/b)
# 3. bin 投影
# bin 0 - 360 9 bin 0 -40
# bin1 0-20 180-200
# 25 bin1 bin2
# f1 = f*f(夹角) f2 = f*(1-f(夹角))  f(夹角) 0 - 1.0
# 或者直接+1 得到 hog映射
# hog*svm = 值 值>T 目标obj