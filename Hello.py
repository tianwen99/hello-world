
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

n = int(input('<<<'))
for i in range(2, n):
    if n % i == 0 :
        print('不是素数')
        break
else:
    print('是素数')























