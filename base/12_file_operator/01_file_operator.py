"""
    python 使用文件操作基本步骤
    1).首先通过open方法获得一个句柄
    2).通过句柄对文件进行读、写、创建等操作
    3）写结束关闭文件流
    1.创建一个文件，包含两种方式
    1）open("file","w") 创建文件，文件已经存在不会报错
    2)open（“file”,"x"） 创建文件，文件已经存在则会报错，是为了防止失误操作文件，将原文件覆盖


"""

# 创建一个文件 两种方式，一个通过指定操作为w，一个通过指定操作为x
# 文件已经存在会覆盖
import os
from os import path

import pathlib

# file_instance = open("a.txt", "w", encoding="utf-8")
# 文件存在程序会报错 FileExistsError: [Errno 17] File exists: 'b.txt'
# file_instance1 = open("b.txt", "x")


# 文件写入数据 write 与 writeline的区别是，write只能接收字符串，writeline可以接收任意参数
# file_instance.write("aaa\naa")
# file_instance.writelines("sssssss")
# file_instance.writelines("11111")
# file_instance.writelines(["a1", "b1", "c1", "d1", "e1", "f1"])
# 结束关闭流
# file_instance.close()

# 文件写入数据，追加写

file_instance2 = open("b.txt","a",encoding="utf-8")

file_instance2.write("\n我是中文")
file_instance2.close()

# 判断文件是否存在 1)根据os.path 判断 2）根据pathlib 判断
# print(path.exists("a.txt"))
# print(path.isfile("a.txt"))

# 重命名文件
try:
    os.rename("a.txt","a1.txt")
except FileNotFoundError:
    print("文件找不到")


# 删除文件
os.remove("b.txt")





path_instance= pathlib.Path("b1.txt")
print(path_instance.exists())



