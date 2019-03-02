# 定义两个变量分别为美元和汇率
# 通过搜索引擎找到美元兑人民币汇率
# 使用Python计算100美元兑换的人民币数量并用print( )进行输出

dollar = 100
rate = 6.7
print(dollar*rate)
print('{dol}美元兑换的人民币数量为{yuan}'.format(dol=dollar, yuan=dollar * rate))

# 定义一个字符串Hello Python 并使用print( )输出
# 定义第二个字符串Let‘s go并使用print( )输出
# 定义第三个字符串"The Zen of Python" -- by Tim Peters 并使用print( )输出
message1 = 'Hello Python'
print(message1)
message2 = "Let's go"
print(message2)
message3 = '"The Zen of Python" -- By Tim Peters'
print(message3)

# 定义两个字符串分别为 xyz 、abc
# 对两个字符串进行连接
# 取出xyz字符串的第二个和第三个元素
# 对abc输出10次
# 判断a字符（串）在 xyz 和 abc 两个字符串中是否存在，并进行输出

a = 'xyz'
b = 'abc'
print(a+b)
x1, x2, x3 = a
print(x2+x3)
print(a[1:4])
print(b*10)
print('a' in a)
print('a' in b)

# 定义一个含有5个数字的列表
# 为列表增加一个元素 100
# 使用remove()删除一个元素后观察列表的变化
# 使用切片操作分别取出列表的前三个元素，取出列表的最后一个元素
mylist = [1,2,3,4,5]
mylist.append(100)
print(mylist)
mylist.remove(5)
print(mylist)
print(mylist[:3], mylist[-1])

