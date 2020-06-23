import matplotlib.pyplot as plt
import math
import random
import numpy as np
# s=[]
# q=p=0
# for i in range(10000):
# 	s.append(random.randint(1,3))
# print(s)
# for i in range(10000):
# 	if(s[i]==1):
# 		q=q+1
# 	else:
# 		p=p+1
# print(q,p)
# for i in range(4):
# 	print(i)
# X=[]
# Y=[]
# for i in range(500):
# 	X.append(random.uniform(0,2*math.pi))
# X.sort()
# print(X[0])
# for i in range(500):
# 	Y.append(2*math.sin(X[i-1])+math.cos(X[i-1]))
# plt.plot(X,Y)
# plt.show()
# x=np.linspace(0,10,10000)
# y=np.sin(x)
# y.append(1)
# plt.plot(x,y)
# plt.show()
# for i in range(4,-1,-1):
# 	print(i)
# s=[[222,3],[41,5],[54,23]]
# s.sort()
# print(s)
# s.sort()
# for i in range(5):
# 	print(s[i])
num=[]
for i in range(10,501,10):
	num.append(i)
print(num)
loss=[773481,691626,428806,287944,189112,153025,109566,78747,
38271,21353,11186,7828,3157,2905,1901,634,1151,266,288,666,
150,500,600,455,555,444,666,11,222,448,
150,500,600,455,555,444,666,11,222,448,
150,500,600,455,555,444,666,11,222,448]
acc=[0.332,0.38,0.44,0.58,0.576,0.624,0.658,0.722,0.788,0.844,
0.888,0.91,0.964,0.962,0.968,0.98,0.962,0.99,0.98,0.99,
0.98,0.992,0.99,0.98,0.99,0.98,0.992,0.99,0.98,0.99,
0.98,0.992,0.99,0.98,0.99,0.98,0.992,0.99,0.98,0.99,
0.98,0.992,0.99,0.98,0.99,0.98,0.992,0.99,0.98,0.99]
plt.plot(num,acc)
plt.show()