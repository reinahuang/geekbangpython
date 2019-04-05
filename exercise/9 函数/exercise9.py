!/usr/bin/python
#-*- coding:utf-8 -*-

# 创建一个函数，用于接收用户输入的数字，并计算用户输入数字的和


def NumberSumup(x, y):
    sum = x + y
    return sum


try:
   n = input("Please input 2 numbers: ")
   (x, y) = (n[0], n[1])
except Exception as e:
    print (e)

print(NumberSumup(int(x), int(y)))


# 创建一个函数，传入n个整数，返回其中最大的数和最小的数

def comparetwonumber(x, y):
    try:
        if int(x) > int(y):
            return x
        else:
            return y
    except Exception as e:
        print(e)


n = input("Please input numbers separated by ',': ")
length = len(n) - 1
i = 0
max_num = 0
while i <= length:
    max_num = comparetwonumber(n[i], max_num)
    i = i + 1

print("The Max number is: " + str(max_num))
