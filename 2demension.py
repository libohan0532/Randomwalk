import random
i=0#走路的计数器
x=0
y=0#设置初始位置
k=0#设置随机方向和大小
sumx=0
sumy=0
sumr2=0
sumr1=0
r=0
sumr=0#总位移的计数器
count=0#walk2函数调用次数
lst = [-1,1,2,-2]
def walk2(i,x,y,k):
    global sumr1,sumx,sumy
    while i<1000:
        k=random.choice(lst)
        if (k==-1) :
            x=-1
            y=0
        elif(k==1):
            x=1
            y = 0
        elif (k==-2) :
            y=-1
            x=0
        elif (k == 2):
            y = 1
            x=0
        sumx+=x
        sumy+=y
        i = i + 1

    sumr1 = sumx ** 2 + sumy ** 2
    sumx=0
    sumy=0



    print(sumr1,'某次实验的距离')
while count<1000:
    count += 1  # 全局变量怎样调用局部变量
    walk2(0,x,y,0)


    sumr2 += sumr1
print(sumr2, '方差')
print((sumr2) / 1000, '均方差')
print((sumr2 / 1000) ** 0.5, '均方根')
