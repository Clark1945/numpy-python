import numpy as np
a=np.array([[[0,1,2,3],
             [4,5,6,7]],
             [[0,1,2,3],
             [4,5,6,7]]])
print(a)
print(a.shape)
b=a.sum(axis=0)#axis=0 2個元素加總
print(b)
b=a.sum(axis=1) #axis=1 2個元素加總
print(b)
b=a.sum(axis=2) #axis=2 4個元素加總
print(b)

c=np.array([0,1,2,3],dtype="int32")
print(c.dtype)

ar=[0,1,2,3,4]
print(ar[:])
ar=np.arange(20).reshape(4,5)
print(ar)
print(ar[2:4,1:4])

print("-------------------------------")
a=np.array([[1,2]])
b=np.array([3,4])
print(a+b)

a=np.array([1,2])
b=np.array([[3,4],[2,3]])
print(a+b)
#a進行增軸([1,2] >> [[1,2]]),進行增維([[1,2]] >> [[1,2],[1,2]])
