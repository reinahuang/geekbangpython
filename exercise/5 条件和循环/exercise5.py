# 练习一 条件语句的使用
# 使用if语句判断字符串的长度是否等于10，根据判断结果进行不同的输出
first_string = input("Please input a string: ")
if len(first_string) == 10:
    print(first_string + " The length equal 10")
else:
    print("The length of" + first_string + "is: " + len(first_string))

提示用户输入一个1-40之间的数字，使用if语句根据输入数字的大小进行判断，如果输入的数字在 1-10，11-20，21-30，31-40，分别进行不同的输出
num = int(input("Please input a number between 1-40: "))
if num in (1, 10):
    print("Group A: 1-10")
elif num in (11, 20):
    print("Group B: 2-20")
elif num in (21, 30):
    print("Group C: 21-30")
elif num in (31, 40):
    print("Group D: 31-40")
else:
    print("Your input is out of our scope!")

# 练习二 循环语句的使用
# 使用for语句输出1-100之间的所有偶数
i = 0
result = []
print("#List The Even numbers between 1 and 100 ")
for num_a in range(1, 100):
    if(num_a % 2 == 0):
        i = i + 1
        result.append(num_a)
        #print("%s" %(num_a), end=' ')
print("Total are: %i" %(i))
print(result)

# 使用while语句输出1-100之间能够被3整除的数字
result = []
i = 1
n = 0
while i <= 100:
    if(i % 3 == 0):
        result.append(i)
        n = n + 1
    i = i + 1

print(str(n) + " numbers can be divided by 3 with no remainder.. " )
print(result)
