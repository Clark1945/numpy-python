from matplotlib.pyplot import axis
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

a=np.random.randint(10,size=(2,3)) #0~9 建立2x3的陣列
print(a)
print(np.any(a==1)) 
print(np.any(a==9,axis=0))
print(np.any(a==9,axis=1))
print(np.any(a==9,axis=1,keepdims=True))
print((a%7==0).any())
b=np.random.randint(10,size=(2,3))
print(b)
print((a==b).any(axis=1,keepdims=True))#判斷一軸是否重複

b= np.arange(20,0,-2)
c=np.where(b<10) #符合條件的索引值
print(b)
print(c)
print(b[c])

a=np.arange(12).reshape(3,4)
print(np.where(a%2==0))
#[0,0,1,1,2,2],
#[0,2,0,2,0,2]  ==索引值 0-0 0-2 1-0 1-2

print(np.where(a%2==0,'even','odd'))
#print(np.where(a%2==0,'even')) ERROR
b=np.reshape(a,(3,4))
c=b**2
print(np.where(b%2==0,b,c))#符合條件不變，不符合用C取代
