import random
i=0#走路的计数器
j=0#设置初始位置
k=0#设置随机方向和大小
sum=0 #总位移的计数器
count=0 #walk2函数调用次数
lst = [-1,1]#配合随机数生成器
def walk1(i,j,k):
    global sum
    while i<1000:
        k=random.choice(lst)
        j=j+k
        i=i+1
        print(k)
    print(str(j),'某一次实验的位置变化')
    sum = j#记录该次实验的位移
sum2=0
while count<1000:
    walk1(0,0,0)
    count+=1
    sum2+=sum**2
print(sum2,'方差')
print((sum2)/1000,'均方差')
print((sum2/1000)**0.5,'均方根')