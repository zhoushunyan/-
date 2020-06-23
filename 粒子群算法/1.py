import random
import numpy as np

x=np.random.uniform(-10, 10,10)
x1=np.random.uniform(-10, 10,10)
print(x)
print(x1)
q=np.greater(x,x1)
print(q)
x[q]=x1[q]
print(x)
print(x1)
area=(30*np.random.rand(10))**2
# print(area)
# z=np.square([1,2])
# print(x[:,1])
# print(y)