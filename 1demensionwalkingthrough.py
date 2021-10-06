import random
import matplotlib.pyplot as plt
i1=0
i2=0
i3=0#走路的计数器
j1=0
j2=0
j3=0#设置初始位置
k1=0
k2=0
k3=0#设置随机方向和大小
l1=[]
l2=[]
l3=[]
sum=0 #总位移的计数器
count=0 #walk2函数调用次数
xaix=[]
lst = [-1,1]#配合随机数生成器
def walk1(i1,i2,i3,j1,j2,j3,k1,k2,k3,l1,l2,l3,xaix):
    global sum
    while i1<1000:
        xaix.append(i1)
        k1=random.choice(lst)
        j1=j1+k1
        print(j1)
        l1.append(j1)
        i1=i1+1
    print(l1)
    while i2<1000:
        k2 = random.choice(lst)
        j2 = j2 + k2
        print(j2)
        l2.append(j2)
        i2 = i2 + 1
    print(l2)
    while i3<1000:
        k3 = random.choice(lst)
        j3 = j3 + k3
        print(j3)
        l3.append(j3)
        i3 = i3 + 1
    print(l3,'changdele')
    print(xaix,'xaix')
    plt.plot(xaix, l1,color='blue')
    plt.plot(xaix,l2,color="red")
    plt.plot(xaix, l3,color="yellow")
    plt.show()
walk1(0,0,0,0,0,0,0,0,0,[],[],[],[])