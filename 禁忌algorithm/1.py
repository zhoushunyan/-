# -*-coding: utf-8-*-
import random
import datetime
import matplotlib.pyplot as plt
city = []
eg=[]
for line in open("tsp.txt"):
    place,lon,lat = line.strip().split(" ")
    city.extend([(place,(lon,lat))])  #导入城市的坐标
def printtravel(vec):
    print(city[0],city[vec[0]])
    for i in range(len(vec)-1):
        print(city[vec[i]],city[vec[i+1]])
    print(city[vec[i+1]],city[0])  #打印结果函数  
# eg=[i for i in range(1,29)]  #一个例
# printtravel(eg)
# print(city[0][1][0])

plt.plot([1,3],[3,4],c='r')
plt.plot([3,5],[4,6],c='r')
plt.plot([5,1],[6,3],c='r')
plt.show()