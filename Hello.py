
#x循环else子句,如果循环正常的执行结束，就执行else子句；如果使用break终止，else子句不会执行。
# while condition:
#     block
# else:
#     block
#
# for element in iteratable:
#     block
# else:
#     block


# for i in range(0):
#     print('...')
# else:
#     print('else')
#
#
# for i in range(1):
#     break
#     print('...')
# else:
#     print('else')

# # 1.打印一个边长为n的正方形
# var=int(input('<<<'))
# for i in range(var):
#     if i == 0 or i == (var-1):
#         print('*'*var)
#     else:
#         print('*'+' '*(var-2)+'*')
#
#
# n=int(input('<<<'))
# print('*'*n)
# a=n-2
# while a :
#     print('*'+' '*(n-2)+'*')
#     a-=1
# print('*'*n)


# z = 5
# for i in range(z) :
#     if i % (z-1) == 0 :
#         print('*'*z)
#     else :
#         print('*'+' '*(z-2)+'*')


# 坐标对称性
# 边为3，则-1 0 1，range(-1,2)
# 边为4，则-2 -1 0 1，range(-2,2)
# 边为5，则 -2 -1 0 1 2，range(-2,3)

# n = 4
# e = -( n // 2)
# for i in range( e, n + e ):
#     if i == e or i == n + e - 1:
#         print('*'*n)
#     else:
#         print('*' + ' '*(n-2)+ '*')
#

# 求100内所有奇数的和（2500）
# num = 0
# for i in range(1,100,2):
#     num += i
# print(num)

# 求1到5 阶乘之和
# s = 0
# j = 1
# for i in range(1,6):
#     j = j * i
#     s = s + j
# print(s)

# 给一个数，判定他是否是素数（一个大于1的自然数，只能被1和他本身整除）

# n = int(input('<<<'))
# for i in range(2, n):
#     if n % i == 0 :
#         print('不是素数')
#         break
# else:
#     print('是素数')

# <<<<<<< HEAD
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('j'+'*'+'i'+'='+str(j*i)+end=' ')
#     print( )
#
# =======
# num=500 #int
# n=6 #几位数
# w=10**(n-1)
# flag=False #假定还没有碰到第一个非零
# for i in range(n):
#     y=num//w
#     if flag or y:
#         print(y)
#         flag=True #从此开关打开
#     num=num%w
#     w = w//10
# >>>>>>> 2059383a2c611867e5dc1e14835e236c2fb90550
#
# 字符串练习：
# 用户输入一个数字，判断是几位数。
# 打印每一个数字，个十百千。。
# num = '1234556'
# print(len(num))
# for i in range(len(num)-1,-1,-1):
#     print(num[i])
# 打印每一个数字及其重复次数
# n = '12455'
# print(len(n))
# z = [0]*10 #[0,0,0,0,0,0,0,0,0,0]
# #迭代字符串本身的字符
# for i in n :
#     z[int(i)] += 1 #[0,1,1,1,1,2,0,0,0,0,0,0]
# for j in range(10):
#     if z[j] != 0 :
#         print('{} {}'.format(j,z[j]))

# 输入5个数，打印每个数的位数，将这些数升序打印。
# nums = []
# while len(nums) < 5 :
#     num = input('<<<').rstrip().lstrip(' 0')
#     if  not num.isdigit() :
#         continue
#     print(len(num))
#     nums.append(int(num))
# nums.sort()
# print(nums)
#
# print(bytes([0,1])
# print('a'.encode())

# num = b'abc'
# l = num[0]
# print(bytearray(b'abcde')[1])
#
#
# i = int.from_bytes(b'abc','big')
# print(i,hex(i))
# print(i.to_bytes(6,'big'))
#
# 求杨辉三角的第m行第k个元素（C（m-1，k-1））
# m = 6
# k = 5
# oldline = []
# for i in range(m) :#i=3
#     newline = [1]*(i+1)  #[1,1,1,1]
#     for j in range(i-1) :#j=0,1
#         newline[j+1] = oldline[j] +oldline[j+1] #
#     oldline = newline#[1,2,1]
#     print(newline)
# print(oldline[k-1])

# 给定一个3*3的方阵，反转打印
# 123    147
# 456》》258
# 789    369
# 0,0  1,0  2,0
# 0,1  1,1  2,1
# 0,2  1,2  2,2
# 看对角线159不动，其他的变换位置
# num = [[1,2,3],[4,5,6],[7,8,9]]
# for i in range(3) :
#     for j in range(i) :
#         if j<i :
#             num[i][j],num[j][i]=num[j][i],num[i][j]
# print(num)

# 123    14
# 456》》25
#        36

# num = [[1,2,3],[4,5,6]]
# #一次性创建目标矩阵[[0,0],[0,0],[0,0]]
# tm = [[0 for j in range(len(num)) ] for i in range(len(num[0])) ]
# for i in range(len(tm)) :#i=0,1,2
#     for j in range(len(tm[0])) :#j=0,1,2
#         tm[i][j] = num[j][i]
# print(tm)

# 随机产生10个数字
# 要求：
# 1.每个数字取值范围【1,20】
# import  random
# nums = [random.randrange(21) for _ in range(10)]
# # nums = [11,7,5,11,6,7,4,11]
# # 2.统计重复的数字有几个？分别是什么？
# length = len(nums)
# states = [0]*length #[0,0,0,0,0,0,0]
# samenums = []
# diffnums = []
# for i in range(length) :
#     # 状态不等于0说明已经被标记过，跳过，不用对比了，加快速度
#     if states[i] != 0:
#         continue
#     flag = False
#     count = 0
#     for j in range(1+i,length) :
#         if states[j] != 0:
#             continue
#         if nums[i] == nums[j] :
#             flag = True
#             states[j] = count +1
#             count += 1
#     if flag :
#         # states[i] = 1
#         states[i] = count +1
#         samenums.append((nums[i],count+1))
#     else :
#         diffnums.append(nums[i])
# print(samenums)
# print(diffnums)
# 3.统计不重复的数字有几个？分别是什么？
# 举例：11,7,5,11,6,7,4，其中2个数字重复，是7和11,3个数字没有重复，是4,5和7


t1 = (1,2)
t2 = 1,2
print(type(t1))
print(type(t2))


lst=(3,5)
first,second=lst
print(first,second)
print(first,second)


a,*b=2,6,9,8,3,5,5
print(a,b)

lst = [1,(2,3,4),5]
a,b,c=lst
print(b[2])

































