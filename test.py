# for i in range(1,10):
#     for j in range(1,i+1):
#         print(j,'*',i,'=',j*i,end='\t')
#     print( )
#
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('{}*{}={:<{}}'.format(j,i,i*j,2 if j< 2 else 3), end=' ')
#     print( )
#
# print('--------')

# unit = ' '*8
# for i in range(1,10):
#     print( unit* (i-1),end='')
#     for j in range(i,10):
#         print('{}*{}={:<{}}'.format(i,j,i*j,2 if j< 2 else 3), end=' ')
#     print( )


# for i in range(1,10):
#     # print( unit* (i-1),end='')
#     line = ''
#     for j in range(i,10):
#         line +='{}*{}={:<{}}'.format(i,j,i*j,2 if j< 2 else 3)
#     print('{:>66}'.format(line) )
#
# lis = [1,2]*3
# print(lis)
# lis[1]=30
# print(lis)
# lis1=[[1,2]]*3
# print(lis1)
# lis1[1][1]=40
# print(lis1)
# print(id(lis1[1]))
# print(id(lis1[0]))
# import random
# i = random.choice(range(1,7,2))
# print(i)
#
# j = random.randrange(1,7,2)
# print(j)
#
# a=random.sample((2,3,1,4),4)
# print(a)
# from collections import namedtuple
# point = namedtuple('i',['x','y','z'])
# p1=point(5,6,7)
# print(p1)

# 练习：依次接收用户输入的3个数，排序后打印
# 1.转换int后，判断大小排序。使用分支结构（if else结构）完成。

# num1 = input('<<<')
# num2 = input('<<<')
# num3 = input('<<<')
# num1 = int(num1)
# num2 = int(num2)
# num3 = int(num3)
# if num1 > num2 and num2 >num3:
#     print(num1,num2,num3)
# elif num1 > num2 and num2 < num3 and num1 >num3:
#     print(num1,num3,num2)
# elif num2 >num1 and num1 > num3 :
#     print(num2,num1,num3)
# elif num2 >num1 and num1 < num3 and num2 >num3:
#     print(num2,num3,num1)
# elif num3 >num1 and num1 >num2:
#     print(num3,num1,num2)
# else:
#     print(num3,num2,num1)

# 2.使用max函数
# num = []
# out = None
# for i in range(3):
#     num.append(int(input('<<<')))
# m = max(num)
# print(m)
# num.remove(m)
# m1 = max(num)
# print(m1)
# num.remove(m1)
# print(num[0])

# while num :
#     if len(num) == 1 :
#         print(num[0])
#         break
#     m = max(num)
#     print(m)
#     num.remove(m)

# 3.使用列表的sort方法
# num.sort()
# print(num)
# 4.冒泡法
# num = [4,6,8,2,3,1]
# for j in range(len(num)-1):#第几趟
#     print('第',j,'趟:')
#     for i in range(0,len(num)-1-j):#完成两两比较
#         if num[i] > num[i+1] :#交换
#             tmp = num[i]
#             num[i] = num[i+1]
#             num[i+1] = tmp
#         print('第',i,'次结果：',num)

# 冒泡排序优化，如果第一趟两两比较完没有交换过，说明就是我们要的了，后面就不用再走第二第三趟比较了，可以做一个标记，当没有交换时，结束循环。
# num = [1,2,3,6,5]
# count = 0 #两两比较多少次
# jh = 0 #交换多少次
# for j in range(len(num)-1):#第几趟
#     flag = False
#     for i in range(0,len(num)-1-j):#完成两两比较
#         count += 1
#         if num[i] > num[i+1] :#交换
#             tmp = num[i]
#             num[i] = num[i+1]
#             num[i+1] = tmp
#             jh += 1
#             flag = True
#     if not flag :
#         break
# print(num,count,jh)


# 100以内的所有素数个数
import datetime
n = 10000
count = 0
primenumbers = []
start =datetime.datetime.now()
for i in range(2,n):
    for j in primenumbers:#奇数都多，就用素数列表
        if i % j == 0:
            break
    else :
            count +=1
            primenumbers.append(i)
endtime = (datetime.datetime.now() - start).total_seconds()
print(endtime)
# print(count,primenumbers)

#合数等于素数的乘积

primenumbers = []
start =datetime.datetime.now()
for i in range(2,n):
    flag = False #不是合数
    f = i ** 0.5
    for j in primenumbers:#奇数都多，就用素数列表
        if i % j == 0:#找到了合数
            flag = True
            break
        if j > f :#找到了素数
            break
    if not flag  :
        count +=1
        primenumbers.append(i)
endtime = (datetime.datetime.now() - start).total_seconds()
print(endtime)
# print(count,primenumbers)

count = 0
primenumbers = []
start =datetime.datetime.now()
for i in range(2,n):
    for j in range(2,int(i**0.5)+1):#奇数都多，就用素数列表
        if i % j == 0:
            break
    else :
            count +=1
            primenumbers.append(i)
endtime = (datetime.datetime.now() - start).total_seconds()
print(endtime)

#以上结论，用上一次的结果，会大大减少运算时间

# 大于3时，素数的间隔是2和4或是6，如：5，7,11,13,17,19，23,29,31
# 大于3的素数只有6N-1和6N+1两种形式


x = 5
step1 = 2
count = 2
start =datetime.datetime.now()
while x <= n :
    for i in range(3,int(x**0.5)+1,2):
        if x % i == 0:
            break
    else :
        count += 1

    x += step1
    step = 4 if step1 == 2 else 2

endtime = (datetime.datetime.now() - start).total_seconds()
print(endtime)
print(count)

























