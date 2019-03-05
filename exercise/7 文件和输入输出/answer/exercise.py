# 练习一 文件的创建和使用
# 创建一个文件，并写入当前日期
# 再次打开这个文件，读取文件的前4个字符后退出
import datetime

now = datetime.datetime.now()
f = open("test.txt", 'w')
f.write("Created by Reina")
f.write(str(now))


f = open("test.txt", 'r')
for i in f.readlines():
    print(i)
f.seek(0)
print(f.read(4))
print(f.tell())
f.close()
