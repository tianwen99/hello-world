# # list1=[1,2,3]
# # list2=[1,2,3]
# # print(list1==list2)
# # print(list1 is list2)
# # print(id(list1))
# # print(id(list2))
# # list3=list1.copy()
# # print(id(list3))
# # list3.append([1,2])
# # print(list3)
# # print(list1)
# lis0=list(range(4))
# lis1=list(range(4))
# print(lis0==lis1)
# print(lis0 is lis1)
# lis2=lis0
# lis2[2]=200
# print(lis2==lis0)
# print(lis2 is lis0)
# lis3=lis1.copy()
# lis3.append([1,2])
# lis4=lis3.copy()
# print(lis3,lis4)
# lis4[-1][1]=200
# print(lis4,lis3)
# print(lis4 is lis3)
# print(lis4[-1] is lis3[-1])
# print(id(lis4))
# print(id(lis4[1]))
# print(lis3==lis1)
# print(lis3 is lis1)
# lis4=[]
# for i in lis3:
# 	lis4.append(i)
# print(lis4==lis3)
# print(lis4 is lis3)
# num=int(input('<<'))
# lnum=len(str(num))
# w=10000
# for i in range(lnum):
# 	print(num//w)
# 	num%=w 
# 	w//=10

# for i in range(lnum):
# 	print(num-(num//10)*10)
# 	num//=10

# num=00500
# n=5
# flag=False 
# for i in range(n):
# 	y=num//10**(n-1)
# 	if flag or y:
# 		print(y)
# 		flag=True
# 	num%=10**(n-1)
# 	n-=1

# a=min(2,4)
# print(a)
# b=round(3.5)
#math.floor()是向下取整
#math.ceil()是向上取整
#round()是
# import math
# # flo2=math.floor(-2.5)
# # flo1=math.ceil(-2.5)
# # print(flo2)
# # print(flo1)

# print(round(2.500001))
# print(round(5.4500000))

# 看当前路径
# import os
# print(os.getcwd())

# 第1题 给一个半径，求圆的面积和周长。圆周率为3.14

# r = float(input('r=:'))
# area=3.14*r**2
# c=2*3.14*r 
# # print(area)
# # print(c)


# # 第2题 输入两个数，比较大小后，从小到大升序打印
# # num1 = float(input('<<<'))
# # num2 = float(input('<<<'))
# # if num1 >= num2  :
# # 	print(num2, num1)
# # else:
# # 	print(num1, num2)

# # 第3题 输入一个成绩分数，判断学生成绩等级，A至E，其中，90分以上为'A'，80~89分为'B'， 70~79分为'C'，60~69分为'D'，60分以下为'E'
# score = float(input('成绩：'))
# if score >=90 :
# 	print('A')
# elif score >=80 :
# 	print('B')
# elif score >=70 :
# 	print('C')

# elif score >=60 :
# 	print('D')
# else :
# 	print('E')

# 第4题 死循环输入数字，输入后打印出之前输入的最大值和之前所有数字的平均数，如果输入的不是数字，而是quit字符串或者空格，则结束循环，退出程序。
# count = 1
# maxnum = 0
# sumnum = 0
# while True :
# 	strNum = input('input a num:')
# 	if strNum == '' or strNum == ' ' or strNum == 'quit' :
# 		print('game is over!')
# 		break
# 	intnum = int(strNum)
# 	sumnum += intnum
# 	avgnum = sumnum / count
# 	if intnum > maxnum :
# 		maxnum = intnum
# 	count += 1
# 	print(avgnum)
# 	print(maxnum)


# 第5题 用 * 打印一个边长为 n 的正方形，n 为整数。

# n = int(input('<<<'))
# e = -n//2
# for i in range(e,n+e) :
# 	if i == e or i == n+e-1 :
# 		print('*'*n)
# 	else :
# 		print('*'+' '*(n-2)+'*')


# 第6题 输入一个正整数n，求0到这个数以内的所有 奇数的和 与 偶数的和。
# intnum = int(input('input an int num.:'))
# sumnum1 = 0
# sumnum2 = 0
# for i in range(0,intnum,2) :
# 	sumnum1 += i 
# print('evenNum is:',sumnum1)
# for j in range(1,intnum,2):
# 	sumnum2 += j
# print('oddval is:',sumnum2)

# num = int(input('please input a num:'))
# evennum = 0
# oddnum = 0 
# for i in range(0,num+1) :
# 	if i %2 == 0 :
# 		evennum += i 
# 	else :
# 		oddnum += i 
# print('evennum is:',evennum)
# print('oddnum is:',oddnum)

# 方法一: 求1到n的阶乘结果之和
# 1=1*1
# 2=1*2
# 3=1*2*3
# 4=1*2*3*4
# n = int(input('n=:'))
# num = 1
# snum = 0 
# for i in range(1,n+1):
# 	num *= i 
# 	snum += num
# 	# print(num)
# print(snum)


# 输入一个整数，判断他是否是素数。
# num = int(input('input a num:'))
# for i in range(2,num) :
# 	if num % i == 0 :
# 		print(i)
# 		print('num is not a prime')
# 		break
# else :
# 	print('num is a prime')
import os
print(os.getcwd())





# 字符串习题
# 判断数字并打印
# 用户输入一个十进制正整数数字

# 判断是几位数
# 打印每一位数字及其重复的次数
# 依次打印每一位数字，顺序个、十、百、千、万...位


















