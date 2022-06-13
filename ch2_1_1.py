import numpy as np
a=np.array([1,2,3,4,5,6])
b=np.reshape(a,(2,3))
print(b)
b[1,1]=20 #改變值會同時影響a b
print(b)
print(a)
b=np.reshape(a,(3,2),order="F")#針對行做運算
print(b)
b=np.arange(25).reshape((5,5),order="F")
print(b)

c=np.arange(15)
d=np.reshape(c,(3,5))
d=np.resize(c,(5,3))
print(d)
d=np.resize(c,(3,2)) #resize會裁減值
print(d)
d[0]=0 #resize不會影響源頭的值
print(d)
print(c)

a=np.arange(5)
a=np.append(a,[11,12,13,14,15]).reshape(2,5)
print(a)
b=np.append(a,[125,126])
print(b) #結構不同會被強制轉成一維陣列。
c=np.append(a,[[125,150,175,200,225]],axis=0) #axis=0 設定於零軸末端加入。
print(c) #以二軸形式加入。
e=np.array([[200,200,200,200,200],[200,200,200,200,200]])
ee=np.array([[100,100,100,100,100],[100,100,100,100,100]])
dd=np.append(ee,e,axis=0)
print(dd)
eee=np.append(ee,e,axis=1)
print(eee)

a=np.array([[1,1,1],[1,0,1],[1,0,1]])
print(np.all(a)) # 全部元素非為0則為True，否則false  
b=np.ones((3,3))#建立元素都是1的3x3陣列
print(b<2)
print(b*5>10)
print(np.all(a,axis=0))
print(np.all(a,axis=1))
print(np.all(a,axis=1,keepdims=True))#避免結果的降維
#np.all(a) == a.all()
#np.all(keepdims=True) == np.all(a,keepdims=True)