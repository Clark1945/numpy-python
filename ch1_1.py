import numpy as np
a=np.array([1,2,3]) #陣列轉換為ndarray
print(type(a))
print(a)
print(a*3)
print(a-15)
b=np.array([4,5,6])
print(a+b)
print(a*b)
#無法用除法

c=np.arange(10) #產生0-9的陣列
c=np.arange(0,10,2) # 產生 0 2 4 6 8 陣列

d=np.linspace(0,10,15) #切成15等分的陣列

e = np.array([[1,2,3,4],[5,6,7,8]])
print(e.shape)
e = np.array([[[1,2,3],[4,5,6],[7,8,9],[10,11,12]],[[13,14,15],[16,17,18],[19,20,21],[22,23,24]]])
print(e.shape)
e=np.arange(10)
print(e.reshape(10,1))
print(e.reshape(5,2))

import time
def calculate_time():
    a=np.random.randn(100000) #產生100000個數值
    b=list(a)
    startTime=time.time()
    for _ in range(1000):
        sum_l=np.sum(a)
    print("Using Numpy  %f sec"%(time.time()-startTime))
    startTime=time.time()
    for _ in range(1000):
        sum_2=sum(b)
    print("Without Numpy %f sec"%(time.time()-startTime))

#calculate_time() 得出使用numpy與list的計算效率差異。
print("----------------------------------------")
f=np.array([[1,2,3,4,10],[5,6,7,8,21]])
print(f.ndim) #得出幾維陣列。
print(f.shape)#得出內部結構。
print(f.T)#轉置矩陣。
print(f.data)#傳入記憶體位置。
print(f.dtype)#ndarray中元素的資料型別。
print(f.flat)#轉一維
print(f.imag)#虛數
print(f.real)#實數
print(f.size)#總元素數量。
print(f.itemsize)#每一個元素的記憶體使用量/bytes
print(f.nbytes)#所有元素的記憶體使用量bytes
print(f.strides)#=移動一部所需要的byte與需要移動的數量 4*5