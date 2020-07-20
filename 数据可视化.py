# 读取数据
import pandas as pd
import matplotlib.pyplot as plt
from pylab import mpl
import numpy as np
from mpl_toolkits.mplot3d import axes3d

# 设置字体
mpl.rcParams['font.sans-serif']=['FangSong']

df = pd.read_csv(r'必备-Excle数据可视化/data.csv',index_col='年份')
df.head()

# 将索引的值赋值给x
# x = df.index.values
# y = df['人均GDP（元）'].values

# 设置折线图一种写法
# fig,ax = plt.subplots()
# 设置颜色
# ax.plot(x,y,'r--*')
# 设置标题和横坐标
# ax.set(title='人均GDP走势图',xlabel='年份')
# plt.show()

# 设置折线图二种写法
# fig = plt.figure()
# ax = fig.add_subplot(111)
# 设置颜色
# ax.plot(x,y,'r--*')
# # 设置标题和横坐标
# ax.set(title='人均GDP走势图',xlabel='年份')
# plt.show()

# pandas中绘制函数
# df['人均GDP（元）'].plot(color='r')
# plt.show()

# 绘制柱形图
# df['人均GDP（元）'].plot(kind='bar',color='skyblue')
# plt.show()

# 不指定列，会将所有的列绘制出来
# df.plot()
# plt.show()

# 添加参数绘制不同的图形-柱形图
# df.plot(kind='bar')
# plt.show()

# 绘制堆积柱形图
# df.plot(kind='bar',stacked='True')
# plt.show()

# 饼图
# fig,ax = plt.subplots()
# # ax.pie(y[:5],labels=x[:5])
# ax.pie(y,labels=x)
# plt.show()

# 制作散点图
# 生成0-100的随机数，高40，宽40
data = np.random.randint(0,100,size=[40,40])
# x,y = data[0],data[1]
# ax = plt.subplot(111)
# ax.scatter(x[:10],y[:10],c='r')
# ax.scatter(x[10:20],y[10:20],c='b')
# ax.set_xlabel('x')
# ax.set_ylabel('y')
# plt.show()

# 生成三维散点图
# data[0]是第一行
# x,y,z = data[0],data[1],data[2]
# ax = plt.subplot(111,projection='3d')
# ax.scatter(x[:10],y[:10],z[:10],c='b')
# ax.scatter(x[10:20],y[10:20],z[10:20],c='r')
# ax.scatter(x[20:30],y[20:30],z[20:30],c='g')
# ax.set_xlabel('X')
# ax.set_zlabel('Z')
# ax.set_ylabel('Y')
# plt.show()

# 绘制词云图及jieba分词




